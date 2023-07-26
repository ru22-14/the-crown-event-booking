from django import forms
from .models import Comment, Booking
from datetime import datetime, date, timedelta


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)



class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    
    date = forms.DateField(widget=forms.DateInput(attrs={'id': 'datePicker', 'class': 'form-control', 'type': 'date'}))

    
    class Meta:
 
        model = Booking
        fields = ['event', 'date', 'timeblock', 'theme', 'menu', 'drinks', 'guests', 'username']
        
        widgets = {
            'date': DateInput(),
        }
