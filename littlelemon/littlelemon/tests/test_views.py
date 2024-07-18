from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.ice_cream = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.choco_chips = Menu.objects.create(title="Chocolate chips", price=12, inventory=100)
    def test_getall(self):
        items = Menu.objects.all()
        # serialize data
        serialize_data = MenuSerializer(items, many=True)
        # Extract only the relevant fields from serialized data
        serialized_data = [ 
            {
                "title": item['title'],
                "price": item['price'],
                "inventory": item['inventory']
            } for item in serialize_data.data
        ]
        expected_serialized_data = [
            {
                "title": "IceCream",
                "price": "80.00",
                "inventory": 100
            },
             {
                "title": "Chocolate chips",
                "price": "12.00",
                "inventory": 100
            }
        ]
        # check serialazation with an assertion
        self.assertEqual(serialized_data, expected_serialized_data)
        # assert all items retrieval
        self.assertEqual(len(serialized_data), 2)

    def test_get_one(self):
        url = reverse('menu_detail', kwargs={'pk': self.ice_cream.pk})
        response = self.client.get(url)
        # Serialize the expected data
        expected_data = MenuSerializer(self.ice_cream).data
        # Check the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that the response data matches the expected data
        self.assertEqual(response.data, expected_data)
