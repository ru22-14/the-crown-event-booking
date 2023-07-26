from django.contrib import admin
from .models import Event, Comment, Booking
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    """
    Add fields for event Posts in admin panel
    """

    list_display = (
        'title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')

    def publish_events(self, request, queryset):
        queryset.update(status=1)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Add fields for Comments in admin panel
    """
    list_display = ('event', 'date', 'timeblock', 'theme', 'guests', 'menu', 
                    'drinks','username', 'approved')
    list_filter = ('event', 'date', 'username', 'approved')  
    search_fields = ['event', 'username']
    actions = ['approved_booking']

    def approve_booking(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Add fields for Comments in admin panel
    """
    list_display = ('event', 'username', 'useremail', 'message', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['username', 'useremail', 'message']
    actions = ['approve_comments']
        
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)