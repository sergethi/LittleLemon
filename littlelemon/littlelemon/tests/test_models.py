from django.test import TestCase
from restaurant.models import Menu, Booking
from django.utils import timezone

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class BookingTest(TestCase):
    def test_get_booking(self):
        date = timezone.now()
        booking = Booking.objects.create(name="Jessica", no_of_guests=5, booking_date=date)
        self.assertEqual(str(booking), "Jessica")