from django import forms
from .models import Comment, Booking
from datetime import datetime, date, timedelta


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)



class BookingForm(forms.ModelForm):
    
    date = forms.DateField(widget=forms.DateInput(attrs={'id': 'datePicker', 'class': 'form-control', 'type': 'date'}))
    # timeblock = forms.ChoiceField(widget=forms.Select(
    #              attrs={'id': 'time', 'class': 'form-select', 'type' : 'text'}),
    #              choices=(("8:00 AM - 12:00 PM"), 
    #                       ("14:00 PM - 18:00 PM"), 
    #                       ("20:00 PM - 00:00 AM")))
    # event = forms.ChoiceField(widget=forms.Select(
    #              attrs={'id': 'event', 'class': 'form-select', 'type': 'text'}),
    #              choices=(("Birthday"), ("Anniversary"), ("Business Dinner"), ("Graduation Party"),
    #                       ("Eid Milan Party"), ("Party")))  
    # menu = forms.ChoiceField(widget=forms.Select(
    #              attrs={'id': 'menu', 'class': 'form-select', 'type': 'text'}),
    #              choices=(("Italien"), ("Chinese"), ("Oriental"), ("Indien"),
    #                       ("Snacks")))  
    # drinks = forms.ChoiceField(widget=forms.Select(
    #              attrs={'id': 'drinks', 'class': 'form-select', 'type': 'text'}),
    #              choices=(("Juices"), ("Shakes"), ("Smoothies"), ("Fizzy Drinks"),
    #                       ("Cocktails"), ("Mineral Water")))                                   
    
    class Meta:
 
        model = Booking
        fields = ['event', 'guests', 'date', 'timeblock', 'menu', 'drinks', 'theme', 'username']
        
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
