from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Event, Booking, Comment
from .forms import CommentForm, BookingForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import date
import datetime


class EventPageView(TemplateView):
    """
    event overview 
    """
    model = Event
    template_name = 'index.html'


class EventListView(generic.ListView, View):
    """
    Retrieve the event list and set pagination
    """
    model = Event
    queryset = Event.objects.filter(status=1).order_by('-created_on')
    template_name = 'events.html'
    paginate_by = 6


class EventDetailView(View):  
    """
    Display Event Details for selected event

    get method : retrieve event details including comments and likes
    and render event detail page

    post method : validate comment input, store and re-load detail page
    """
    template_name = 'events_detail'
    model = Event

    def get(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        comments = event.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if event.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "events_detail.html",
            {
                "event": event,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        comments = event.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if event.likes.filter(id=self.request.user.id).exists():
            liked = True
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.useremail = request.user.email
            comment_form.instance.username = request.user.username
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.save()
            messages.success(request, 'Thank You For your Review!')
            return HttpResponseRedirect(reverse('events_detail', args=[slug]))
        else:
            comment_form = CommentForm()
    

class EventLikeView(View):
    """
    Allow user to like/unlike the selected event

    post method : toggle 'like' setting for event for this user
    """
    
    def post(self, request, slug):
        event = get_object_or_404(Event, slug=slug)
        if event.likes.filter(id=request.user.id).exists():
            event.likes.remove(request.user)
        else:
            event.likes.add(request.user)
        return HttpResponseRedirect(reverse('events_detail', args=[slug]))


class EventBookingView(TemplateView, View):
    """
    Display booking form for current user

    get method : retrieve all the data (if valid) entered by the user in order to book an event 

    post method : validate input provided by the user, re-load if input is not correct, redirects event.html
    if input is valid and correct
    """

    template_name = 'booking.html'
    form = BookingForm()
    date = date.today()
    time = Booking.TIME_CHOICE[0]
    booking_capacity_per_day = 3
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookingForm
        return context

    def post(self, request):
        min_guests = 15
        max_guests = 50
        booking_capacity_per_day = 3
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                event_booking = form.save(commit=False)
                if event_booking.date < date.today():
                    messages.error(request,
                                   "Booking in the past date is not allowed!")
                    return redirect('booking')                
                booked_events = (Booking.objects.filter(date=event_booking.
                                                        date, timeblock=event_booking.timeblock).count())
                if event_booking.guests < min_guests:
                    messages.error(request, 'minimum no. of guests are 15')
                    return redirect('booking')
                if event_booking.guests > max_guests:
                    messages.error(request, 'maximum no. of guests are 50') 
                    return redirect('booking')   
                if booked_events >= booking_capacity_per_day:
                    messages.error(request, "Sorry no more bookings are possible today!")
                    return redirect('booking')
                context = {
                   'form': form
                }   
                event_booking.username = request.user
                event_booking.save()
                request.session['booking_id'] = event_booking.id
                messages.success(request, 'Event Booking request is proposed successfully. Your booking is awaiting for approval now.')
                return render(request, 'events.html')
            else:
                messages.error(request, 'There is some problem submitting your booking.')
                return render(request, 'booking.html')
                context = {
                   'form': form
                }
                return render(request, 'booking.html', context)     
        else:
            form = BookingForm(request.GET)
        return render(request, 'booking.html',
                      {'form': form})  


class MyBookingView(View):
    """
    Display booking information for current user

    get method : retrieve past and upcoming bookings for user
                 and render my bookings page
    """
    model = Booking
    template_name = 'mybooking.html'

    def get(self, request):
        booking_list = (Booking.objects.all())
        if request.user.is_authenticated:
            previous_bookings = (Booking.objects.filter(username=request.user).order_by('event'))
            context = {
                'previous_bookings': previous_bookings,
            }
            return render(request, 'mybooking.html', context)


class UpdateBookingView(UpdateView):
    """
    Display booked event data for current user

    get method : retrieve data if valid

    post method : update selected booking
    """

    template_name = 'update_booking.html' 
    date = date.today()
    
    def get(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id, username=request.user)
        form = BookingForm(instance=booking)
        context = {
            'form': form,
        }
        return render(request, 'update_booking.html', context) 

    def post(self, request, booking_id):
        booking_capacity_per_day = 3 
        booking = get_object_or_404(Booking, id=booking_id, username=request.user)
        form = BookingForm(request.POST, instance=booking)

        if form.is_valid():
            event_booking = form.save(commit=False)
            if event_booking.date < date.today():
                messages.error(request, "Booking in the past date is not allowed!")
            booked_events = (Booking.objects.filter(date=event_booking.date, 
                                                    timeblock=event_booking.timeblock).exclude(id=booking_id).count())
            if booked_events >= booking_capacity_per_day:
                messages.error(request, "Sorry no more bookings are possible today!") 
                return redirect('booking')
            context = {
                'form': form
                }
            event_booking.user = request.user
            event_booking.approved = False
            event_booking.save()
            request.session['booking_id'] = event_booking.id
            messages.success(request, 'Your booking is updated successfully and is waiting for approval now.')
            return render(request, 'events.html') 

        else:
            messages.error(request, 'There is some problem submitting your booking.') 
            return render(request, 'booking.html')         
        context = {
            'form': form,
        }
        return render(request, 'update_booking.html', context)
    

class DeleteBookingView(DeleteView):
    """
       cancel selected booking and redirects to mybooking
    """

    template_name = 'delete_booking.html'

    def get(self, request, booking_id):

        booking = get_object_or_404(Booking, id=booking_id, username=request.user)
        context = {
            'booking': booking
        }
        return render(request, 'delete_booking.html', context)

    def post(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id, username=request.user)
        booking.delete()
        messages.success(request, 'Your booking has been cancelled')
        return HttpResponseRedirect(reverse('mybooking'))