from . import views
from django.urls import path
from .views import EventPageView, EventListView, EventCommentView, EventLikeView, EventBookingView


urlpatterns = [
    path('', views.EventPageView.as_view(), name='home'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('comments<slug:slug>/', views.EventCommentView.as_view(), name='events'),
    path('like/<slug:slug>', views.EventLikeView.as_view(), name='events'),
    path('booking/', views.EventBookingView.as_view(), name='booking'),
    
] 