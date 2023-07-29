from django.test import TestCase
from .forms import CommentForm, BookingForm
from datetime import date


class TestCommentForm(TestCase):

    # test that message value needs to be provided
    def test_message_is_required(self):
        form = CommentForm({'message': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')

    # test that message is named as an explicit field
    def test_fields_are_explicit_in_forms_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('message',))


class TestBookingForm(TestCase):

    def test_get_free_dates(self):
        form = BookingForm()
        free_dates = form.get_free_dates()
        self.assertIsInstance(free_dates, list)

        for date_option in free_dates:
            self.assertIsInstance(date_option, date) 
        
    def test_fields_are_explicit_in_forms_metaclass(self):
        form = BookingForm()
        self.assertEqual(form.Meta.fields, ['event', 'guests', 'date', 'timeblock', 'menu', 'drinks','cake', 'theme', 'username'])    
