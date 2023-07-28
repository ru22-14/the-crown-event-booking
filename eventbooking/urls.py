from . import views
from django.contrib import admin
from django.urls import path
from .views import EventPageView, EventListView, EventDetailView, EventLikeView, EventBookingView, MyBookingView, UpdateBookingView, DeleteBookingView


urlpatterns = [
    path('', views.EventPageView.as_view(), name='home'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('booking/', views.EventBookingView.as_view(), name='booking'),
    path('mybooking/', views.MyBookingView.as_view(), name='mybooking'),
    path('update_booking/update_booking<int:pk>', views.UpdateBookingView.as_view(), name='update_booking'),
    path('delete_booking/', views.DeleteBookingView.as_view(), name='delete_booking'),
    path('detail/<slug:slug>', views.EventDetailView.as_view(), name='events_detail'),
    path('like/<slug:slug>', views.EventLikeView.as_view(), name='event_like'),
    
    
] 