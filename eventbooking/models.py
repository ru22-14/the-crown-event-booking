from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Event(models.Model):
    "Model for event"
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    event = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="event_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    customer_full_name = models.CharField(max_length=200,
                                          blank=True)
    customer_email = models.EmailField(max_length=200, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-created_on"]


class Comment(models.Model):
    """
    Model for comments
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                              related_name="comments")
    name = models.CharField(max_length=85)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"       





