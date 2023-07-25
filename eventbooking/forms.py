from django import forms
from .models import Comment, Booking
from datetime import datetime, date, timedelta


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)


class BookingForm(forms.ModelForm):
    
    # date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
 
        model = Booking
        fields = ['event', 'date', 'timeblock', 'theme', 'menu', 'drinks', 'guests',]
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }
    def get_free_dates(self, request):
        booked_dates = Booking.objects.values_list('date', flat=True)
        start_date = datetime.date.today()
        end_date = start_date + timedelta(days=60)
        free_dates = [start_date + timedelta(days=n)

                      for n in range(int((end_date - start_date).days))]

        free_dates = [
            date for dates in free_dates if date not in booked_dates
        ]

        return free_dates
        
