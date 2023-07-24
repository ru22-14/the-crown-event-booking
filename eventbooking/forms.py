from django import forms
from .models import Comment, Booking
from datetime import datetime


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)


class BookingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={
       'class': 'form-control', 'type': 'date'}))
    
    class Meta:

        model = Booking
        fields = ['event', 'theme', 'menu', 'drinks', 'guests', 'username', 'useremail']
        



        
