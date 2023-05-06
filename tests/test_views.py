from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title='rice', Price=20.3, Inventory=50)
        Menu.objects.create(Title='beans', Price=12.5, Inventory=5)
        Menu.objects.create(Title='potatoes', Price=500, Inventory=4)
        
    def test_getall(self):
        rice = Menu.objects.get(Title='rice')
        beans = Menu.objects.get(Title='beans')
        potatoes = Menu.objects.get(Title='potatoes')
        riice = MenuSerializer(data=rice)
        beeans = MenuSerializer(data=beans)
        pott = MenuSerializer(data=potatoes)
        self.assertEqual(str(riice.initial_data.Title), 'rice')
        self.assertEqual(str(beeans.initial_data.Title), 'beans')
        self.assertEqual(str(pott.initial_data.Title), 'potatoes')