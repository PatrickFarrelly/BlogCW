from django import forms
from .models import Blog, Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['blog_name', 'blog_description', 'blog_image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']