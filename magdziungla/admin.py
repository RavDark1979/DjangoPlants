from django.contrib import admin
from .models import (Location, Plant, Pot, Soil, Supplier, Plan)
# Register your models here.

admin.site.register(Location)
admin.site.register(Plant)
admin.site.register(Pot)
admin.site.register(Soil)
admin.site.register(Supplier)
admin.site.register(Plan)
