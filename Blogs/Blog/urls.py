from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),  # Display the blog list on the homepage
    path('create_blog/', views.create_blog, name='create_blog'),  # New URL to create a blog
    path('update_blog/<int:id>/', views.update_blog, name='update_blog'),
    path('delete_blog/<int:id>/', views.delete_blog, name='delete_blog'),
    path('api_blogs/v1/', views.api_blogs, name='api_blogs'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blogs/login.html'), name='login'),
    path('view_blog/<int:id>/', views.view_blog, name='view_blog'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]



# urlpatterns = [
#     path('', views.blogs, name='blogs'),  # Display the blog list on the homepage
#     path('update_blog/<int:id>/', views.update_blog, name='update_blog'),
#     path('delete_blog/<int:id>/', views.delete_blog, name='delete_blog'),
#     path('api_blogs/v1/', views.api_blogs, name='api_blogs'),
#     path('register/', views.register, name='register'),
#     path('login/', auth_views.LoginView.as_view(template_name='blogs/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Redirect to homepage after logout
#     path('create_blog/', views.create_blog, name='create_blog'),
# ]




# from django.urls import path
# from django.contrib.auth import views as auth_views
# from . import views

# urlpatterns = [
#     path('', views.blogs, name='blogs'),  # Display the blog list on the homepage
#     path('update_blog/<int:id>/', views.update_blog, name='update_blog'),
#     path('delete_blog/<int:id>/', views.delete_blog, name='delete_blog'),
#     path('api_blogs/v1/', views.api_blogs, name='api_blogs'),
#     path('register/', views.register, name='register'),
#     path('login/', auth_views.LoginView.as_view(template_name='blogs/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
# ] 




# from django.urls import path
# from django.contrib.auth import views as auth_views
# from . import views

# urlpatterns = [
#     path('', views.blogs, name='blog_list'),  # Changed to 'events' for event listing
#     path('update_blog/<int:id>/', views.update_blog, name='update_blog'),  # Changed to update an event
#     path('delete_blog/<int:id>/', views.delete_blog, name='delete_blog'),  # Changed to delete an event
#     path('api_blogs/v1/', views.api_blogs, name='api_blogs'),  # Changed to align with events API
#     path('register/', views.register, name='register'),  # Custom registration view
#     path('login/', auth_views.LoginView.as_view(template_name='blogs/login.html'), name='login'),  # LoginView
#     path('logout/', auth_views.LogoutView.as_view(template_name='blogs/logout.html'), name='logout'),  # LogoutView
#     path('', views.blogs, name='blogs'),  # Your existing blogs page
# ]
