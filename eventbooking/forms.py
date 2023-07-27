from django import forms
from .models import Comment, Booking
from datetime import datetime, date, timedelta


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)



class BookingForm(forms.ModelForm):
    
    date = forms.DateField(widget=forms.DateInput(attrs={'id': 'datePicker', 'class': 'form-control', 'type': 'date'}))                                  
    
    class Meta:
 
        model = Booking
        fields = ['event', 'guests', 'date', 'timeblock', 'menu', 'drinks','cake', 'theme', 'username']
        widgets = {
            'cake': forms.TextInput(attrs={'class': 'form-field', 'type': 'text', 'placeholder': 'Yes, or no'}),
            'theme': forms.TextInput(attrs={'class': 'form-text','placeholder': 'Please share what Theme you want for the Event e,g. Fairy Tale Theme, Unicorn Theme, Dinosaur Theme.'}),
        }
        
class DateBookingForm(forms.ModelForm):
    """
    Form for the BookingQuery Model
    It is used for filtering the bookings in admin manage booking page
    """
    date = forms.DateField(widget=forms.DateInput(
        attrs={'id': 'datePicker', 'class': 'form-control',
               'type': 'date'}),
                           initial=date.today())

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['date'].required = False
        self.fields['date'].label = "Filter By Date:"
        self.fields['date'].initial = date.today()

    class Meta:
        """Meta class"""
        model = Booking
        fields = ['date']
