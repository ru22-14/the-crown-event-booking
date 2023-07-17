from . import views
from django.urls import path
from .views import EventPageView, EventListView, EventBookingCreateView


urlpatterns = [
    path('', views.EventPageView.as_view(), name='home'),
    path("events/", views.EventListView.as_view(), name="events"),
    path("booking/", views.EventBookingCreateView.as_view(), name="booking"),
]