from django.shortcuts import render

from .forms import PlantForm, PotForm, PlanForm, SupplierForm, LocationForm, SoilForm
from .models import Plant, Plan


# Create your views here.

def page(request):
    return render(request, 'main_page.html')


def all_plants(request):
    plants = Plant.objects.all()
    return render(request, 'plant_list.html', {'plants': plants})


def all_plans(request):
    plans = Plan.objects.all()
    return render(request, 'plan_list.html', {'plans': plans})


def add_plant(request):
    form = PlantForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    return render(request, 'add_plant.html', {'form': form})


def add_pot(request):
    form = PotForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'add_pot.html', {'form': form})


def add_soil(request):
    form = SoilForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'add_soil.html', {'form': form})


def add_location(request):
    form = LocationForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'add_location.html', {'form': form})


def add_supplier(request):
    form = SupplierForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'add_supplier.html', {'form': form})


def add_plan(request):
    form = PlanForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request, 'add_plan.html', {'form': form})
