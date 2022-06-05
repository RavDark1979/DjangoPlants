from django.db import models


# Create your models here.
#    Lokacje done
#    Rośliny (relacja jeden do wiele z lokacją) done
#    Donice (jeden do jeden z rośliną?) done
#    Ziemia/podłoże (typ? wiele do wiele z rośliną?) done
#    Dostawca (gdzie roślina była kupiona) - wiele do wiele z rośliną? done

class Location(models.Model):
    """
    - name (living room, baclony, terrace, ect.)
    - sunlight level (high, medium, low)
    """
    name = models.CharField(max_length=120)
    sunlight = models.CharField(max_length=64)

    def __str__(self):
        return self.name_and_sunlight()

    def name_and_sunlight(self):
        return "name: {}, sunlight level: {}".format(self.name, self.sunlight)


class Plant(models.Model):
    """
    - name: plant name,
    - price: purchase cost,
    - location: relation one-to-many with location
    - created: when the plant arrived to your home
    - updated: last date when the plant was watered, fertilized, ect.
    - difficulty: liczba głosów na przepis (domyślnie 0)
    - picture: graphical representation
    - notes: additional info about a plant (special care, sun requirements, ect)
    """
    objects = None
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    created = models.DateField(blank=True, null=True)
    updated = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=1500)
    difficulty = models.IntegerField(default=0)
    picture = models.ImageField(upload_to="pictures", null=True, blank=True)

    def __str__(self):
        return self.name_and_location()

    def name_and_location(self):
        return "name: {}, location: {}".format(self.name, self.location)


class Pot(models.Model):
    """
    - type: plastic, stone, ect.
    - price: purchase cost,
    - radius (in cm)
    - plant: relation one to one with pot
    """
    type = models.CharField(max_length=20)
    price = models.PositiveIntegerField(null=True)
    radius = models.IntegerField(blank=True, null=True)
    plant = models.OneToOneField(Plant, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.type_and_radius()

    def type_and_radius(self):
        return "type: {}, radius: {}".format(self.type, self.radius)


class Soil(models.Model):
    """
    - name: name of the soil
    - type relation many-to-many with Plant,
    - price: purchase cost,
    """
    name = models.CharField(max_length=100, null=True)
    type = models.ManyToManyField(Plant)
    price = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name_and_type()

    def name_and_type(self):
        return "name: {}, type: {}".format(self.name, self.type)


class Supplier(models.Model):
    """
    - name (shop, garden centre, ect.)
    - address
    - relaction many to many with plant, soil, pot
    """
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    plant = models.ManyToManyField(Plant, blank=True)
    pot = models.ManyToManyField(Pot, blank=True)
    soil = models.ManyToManyField(Soil, blank=True)

    def __str__(self):
        return self.name_and_address()

    def name_and_address(self):
        return "name: {}, address: {}".format(self.name, self.address)


class Plan(models.Model):
    """
        - name (watering, ferilizing, cleaning)
        - description: detail work in this place
        - created - date of creation
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name_and_created()

    def name_and_created(self):
        return "name:{}, created: {}".format(self.name, self.created)
