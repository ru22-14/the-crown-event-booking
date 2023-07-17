from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.views.generic import TemplateView, CreateView
from .models import Event, Booking
from .forms import BookingForm
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
    form_class = BookingForm
    template_name = 'booking.html'
    success_url = reverse_lazy('booking')  # URL to redirect after successful form submission

    def form_valid(self, form):
        if form.is_valid():
            response = super().form_valid(form)
            messages.success(self.request, 'You booked successfully')
            return response  
        else:
            return messages.error(self.request, 'something went wrong')