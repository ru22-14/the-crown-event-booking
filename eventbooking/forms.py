from django import forms
from django.forms import ModelForm
from .models import Booking
from datetime import date 


# create a booking form
class BookingForm(forms.ModelForm):
        
    date = forms.DateField(widget=forms.DateInput(attrs={
        'id': 'datePicker', 'class': 'form-control', 'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={
        'id': 'Time', 'class': 'form-control', 'type': 'time',
        'step': '3600'}))
    event = forms.ChoiceField(widget=forms.TextInput(attrs={
        'id': 'event', 'class': 'form-control', 'type': 'form-select',
        }))
    theme = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'theme', 'class': 'form-control', 'type': 'text', })),
    guest = forms.IntegerField(widget=forms.NumberInput(attrs={
        'id': 'guest', 'class': 'form-control', 'type': 'number', 
        }))

    menu = forms.ChoiceField(widget=forms.TextInput(attrs={
        'id': 'menu', 'class': 'form-control', 'type': 'form-select',
        }))

    drinks = forms.ChoiceField(widget=forms.TextInput(attrs={
        'id': 'drinks', 'class': 'form-control', 'type': 'form-select',
        }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'username', 'class': 'form-control','type': 'text', 
        }))

    useremail = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'useremail', 'class': 'form-control','type': 'email', 
        }))      

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].required = True
        self.fields['useremail'].required = True

    class Meta:
        model = Booking
        fields = '__all__' 



        
