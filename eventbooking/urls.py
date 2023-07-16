from . import views
from django.urls import path
from .views import EventPageView, EventListView, EventBookingView


urlpatterns = [
    path('', views.EventPageView.as_view(), name='home'),
    path("events/", views.EventListView.as_view(), name="events"),
    path("booking/", views.EventBookingView.as_view(), name="booking"),
]