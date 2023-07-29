from django.test import TestCase, Client
from .models import Event, Booking, Comment
from django.contrib.auth.models import User
from datetime import datetime, date
from .views import (
    EventListView,
    MyBookingView,
    EventBookingView,
    UpdateBookingView,
    DeleteBookingView,
)


class TestViews(TestCase):
    
    @classmethod
    def setUpTestData(self):
        self.client = Client()
        # self.user = User.objects.create_user(
        #     username='rumaissa',
        #     password='1482'
        # )

        self.event = Event.objects.create(
            title='test event party',
            slug='test-event-slug-party',
            description='this is the test event datenight content',
            status=1
        )
        self.comment = Comment.objects.create(
            event=self.event,
            username=self.user,
            message='this is a comment for event party'
        )

        self.booking = Booking.objects.create(

            username=self.user,
            event='Eid Party',
            guests=40,
            date='July 31, 2023',
            time='10 AM - 12 AM',
            menu='oriental',
            drinks='juices',
            theme='oriental',
            cake='no',
            approved=False,
        )

    def test_get_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'index.html')
        


        
        
    

       