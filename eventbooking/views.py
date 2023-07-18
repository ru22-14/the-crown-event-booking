from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.views.generic import TemplateView, CreateView
from .models import Event, Booking
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
import datetime


# Create your views here.

class EventPageView(TemplateView):
    """
    events overview and pagination
    """
    model = Event
    template_name = 'index.html'
    
    
class EventListView(generic.ListView):
    model = Event
    queryset = Event.objects.filter(status=1).order_by('-created_on')
    template_name = 'events.html'
    paginate_by = 6

     


# class EventBooking(CreateView):
#     model = Booking
#     template_name = 'booking.html'
    
#     def booking(self, request):
#         submitted = False
#         if request.method == "POST":
#             form = BookingForm(request.POST)
#             if form.is_valid():
#                 booking.save()
#                 messages.success(request, 'you booked successfully')
#                 return HttpResponseRedirect('/booking?submitted=True')
#         else:
#             form = BookingForm
#             if 'submitted' in request.GET:
#                 submitted = True        
#         return render(request, 'booking.html', {'form': form, 'submitted': submitted, })


class EventBookingCreateView(CreateView):
    model = Booking
    template_name = 'booking.html'
    fields = '__all__'
    success_url = reverse_lazy('')  # URL to redirect after successful form submission

    def booking(self, request):
        submitted = False
        if request.method == 'POST':
            if form.is_valid():
                booking.save()
                messages.success(request, 'you submitted successfully')
            return HttpResponseRedirect('/events')
        else:
            if 'submitted' in request.GET:
                submitted = True        
            return HttpResponseRedirect('home')   
   
   