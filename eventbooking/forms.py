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
        
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

        def get_dates_available():
            dates_reserved = BookingForm.fields('date', flat=True)
            dates_reserved = list(itertools.chain(dates_reserved))
            return dates_reserved
        
