from django import forms
from .models import Comment, Booking
from datetime import datetime, date, timedelta


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)


class BookingForm(forms.ModelForm):
    
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    timeblock = forms.ChoiceField(widget=forms.Select(
                 attrs={'class': 'form-select'}),
                 choices=(
                       (1, '08:00 AM - 12:00 PM'),
                       (2, '14:00 PM - 18:00 PM'),
                       (3, '20:00 PM - 00:00 AM'),
                 ))
    
    class Meta:
 
        model = Booking
        fields = ['event', 'date', 'timeblock', 'theme', 'menu', 'drinks', 'guests', 'username',]

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
        
