from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.views.generic import TemplateView, CreateView
from .models import Event, Booking, Comment
from .forms import CommentForm, BookingForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import datetime, date


# Create your views here.

class EventPageView(TemplateView):
    """
    events overview and pagination
    """
    model = Event
    template_name = 'index.html'
    
    
class EventListView(generic.ListView, View):
    model = Event
    queryset = Event.objects.filter(status=1).order_by('-created_on')
    template_name = 'events.html'
    paginate_by = 6


class EventDetailView(View):  
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
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.name
            comment = comment_form.save(commit=False)
            comment.event = event
           
            comment.save()
            messages.success(request, 'Thank You For your Review!')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "events_detail.html",
            {
                "event": event,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )    


class EventLikeView(View):
    
    def post(self, request, slug):
        event = get_object_or_404(Event, slug=slug)

        if event.likes.filter(id=request.user.id).exists():
            event.likes.remove(request.user)
        else:
            event.likes.add(request.user)

        return HttpResponseRedirect(reverse('events_detail', args=[slug]))


class EventBookingView(TemplateView, View):

    template_name = 'booking.html'
    form = BookingForm()

    def get(self, request):
        
        form = BookingForm()

        context = {
            'form': form,
        }
        return render(request, 'booking.html', context)

    def post(self, request):
       
        if request.method == 'POST':

            form = BookingForm(request.POST)
            if form.is_valid():

                form.save()
                messages.success(
                    request, 'Your booking was successfully registered')
                return redirect('mybooking')        
            else:

                messages.error(
                    request, 'There was a problem submiting your booking.'
                             ' Please try again!')
                return HttpResponseRedirect(reverse('booking'))
         
        form = BookingForm()
        context = {
            'form': form
        }


class MyBookingView(View):
    template_name = 'mybooking.html'

    def get(self, request):
        if request.user.is_authenticated:
            booking = (Booking.objects.filter(username=self.request.user).order_by('date'))
            context = {
                'booking': booking
                }
            return render(request, 'mybooking.html', context)
