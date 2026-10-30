from datetime import timedelta
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status
from .models import MenuItem, Booking

User = get_user_model()

class MenuAPITests(APITestCase):
    def test_menu_list_and_create(self):
        MenuItem.objects.create(title="Bruschetta", price="8.50", inventory=12)
        response = self.client.get("/api/menu/items/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_anonymous_cannot_create_menu_item(self):
        response = self.client.post("/api/menu/items/", {"title": "Pasta", "price": "12.00", "inventory": 4})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class BookingAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="reviewer", password="TestPass123!")
        self.client.force_authenticate(self.user)

    def test_create_and_list_own_booking(self):
        response = self.client.post("/api/booking/tables/", {
            "name": "Reviewer", "no_of_guests": 2,
            "booking_date": (timezone.now() + timedelta(days=1)).isoformat()
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["user"], self.user.id)
        self.assertEqual(self.client.get("/api/booking/tables/").status_code, status.HTTP_200_OK)

    def test_guest_count_must_be_positive(self):
        response = self.client.post("/api/booking/tables/", {
            "name": "Reviewer", "no_of_guests": 0,
            "booking_date": (timezone.now() + timedelta(days=1)).isoformat()
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class RegistrationTests(APITestCase):
    def test_registration(self):
        response = self.client.post("/api/registration/", {
            "username": "newuser", "email": "new@example.com", "password": "StrongPass123!"
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="newuser").exists())
