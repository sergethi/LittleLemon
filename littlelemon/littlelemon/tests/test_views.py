from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Chocolate chips", price=12, inventory=100)
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