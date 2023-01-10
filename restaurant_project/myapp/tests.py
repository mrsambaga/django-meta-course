from django.test import TestCase
from .models import *
from datetime import datetime

# Create your tests here.
class BookingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.booking = Booking.objects.create(
            first_name = "John",
            last_name = "Mac Tavish",
            guest_count = 3,
            comment = "please add a baby chair"
        )

    def test_fields(self):
        self.assertIsInstance(self.booking.first_name, str)
        self.assertIsInstance(self.booking.last_name, str)
        self.assertIsInstance(self.booking.guest_count, int)
        self.assertIsInstance(self.booking.comment, str)
    
    #def test_timestamps(self):
    #    self.assertIsInstance(self.booking.reservation_time, datetime)