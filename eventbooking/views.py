from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views import generic, View
from .models import Event
from .models import Booking

# Create your views here.


class EventList(generic.ListView):
    """
    events overview and pagination
    """
    model = Event
    queryset = Event.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class EventDetails(View):
    """
    events overview and pagination
    """
    model = Event
    queryset = Event.objects.filter(status=1).order_by('-created_on')
    template_name = 'event.details.html'
    paginate_by = 6         