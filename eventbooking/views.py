from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Event, Booking, Comment
from .forms import CommentForm, BookingForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import  date
import datetime


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
            comment_form.instance.name = request.user.username
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
    
    # def get(self, request):
        
    #     form = BookingForm()
        
    #     context = {
    #         'form': form

            
    #     }
    #     return render(request, 'booking.html', context)
   
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['form'] = BookingForm
        # context['bookings'] = self.request.booking.objects.all()
        return context


    def post(self, request):
        if request.method == 'POST':

            form = BookingForm(request.POST)
            if form.is_valid():
               
                    
                
                form.save()
                messages.success(request, 'Event Booking request is proposed successfully. Your booking is awaiting for approval now.')
                return render(request, 'mybooking.html') 

                  
            else:
                messages.error(request, 'There is some problem submitting your booking.') 
                return render(request, 'booking.html')         
        else:
            form = BookingForm(request.GET)
        return render(request, 'booking.html',
                      {'form': form, })  


class BookingEdit(UpdateView):

    model = Booking
    template_name = 'edit_booking.html'
    fields = ['event', 'guests', 'menu', 'drinks', 'theme',] 
    success_url = '/mybookings' 
   
    def get_queryset(self):
        return self.request.user.booking_set.all()

class BookingDelete(DeleteView):
    model = Booking
    template_name = 'delete_booking.html'
    success_url ='/' 

    def get_queryset(self):
      return self.request.user.booking_set.all()        
                    

        
       
class MyBookingView(View):
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

        else:
            messages.error(
                request,
                'You need to log in to view your bookings.'
            )
            return redirect('login')
        context = {
            'booking_list': booking_list
        }    

class EditBookingView(View):
    template_name = 'edit_booking.html'            
    model = Booking

    # def get_free_time_blocks(self, date):
    #     """
    #     Specification of of possible booking times for each day.
    #     """

    #     free_blocks = []

    #     for choice, _ in OnlineBooking.BOOKING_CHOICES:
    #         time = choice
    #         booked_events = (
    #             Booking.objects.filter(date=date, time=time).count()
    #         )
    #         remaining_blocks = self.total_timeblock - booked_timeblock
    #         if remaining_blocks > 0:
    #             free_blocks.append((time, remaining_blocks))

    #     return free_blocks

    # def get(self, request, *args, **kwargs):
    #     """
    #     Specification of the data entered into the form.
    #     """
    #     current_date = datetime.now().date
    #     form = BookingForm()
    #     free_blocks = []

    #     for choice, _ in OnlineBooking.BOOKING_CHOICES:
    #         time = choice[1]
    #         booked_events = (
    #             Booking.objects.filter(date=current_date, time=time).count()
    #         )
    #         remaining_blocks = self.total_timeblock - booked_timeblock
    #         if remaining_blocks > 0:
    #             free_blocks.append((time, remaining_blocks))

       
    #     context = {
    #             'booking': booking,
    #             'free_blocks': free_blocks,
    #             }
        
    #     return render(request, 'edit_booking.html', context)

    # def post(self, request, *args, **kwargs):
        # booking = get_object_or_404(Booking, id=id, username=request.user)
        
        # if request.method == 'POST':

        #     form = BookingForm(request.POST, instance=booking)
        #     if form.is_valid():

        #         booking.user = request.user
        #         booking.approved = False
        #         form.save()
        #         request.session['booking_id'] = booking.id
        #         messages.success(
        #             request, 'Your booking was successfully updated')
        #         return redirect('mybooking')        
        #     else:

        #         messages.error(
        #             request, 'There was a problem submiting your booking.'
        #                      ' Please try again!')
        #         context = {
        #             'form': form
        #         }             
        #         return render(reverse, 'edit_booking.html', context)
         
       
    