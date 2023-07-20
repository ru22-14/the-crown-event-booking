from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic import TemplateView, CreateView
from .models import Event
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.contrib import messages
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


class EventReviews(generic.ListView):

    def get(self, request, slug, *args, **kwargs):

        queryset = Event.objects.filter(status=1)
        event = get_object_or_404(queryset, slug=slug)
        comments = event.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if event.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "events.html",
            {
                "event": event,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        ) 



   