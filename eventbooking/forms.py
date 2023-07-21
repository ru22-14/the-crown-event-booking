from .models import Comment, Booking
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('event',)

        
