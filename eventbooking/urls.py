from . import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import EventPageView, EventListView, EventDetailView, EventLikeView, EventBookingView, MyBookingView, UpdateBookingView, DeleteBookingView


urlpatterns = [
    path('', views.EventPageView.as_view(), name='home'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('booking/', login_required(views.EventBookingView.as_view()),
         name='booking'),
    path('mybooking/', login_required(views.MyBookingView.as_view()),
         name='mybooking'),
    path('update_booking/<int:booking_id>/', login_required(views.
         UpdateBookingView.as_view()), name='update_booking'),
    path('delete_booking/<int:booking_id>/', login_required(views.
         DeleteBookingView.as_view()), name='delete_booking'),
    path('detail/<slug:slug>', views.EventDetailView.as_view(),
         name='events_detail'),
    path('like/<slug:slug>', login_required(views.EventLikeView.as_view()),
         name='event_like'),
]