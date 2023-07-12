from . import views
from django.urls import path


urlpatterns = [
    path('', views.EventList.as_view(), name='home'),
    # path("event/", EventDetail.as_view(), name="events"),
]