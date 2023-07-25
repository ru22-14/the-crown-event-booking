from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name="event_likes", blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Booking(models.Model):
    "Model for event"
    BOOKING_CHOICES = ((1, '08:00 AM - 12:00 PM'),
                       (2, '14:00 PM - 18:00 PM'),
                       (3, '20:00 PM - 00:00 AM'),
    )

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_bookings")
    date = models.DateField(null=True, blank=False)
    timeblock = models.IntegerField(null=True, blank=False, choices=BOOKING_CHOICES)
    theme = models.TextField(max_length=200, unique=True)
    guests = models.IntegerField(validators=[MinValueValidator(15), MaxValueValidator(50)])
    menu = models.CharField(max_length=100, unique=True)
    drinks = models.CharField(max_length=100, unique=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="user_bookings")
    useremail = models.EmailField(max_length=200, blank=True)
    approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.event} is booked by {self.username}'
    

class Comment(models.Model):
    """
    Model for comments
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                              related_name="comments")
    username = models.CharField(max_length=80)
    useremail = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.message} by {self.username}"       





