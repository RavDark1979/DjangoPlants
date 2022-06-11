from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .forms import PlantForm, PotForm, PlanForm, SupplierForm, LocationForm, SoilForm
from .models import Plant, Plan, Pot, Supplier, Soil, Location


# Create your views here.


def page(request):
    """main page view"""
    return render(request, 'main_page_form.html')

@login_required(redirect_field_name='login')
def all_plants(request):
    """view of all plants currently uploaded to a database"""
    plants = Plant.objects.all()
    return render(request, 'plant_list_form.html', {'plants': plants})

@login_required(redirect_field_name='login')
def all_plans(request):
    """view of all plans currently uploaded to a database"""
    plans = Plan.objects.all()
    return render(request, 'plan_list_form.html', {'plans': plans})

@login_required(redirect_field_name='login')
def all_suppliers(request):
    """view of all suppliers currently uploaded to a database"""
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_list_form.html', {'suppliers': suppliers})

def add_plant(request):
    """view of form for adding plants to a database"""
    form = PlantForm(request.POST or None, request.FILES or None)  # we accept the post or nothing
    if form.is_valid():
        form.save()

    return render(request, 'plant_form.html', {'form': form})


def edit_plant(request, id):
    """edit view for plants that are in a database"""
    plant = get_object_or_404(Plant, pk=id)
    form = PlantForm(request.POST or None, request.FILES or None, instance=plant)
    if form.is_valid():
        form.save()

    return render(request, 'plant_form.html', {'form': form})


def add_pot(request):
    """view of form for adding pots to a database"""
    form = PotForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'pot_form.html', {'form': form})


def edit_pot(request, id):
    """edit view for pots that are in a database"""
    pot = get_object_or_404(Pot, pk=id)
    form = PotForm(request.POST or None, request.FILES or None, instance=pot)
    if form.is_valid():
        form.save()

    return render(request, 'pot_form.html', {'form': form})


def add_soil(request):
    """view of form for adding soil to a database"""
    form = SoilForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'soil_form.html', {'form': form})


def edit_soil(request, id):
    """edit view for soil that is in a database"""
    soil = get_object_or_404(Soil, pk=id)
    form = SoilForm(request.POST or None, request.FILES or None, instance=soil)
    if form.is_valid():
        form.save()

    return render(request, 'soil_form.html', {'form': form})


def add_location(request):
    """view of form for adding locations to database"""
    form = LocationForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'location_form.html', {'form': form})


def edit_location(request, id):
    """edit view for locations that are in a database"""
    location = get_object_or_404(Location, pk=id)
    form = LocationForm(request.POST or None, request.FILES or None, instance=location)
    if form.is_valid():
        form.save()

    return render(request, 'location_form.html', {'form': form})


def add_supplier(request):
    """view of form for adding suppliers to database"""
    form = SupplierForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'supplier_form.html', {'form': form})


def edit_supplier(request, id):
    """edit view for suppliers that are in a database"""
    supplier = get_object_or_404(Supplier, pk=id)
    form = SupplierForm(request.POST or None, request.FILES or None, instance=supplier)
    if form.is_valid():
        form.save()

    return render(request, 'supplier_form.html', {'form': form})


def add_plan(request):
    """view of form for adding plans to database"""
    form = PlanForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'plan_form.html', {'form': form})


def edit_plan(request, id):
    """edit view for plans that are in a database"""
    plan = get_object_or_404(Plan, pk=id)
    form = PlanForm(request.POST or None, request.FILES or None, instance=plan)
    if form.is_valid():
        form.save()

    return render(request, 'plan_form.html', {'form': form})

