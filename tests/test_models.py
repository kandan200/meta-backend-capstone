from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def testItem(self):
        item = Menu.objects.create(Title='IceCream', Price=50, Inventory=10)
        self.assertEqual(str(item), 'IceCream : 50')