from django.forms import ModelForm
from .models import Plan, Plant, Soil, Supplier, Location, Pot


class PlantForm(ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'price', 'location', 'created', 'updated', 'notes', 'difficulty', 'picture']


class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'description', 'created']


class SoilForm(ModelForm):
    class Meta:
        model = Soil
        fields = ['name', 'type', 'price']


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'sunlight']


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'address']


class PotForm(ModelForm):
    class Meta:
        model = Pot
        fields = ['type', 'price', 'radius', 'plant']
