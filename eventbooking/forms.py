from django import forms
from .models import Comment, Booking



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['event', 'time', 'theme', 'menu', 'drinks', 'guests', 'username', 'useremail']

        
