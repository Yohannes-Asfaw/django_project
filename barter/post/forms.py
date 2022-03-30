import imp
from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["commodity_name", "description", "image", "category"]

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["fullname", "phone", "profile_picture", "bio", "company"]