from django.test import TestCase, Client
from django.urls import reverse
from .models import Event, Booking, Comment
from django.contrib.auth.models import User
from datetime import datetime, date


class TestViews(TestCase):
# set up test event, comment and booking
    @classmethod
    def setUpTestData(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='14682'
        )
        self.event = Event.objects.create(
            title='test event partynight',
            slug='test-event-slug-partynight',
            description='this is the test event partynight content',
            status=1
        )
        self.comment = Comment.objects.create(
            event=self.event,
            username=self.user,
            message='this is a comment for partynight event.'
        )
        self.booking = Booking.objects.create(
            event=self.event,
            guests='40',
            date='2023-07-31',
            timeblock='20:00 PM - 00:00 AM',
            menu='chinese',
            drinks='cocktails',
            theme='disco',
            cake='no',
            username=self.user,
            approved=False,
        )
    # retrieve home page and check correct templates are used
    def test_get_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'index.html')

    # retrieve event detail page and check correct templates are used
    def test_get_events_detail_page(self):
        response = self.client.get(
            reverse('events_detail', args=[self.event.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'events_detail.html') 

    # retrieve booking page and check correct templates are used
    def test_get_mybooking_page(self):
        self.client.login(username='testuser', password='14682')
        response = self.client.get(reverse('mybooking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'mybooking.html')

    # verify like can be toggled on and off
    def test_get_toggle_like_events(self):
        self.client.login(username='testuser', password='14682')
        likesnum = self.event.likes.count()
        response = self.client.post(
            reverse('event_like', args=[self.event.slug]))
        self.assertRedirects(
            response, reverse('events_detail', args=[self.event.slug]))
        self.assertEqual(self.event.likes.count(), likesnum+1)
        response = self.client.post(
            reverse('event_like', args=[self.event.slug]))
        self.assertRedirects(
            response, reverse('events_detail', args=[self.event.slug]))
        self.assertEqual(self.event.likes.count(), likesnum)

    # verify that user can comment on event and page is refreshed
    def test_comments_on_events(self):
        self.client.login(username='testuser', password='14682')
        response = self.client.get(
            reverse('events_detail', args=[self.event.slug]),
            data={'message': 'test comment'})
        self.assertEqual(response.status_code, 200)  

    # verify that user can book an event 
    def test_get_booking_event(self):
        self.client.login(username='testuser', password='14682')
        response = self.client.post(
            reverse('booking'), data={
                'event': self.event,
                'guests': '40',
                'date': '2023-07-31',
                'timeblock': '8:00 PM - 00:00 AM',
                'menu': 'chinese',
                'drinks': 'cocktails',
                'theme': 'disco',
                'cake': 'no',
                'username': self.user
            })
        self.assertEqual(response.status_code, 200)

    # verify user can update booking
    def test_get_update_booking_view(self):
        self.client.login(username='testuser', password='14682')
        response = self.client.get(
            reverse('update_booking', args=[self.booking.id])
        )
        self.assertEqual(response.status_code, 200)  

    def test_post_update_booking(self):
        self.client.login(username='testuser', password='14682')
        response = self.client.post(
            reverse('update_booking', args=[self.booking.id]),
            data={
                'event': self.event,
                'guests': '40',
                'date': '2023-07-31',
                'timeblock': '8:00 PM - 00:00 AM',
                'menu': 'chinese',
                'drinks': 'cocktails',
                'theme': 'disco',
                'cake': 'no',
                'username': self.user
            })

        self.assertEqual(response.status_code, 200)

    # verify user can cancel booking
    def test_delete_booking(self):
        self.client.login(username='testuser', password='14682')
        booking = Booking.objects.create(
            event=self.event,
            guests='40',
            date='2023-7-31',
            timeblock='20:00 PM - 00:00 AM',
            menu='chinese',
            drinks='cocktails',
            theme='disco',
            cake='no',
            username=self.user,
            approved=False
        )
        existing_bookings = Booking.objects.filter(id=booking.id)
        self.assertEqual(len(existing_bookings), 1)
        response = self.client.post(
            reverse('delete_booking', args=[self.booking.id]))
        self.assertEqual(response.status_code, 200)
        existing_bookings = Booking.objects.filter(id=booking.id)
        self.assertEqual(len(existing_bookings), 0)