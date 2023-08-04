from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Event, Booking, Comment
from datetime import datetime, timedelta, date
from unittest import mock


class TestModels(TestCase):
    
    # set up test event, comment and booking
    @classmethod
    def setUpTestData(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='14682'
        )

        self.event = Event.objects.create(
            title='test event newyear',
            slug='test-event-slug-newyear',
            description='this is the test event newyear content',
            status=1
        )
      
        self.comment = Comment.objects.create(
            event=self.event,
            username=self.user,
            message='this is a comment for newyear event'
        )

        self.booking = Booking.objects.create(
            event=self.event,
            guests='40',
            date='2023-07-31',
            timeblock='20:00 PM - 00:00 AM',
            menu='chinese',
            drinks='cocktails',
            theme='romantic',
            cake='no',
            username=self.user,
            approved=False,
        )

    # test the __str__ method for Event
    def test_event_str(self):
        self.assertEqual(str(self.event), 'test event newyear')

    # test default values working as expected for Event status and image fields
    def test_event_defaults(self):
        self.assertEqual(self.event.status, 1)
        self.assertEqual(self.event.featured_image, 'placeholder')

    # test default values working as expected for Event date fields
    def test_event_dates_default(self):
        date = datetime(int(2023), int(7), 30)
        with mock.patch('django.utils.timezone.now',
                        mock.Mock(return_value=date)):
            event = Event.objects.create(
                                        title='test event new year',
                                        slug='test-event-slug-new_year',
                                        description='this is the test event new year content',
                                        status=1
            )
            self.assertEqual(event.created_on, date)
            self.assertEqual(event.updated_on, date) 

    # test the __str__ method for Comment
    def test_comment_str(self):
        self.assertEqual(
            str(self.comment),
            f'Comment this is a comment for newyear event by {self.user}')

    # test default value working as expected for Comment approved field
    def test_comment_approved_default(self):
        self.assertFalse(self.comment.approved)

    # test default values working as expected for Comment date field
    def test_comment_dates_default(self):
        date = datetime(int(2023), int(7), 30)
        with mock.patch('django.utils.timezone.now',
                        mock.Mock(return_value=date)):
            comment = Comment.objects.create(
                event=self.event,
                username=self.user,
                message='this is a date comment for  new year event'
            )
            self.assertEqual(comment.created_on, date) 

    # test the __str__ method for Booking   
    def test_booking_str(self):
        self.assertEqual(str(self.booking),
                         f'{str(self.event)} is booked by {self.user}')   

    # test default value working as expected for Booking approved field
    def test_booking_approved_default(self):
        self.assertFalse(self.booking.approved)