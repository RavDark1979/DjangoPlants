"""plants URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from magdziungla.views import page, all_plants, all_plans, add_plant, \
    add_pot, add_plan, add_soil, add_location, add_supplier, edit_plant,\
    edit_pot, edit_soil, edit_plan, edit_location, edit_supplier, all_suppliers, hunt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page, name='mainpage'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('plants/', all_plants, name='plant_list'),
    path('plans/', all_plans, name='plan_list'),
    path('suppliers/', all_suppliers, name='supplier_list'),
    path('add_plant/', add_plant, name='add_plant'),
    path('edit_plant/<int:id>/', edit_plant, name='edit_plant'),
    path('add_pot/', add_pot, name='add_pot'),
    path('edit_pot/<int:id>/', edit_pot, name='edit_pot'),
    path('add_supplier/', add_supplier, name='add_supplier'),
    path('edit_supplier/<int:id>/', edit_supplier, name='edit_supplier'),
    path('add_plan/', add_plan, name='add_plan'),
    path('edit_plan/<int:id>/', edit_plan, name='edit_plan'),
    path('add_location/', add_location, name='add_location'),
    path('edit_location/<int:id>/', edit_location, name='edit_location'),
    path('add_soil/', add_soil, name='add_soil'),
    path('edit_soil/<int:id>/', edit_soil, name='edit_soil'),
    path('add_location/hunt.html', hunt),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
