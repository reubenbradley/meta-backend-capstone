from django.test import TestCase
from restaurant.models import MenuItem

# TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

