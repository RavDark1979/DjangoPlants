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
    edit_pot, edit_soil, edit_plan, edit_location, edit_supplier

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', page, name='mainpage'),
    path('', auth_views.LoginView.as_view()),
    path('logout/', auth_views.LoginView.as_view()),
    path('plants/', all_plants),
    path('plans/', all_plans),
    path('add_plant/', add_plant),
    path('edit_plant/<int:id>/', edit_plant),
    path('add_pot/', add_pot),
    path('edit_pot/<int:id>/', edit_pot),
    path('add_supplier/', add_supplier),
    path('edit_supplier/<int:id>/', edit_supplier),
    path('add_plan/', add_plan),
    path('edit_plan/<int:id>/', edit_plan),
    path('add_location/', add_location),
    path('edit_location/<int:id>/', edit_location),
    path('add_soil/', add_soil),
    path('edit_soil/<int:id>/', edit_soil),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
