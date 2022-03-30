from django.db import models

from django.conf import settings
from django.urls import reverse

User = settings.AUTH_USER_MODEL

class Post(models.Model):

    commodity_name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to="post/")

    CATEGORIES = (
        ('mobile', 'Mobile'),
        ('electronics', 'Electronics'),
        ('laptops', 'Laptop'),
        ('cloth', 'Cloth'),
        ('house_utensils', 'House Utensil'),
        ('book', 'Book'),
        ('other', 'Other')
    )

    category = models.CharField(max_length=20,
                                choices=CATEGORIES)

    posted_date = models.DateTimeField(auto_now_add=True)

    poster = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    class Meta:
        ordering = ('-posted_date',)
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"id": self.id})
    
class Request(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received')

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent')
    offered = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="+", default=1)
    
    STATUSES = (
        ('accepted', 'accepted'),
        ('pending', 'pending')
    )

    status = models.CharField(max_length=15,
                              choices=STATUSES,
                              default='pending')

    offered_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-offered_date',)