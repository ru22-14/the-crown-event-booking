from . import views
from django.urls import path
from .views import EventPageView, EventListView, EventReviews, EventLike


urlpatterns = [
    path('', views.EventPageView.as_view(), name='home'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('comment/<slug:slug>', views.EventReviews.as_view(), name='event_comment'),
    # path('like/<slug:slug>', views.EventLike.as_view(), name='events'),
    
] 