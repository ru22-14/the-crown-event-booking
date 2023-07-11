from . import views
from django.urls import path


urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    path('all_events/', views.EventList.as_view(), name='all_events'),
]