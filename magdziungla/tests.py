from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import add_plant, add_pot, add_soil, add_plan, add_supplier, add_location
from .models import Plant, Plan, Pot, Soil,Supplier, Location

# Create your tests here.


class MagdziunglaTests(TestCase):

    """url "add" functionality testing for Magdziungla app"""

    def test_url_add_plant(self):
        url = reverse(add_plant)
        self.assertEquals(resolve(url).func, add_plant)

    def test_url_add_pot(self):
        url = reverse(add_pot)
        self.assertEquals(resolve(url).func, add_pot)

    def test_url_add_soil(self):
        url = reverse(add_soil)
        self.assertEquals(resolve(url).func, add_soil)

    def test_url_add_plan(self):
        url = reverse(add_plan)
        self.assertEqual(resolve(url).func, add_plan)

    def test_url_add_supplier(self):
        url = reverse(add_supplier)
        self.assertEquals(resolve(url).func, add_supplier)

    def test_url_add_location(self):
        url = reverse(add_location)
        self.assertEquals(resolve(url).func, add_location)

    """main views, add/edit views and templates tests for Magdziungla app"""

    def test_view_main_page(self):
        client = Client()
        response = client.get(reverse('main_page'))
        self.assertEquals(response.status_code, 200)

    """view requires login - check if redirect works"""

    def test_view_all_plants(self):
        client = Client()
        response = client.get(reverse('plant_list'))
        self.assertEquals(response.status_code, 302)

    """view requires login - check if redirect works"""

    def test_view_all_plan(self):
        client = Client()
        response = client.get(reverse('plan_list'))
        self.assertEquals(response.status_code, 302)

    """view requires login - check if redirect works"""

    def test_view_all_supplier(self):
        client = Client()
        response = client.get(reverse('supplier_list'))
        self.assertEquals(response.status_code, 302)

    def test_view_add_plant(self):
        client = Client()
        response = client.get(reverse('add_plant'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'plant_form.html')

    def test_view_add_pot(self):
        client = Client()
        response = client.get(reverse('add_pot'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pot_form.html')

    def test_view_add_soil(self):
        client = Client()
        response = client.get(reverse('add_soil'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'soil_form.html')

    def test_view_add_plan(self):
        client = Client()
        response = client.get(reverse('add_plan'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'plan_form.html')

    def test_view_add_supplier(self):
        client = Client()
        response = client.get(reverse('add_supplier'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'supplier_form.html')




