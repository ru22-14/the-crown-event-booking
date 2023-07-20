from . import views
from django.urls import path
from .views import EventPageView, EventListView


urlpatterns = [
    path('', views.EventPageView.as_view(), name='home'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('events/', views.EventReviews.as_view(), name='events'),
    
] 