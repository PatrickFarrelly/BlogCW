from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Comment  # Assuming Blog and Comment models exist
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BlogForm, CommentForm
from django.contrib.auth import logout


# View to handle Blog creation (for logged-in users)
@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  # Associate the blog with the logged-in user
            blog.save()
            messages.success(request, 'Your blog has been created successfully!')
            return redirect('blogs')  # Redirect to the list of blogs
    else:
        form = BlogForm()

    return render(request, 'blogs/create_blog.html', {'form': form})


# View to display all blogs and handle blog creation (if not logged in)
def blogs(request):
    queryset = Blog.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(blog_name__icontains=request.GET.get('search'))

    context = {'blogs': queryset}
    return render(request, 'blogs/blogs.html', context)


# View to display a single blog and its comments
def view_blog(request, id):
    blog = get_object_or_404(Blog, id=id)  # Get the blog or return 404 if not found
    comments = blog.comments.all()  # Assuming a related_name of `comments` in the Comment model
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.blog = blog  # Associate comment with the current blog
                comment.author = request.user  # Associate comment with the logged-in user
                comment.save()
                messages.success(request, 'Your comment has been added!')
                return redirect('view_blog', id=blog.id)
        else:
            messages.error(request, 'You need to be logged in to comment.')
    else:
        form = CommentForm()

    context = {
        'blog': blog,
        'comments': comments,
        'form': form  # Pass 'form' to the template to render the comment form
    }
    return render(request, 'blogs/view_blog.html', context)


# View to delete a blog (restricted to the original poster)
@login_required
def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    if request.user != blog.author:  # Check if the logged-in user is the blog author
        messages.error(request, "You are not authorized to delete this blog.")
        return redirect('blogs')  # Redirect to the blogs page

    if request.method == 'POST':  # Double-check for POST requests for delete
        blog.delete()
        messages.success(request, 'Blog deleted successfully!')
        return redirect('blogs')

    return render(request, 'blogs/confirm_delete.html', {'blog': blog})


# View to update a blog (restricted to the original poster)
@login_required
def update_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    if request.user != blog.author:  # Check if the logged-in user is the blog author
        messages.error(request, "You are not authorized to edit this blog.")
        return redirect('blogs')  # Redirect to the blogs page

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog updated successfully!')
            return redirect('view_blog', id=blog.id)
    else:
        form = BlogForm(instance=blog)

    return render(request, 'blogs/update_blog.html', {'form': form, 'blog': blog})


# API view for blogs
def api_blogs(request):
    blogs = Blog.objects.all()
    blogs_data = list(blogs.values())
    return JsonResponse({'blogs': blogs_data}, safe=False)


# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')  # Redirect to login page
    else:
        form = UserCreationForm()
    return render(request, 'blogs/register.html', {'form': form})


# View to handle user logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('blogs')  # Redirect to the home page after logout


# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Blog  # Assuming Blog model exists
# from django.http import JsonResponse
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required  # To ensure only logged-in users can create a blog
# from .forms import BlogForm  # Assuming you have a form for creating blogs (if not, we'll create one below)
# from django.contrib.auth import logout
# from django.views.decorators.http import require_POST
# from .models import Comment  # Assuming you have a Comment model
# from .forms import CommentForm  # Assuming you have a CommentForm for handling comment submissions

# # View to handle Blog creation (for logged-in users)
# @login_required
# def create_blog(request):
#     if request.method == 'POST':
#         form = BlogForm(request.POST, request.FILES)
#         if form.is_valid():
#             blog = form.save(commit=False)
#             blog.author = request.user  # Associate the blog with the logged-in user
#             blog.save()
#             messages.success(request, 'Your blog has been created successfully!')
#             return redirect('blogs')  # Redirect to the list of blogs
#     else:
#         form = BlogForm()

#     return render(request, 'blogs/create_blog.html', {'form': form})

# # View to display all blogs and handle blog creation (if not logged in)
# def blogs(request):
#     queryset = Blog.objects.all()

#     if request.GET.get('search'):
#         queryset = queryset.filter(blog_name__icontains=request.GET.get('search'))

#     context = {'blogs': queryset}
#     return render(request, 'blogs/blogs.html', context)

# # View to display a single blog and its comments
# def view_blog(request, id):
#     blog = get_object_or_404(Blog, id=id)  # Get the blog or return 404 if not found
#     comments = blog.comments.all()  # Assuming a related_name of `comments` in the Comment model
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             form = CommentForm(request.POST)
#             if form.is_valid():
#                 comment = form.save(commit=False)
#                 comment.blog = blog  # Associate comment with the current blog
#                 comment.author = request.user  # Associate comment with the logged-in user
#                 comment.save()
#                 messages.success(request, 'Your comment has been added!')
#                 return redirect('view_blog', id=blog.id)
#         else:
#             messages.error(request, 'You need to be logged in to comment.')
#     else:
#         form = CommentForm()

#     context = {
#         'blog': blog,
#         'comments': comments,
#         'form': form  # Pass 'form' to the template to render the comment form
#     }
#     return render(request, 'blogs/view_blog.html', context)

# # View to delete a blog
# def delete_blog(request, id):
#     queryset = Blog.objects.get(id=id)
#     queryset.delete()
#     return redirect('/')

# # View to update a blog
# def update_blog(request, id):
#     queryset = Blog.objects.get(id=id)

#     if request.method == 'POST':
#         data = request.POST
#         blog_image = request.FILES.get('blog_image')
#         blog_name = data.get('blog_name')
#         blog_description = data.get('blog_description')

#         queryset.blog_name = blog_name
#         queryset.blog_description = blog_description

#         if blog_image:
#             queryset.blog_image = blog_image

#         queryset.save()
#         return redirect('/')

#     context = {'blog': queryset}
#     return render(request, 'blogs/update_blog.html', context)

# # API view for blogs
# def api_blogs(request):
#     blogs = Blog.objects.all()
#     blogs_data = list(blogs.values())
#     return JsonResponse({'blogs': blogs_data}, safe=False)

# # User registration view
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}! You can now log in.')
#             return redirect('login')  # Redirect to login page
#     else:
#         form = UserCreationForm()
#     return render(request, 'blogs/register.html', {'form': form})

# # View to handle user logout
# @login_required
# def logout_view(request):
#     logout(request)
#     return redirect('blogs')  # Redirect to the home page after logout







# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Blog  # Assuming Blog model exists
# from django.http import JsonResponse
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required  # To ensure only logged-in users can create a blog
# from .forms import BlogForm  # Assuming you have a form for creating blogs (if not, we'll create one below)
# from django.contrib.auth import logout
# from django.views.decorators.http import require_POST
# from .models import Comment  # Assuming you have a Comment model
# from .forms import CommentForm  # Assuming you have a CommentForm for handling comment submissions

# # View to handle Blog creation (for logged-in users)
# @login_required
# def create_blog(request):
#     if request.method == 'POST':
#         form = BlogForm(request.POST, request.FILES)
#         if form.is_valid():
#             blog = form.save(commit=False)
#             blog.author = request.user  # Associate the blog with the logged-in user
#             blog.save()
#             messages.success(request, 'Your blog has been created successfully!')
#             return redirect('blogs')  # Redirect to the list of blogs
#     else:
#         form = BlogForm()

#     return render(request, 'blogs/create_blog.html', {'form': form})

# # View to display all blogs and handle blog creation (if not logged in)
# def blogs(request):
#     queryset = Blog.objects.all()

#     if request.GET.get('search'):
#         queryset = queryset.filter(blog_name__icontains=request.GET.get('search'))

#     context = {'blogs': queryset}
#     return render(request, 'blogs/blogs.html', context)

# # View to display a single blog and its comments
# def view_blog(request, id):
#     blog = get_object_or_404(Blog, id=id)  # Get the blog or return 404 if not found
#     comments = blog.comments.all()  # Assuming a related_name of `comments` in the Comment model
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#             form = CommentForm(request.POST)
#             if form.is_valid():
#                 comment = form.save(commit=False)
#                 comment.blog = blog  # Associate comment with the current blog
#                 comment.user = request.user  # Associate comment with the logged-in user
#                 comment.save()
#                 messages.success(request, 'Your comment has been added!')
#                 return redirect('view_blog', id=blog.id)
#         else:
#             messages.error(request, 'You need to be logged in to comment.')
#     else:
#         form = CommentForm()

#     context = {
#         'blog': blog,
#         'comments': comments,
#         'form': form
#     }
#     return render(request, 'blogs/view_blog.html', context)

# # View to delete a blog
# def delete_blog(request, id):
#     queryset = Blog.objects.get(id=id)
#     queryset.delete()
#     return redirect('/')

# # View to update a blog
# def update_blog(request, id):
#     queryset = Blog.objects.get(id=id)

#     if request.method == 'POST':
#         data = request.POST
#         blog_image = request.FILES.get('blog_image')
#         blog_name = data.get('blog_name')
#         blog_description = data.get('blog_description')

#         queryset.blog_name = blog_name
#         queryset.blog_description = blog_description

#         if blog_image:
#             queryset.blog_image = blog_image

#         queryset.save()
#         return redirect('/')

#     context = {'blog': queryset}
#     return render(request, 'blogs/update_blog.html', context)

# # API view for blogs
# def api_blogs(request):
#     blogs = Blog.objects.all()
#     blogs_data = list(blogs.values())
#     return JsonResponse({'blogs': blogs_data}, safe=False)

# # User registration view
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}! You can now log in.')
#             return redirect('login')  # Redirect to login page
#     else:
#         form = UserCreationForm()
#     return render(request, 'blogs/register.html', {'form': form})

# # View to handle user logout
# @login_required
# def logout_view(request):
#     logout(request)
#     return redirect('blogs')  # Redirect to the home page after logout


# from django.shortcuts import render, redirect
# from .models import Blog  # Changed from Event to Blog
# from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages

# # View to handle Blog creation
# def blogs(request):
#     if request.method == 'POST':
#         data = request.POST
#         blog_image = request.FILES.get('blog_image')  # Changed from event_image to blog_image
#         blog_name = data.get('blog_name')  # Changed from event_name to blog_name
#         blog_description = data.get('blog_description')  # Changed from event_description to blog_description

#         Blog.objects.create(  # Changed Event to Blog
#             blog_image=blog_image,
#             blog_name=blog_name,
#             blog_description=blog_description,
#         )
#         return redirect('/')

#     queryset = Blog.objects.all()  # Changed from Event to Blog

#     if request.GET.get('search'):
#         queryset = queryset.filter(
#             blog_name__icontains=request.GET.get('search'))  # Changed from event_name to blog_name

#     context = {'blogs': queryset}  # Changed from events to blogs
#     return render(request, 'blogs/blogs.html', context)  # Changed template name to blogs.html

# # View to delete a blog
# def delete_blog(request, id):
#     queryset = Blog.objects.get(id=id)  # Changed from Event to Blog
#     queryset.delete()
#     return redirect('/')

# # View to update a blog
# def update_blog(request, id):
#     queryset = Blog.objects.get(id=id)  # Changed from Event to Blog

#     if request.method == 'POST':
#         data = request.POST
#         blog_image = request.FILES.get('blog_image')  # Changed from event_image to blog_image
#         blog_name = data.get('blog_name')  # Changed from event_name to blog_name
#         blog_description = data.get('blog_description')  # Changed from event_description to blog_description

#         queryset.blog_name = blog_name  # Changed from event_name to blog_name
#         queryset.blog_description = blog_description  # Changed from event_description to blog_description

#         if blog_image:
#             queryset.blog_image = blog_image  # Changed from event_image to blog_image

#         queryset.save()
#         return redirect('/')

#     context = {'blog': queryset}  # Changed from event to blog
#     return render(request, 'blogs/update_blog.html', context)  # Changed template name to update_blog.html

# # API view for blogs
# def api_blogs(request):  # Changed from api_events to api_blogs
#     blogs = Blog.objects.all()  # Changed from Event to Blog
#     blogs_data = list(blogs.values())  # Fetching the data as a list of dictionaries
#     return JsonResponse({'blogs': blogs_data}, safe=False)  # Changed from events to blogs

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}! You can now log in.')
#             return redirect('login')  # Redirect to login page
#     else:
#         form = UserCreationForm()
#     return render(request, 'blogs/register.html', {'form': form})
