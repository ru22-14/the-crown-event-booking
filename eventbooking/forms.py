from django import forms
from .models import Comment, Booking
from datetime import datetime, date, timedelta


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)



class BookingForm(forms.ModelForm):
    
    class Meta:
 
        model = Booking
        fields = ['event', 'guests', 'date', 'timeblock', 'menu', 'drinks','cake', 'theme', 'username']

        
        widgets = {
            'cake': forms.TextInput(attrs={'class': 'form-field col-2', 'type': 'text', 'placeholder': 'Yes, or no'}),
            'theme': forms.TextInput(attrs={'class': 'form-texinput col-4','placeholder': 'Please share what Theme you want for the Event e,g. Fairy Tale Theme, Unicorn Theme, Dinosaur Theme.'}),
            'date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'guests': forms.TextInput(attrs={'class': 'form-field col-3', 'type': 'text', 'placeholder': 'please choose between 15 and 50'}),
        }

    def get_free_dates(self):
        occupied_dates = Booking.objects.values_list('date', flat=True)

        today = date.today()
        last_date = today + timedelta(days=30)
        free_dates = [
            today + timedelta(days=n)
            for n in range((last_date - today).days)
        ]

        free_dates = [
            date for date in free_dates if date not in occupied_dates
        ]

        return free_dates  
