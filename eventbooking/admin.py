from django.contrib import admin
from .models import Event, Comment
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


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Add fields for Comments in admin panel
    """
    list_display = ('event', 'body', 'name', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approved_comments']
        
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)