from django.db import models

from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.urls import reverse

class User(AbstractBaseUser):

    objects = UserManager()

    fullname = models.CharField(max_length=50)
    username = models.CharField(unique=True, max_length=20, primary_key=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    password = models.TextField()

    profile_picture = models.ImageField(upload_to="profile/", default='profile/default.png')
    bio = models.TextField(null=True, blank=True, max_length=250, default="")
    company = models.CharField(max_length=50, null=True, blank=True, default="")

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    REQUIRED_FIELDS = ["fullname", "email", "phone", "password"]

    def get_absolute_url(self):
        return reverse("others_profile", kwargs={"username": self.username})
    
    def __str__(self):
        return self.fullname.title()
    
    def firstName(self):
        return self.fullname.split()[0]


class Verification(models.Model):
    email = models.EmailField(unique=True, primary_key=True)
    code = models.CharField(max_length=4)
