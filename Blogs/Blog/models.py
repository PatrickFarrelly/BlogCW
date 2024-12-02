from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    # Use 'author' instead of 'user' for clarity and consistency
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='blogs')
    
    blog_name = models.CharField(max_length=100)
    blog_description = models.TextField()
    blog_image = models.ImageField(upload_to="Blogs")
    blog_view_count = models.PositiveIntegerField(default=1)
    
    # Adding the created_at field to track when the blog post is created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_name

class Comment(models.Model):
    # ForeignKey to associate the comment with a blog
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    
    # ForeignKey to associate the comment with a user
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Text content of the comment
    text = models.TextField()
    
    # Auto-generated timestamp for when the comment was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.blog.blog_name}"



# from django.db import models
# from django.contrib.auth.models import User

# class Blog(models.Model):
#     # Use 'author' instead of 'user' for clarity and consistency
#     author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='blogs')
    
#     blog_name = models.CharField(max_length=100)
#     blog_description = models.TextField()
#     blog_image = models.ImageField(upload_to="Blogs")
#     blog_view_count = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return self.blog_name

# class Comment(models.Model):
#     # ForeignKey to associate the comment with a blog
#     blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    
#     # ForeignKey to associate the comment with a user
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     # Text content of the comment
#     text = models.TextField()
    
#     # Auto-generated timestamp for when the comment was created
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Comment by {self.author.username} on {self.blog.blog_name}"



# from django.db import models
# from django.contrib.auth.models import User

# class Blog(models.Model):
#     # ForeignKey to User (just like Recipe model)
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
#     # Renamed fields to match Recipe model naming convention
#     blog_name = models.CharField(max_length=100)
#     blog_description = models.TextField()
#     blog_image = models.ImageField(upload_to="Blogs")
#     blog_view_count = models.PositiveIntegerField(default=1)

#     # String representation of the model (returns the event name)
#     def __str__(self):
#         return self.blog_name
