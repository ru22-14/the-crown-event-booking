from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import (
    EventPageView,
    EventListView,
    EventBookingView,
    EventDetailView,
    MyBookingView,
    UpdateBookingView,
    DeleteBookingView,
)


class TestUrls(SimpleTestCase):
    def test_EventPageView_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, EventPageView)

    def test_EventListView_url(self):
        url = reverse('events')
        self.assertEqual(resolve(url).func.view_class, EventListView)

    def test_EventBookingView_url(self):
        url = reverse('booking')
        self.assertEqual(resolve(url).func.view_class, EventBookingView)  

    def test_MyBookingView_url(self):
        url = reverse('mybooking')
        self.assertEqual(resolve(url).func.view_class, MyBookingView)       

    def test_UpdateBookingView_url(self):
        booking_id = 1
        url = reverse('update_booking', args=[booking_id])
        self.assertEqual(resolve(url).func.view_class, UpdateBookingView)

    def test_DeleteBookingView_url(self):
        booking_id = 1
        url = reverse('delete_booking', args=[booking_id])
        self.assertEqual(resolve(url).func.view_class, DeleteBookingView)    


