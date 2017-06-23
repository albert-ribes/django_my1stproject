from django import forms
from django.forms import ModelForm, TextInput
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'tags',)
        """widgets = {
            'tags': TextInput,
        }"""

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
