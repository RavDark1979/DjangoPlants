from django.db import models


# Create your models here.
#    Lokacje done
#    Rośliny (relacja jeden do wiele z lokacją) done
#    Donice (jeden do jeden z rośliną?)
#    Ziemia/podłoże (typ? wiele do wiele z rośliną?)
#    Dostawca (gdzie roślina była kupiona) - wiele do wiele z rośliną?

class Location(models.Model):
    """
    - name (living room, baclony, terrace, ect.)
    - sunlight level (high, medium, low)
    """
    name = models.CharField(max_length=120)
    sunlight = models.CharField(max_length=10)


class Plant(models.Model):
    """
    - name: plant name,
    - price: purchase cost,
    - location: relation one-to-many with location
    - created: when the plant arrived
    - updated: last date when the plant was watered, fertilized, ect.
    - difficulty: liczba głosów na przepis (domyślnie 0)
    - picture: graphical representation
    - notes: additional info about a plant (special care, sun requirements, ect)
    """
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=False)
    updated = models.DateTimeField(blank=True)
    preparation_time = models.IntegerField()
    difficulty = models.IntegerField(default=0)
    picture = models.ImageField(upload_to="pictures", null=True, blank=True)
    notes = models.CharField(max_length=1500)


class Pot(models.Model):
    """
    - type: plastic, stone, ect.
    - price: purchase cost,
    - capacity (in litres)
    """
    type = models.CharField(max_length=20)
    price = models.PositiveIntegerField
    capacity = models.SmallIntegerField


class Soil(models.Model):
    """
    - type relation many-to-many with Plant,
    - price: purchase cost,
    """

    type = models.ManyToManyField(Plant)
    price = models.PositiveIntegerField


class Supplier(models.Model):
    """
    - name (shop, garden centre, ect.)
    - address
    - relaction many to many with plant, soil, pot
    """
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    plant = models.ManyToManyField(Plant)
    pot = models.ManyToManyField(Pot)
    soil = models.ManyToManyField(Soil)

# class RecipePlan(models.Model):
#     """
#     - meal_name: nazwa posiłku (śniadanie, obiad itp),
#     - recipe: relacja do tabeli przepisów
#     - plan: relacja do tabeli planów
#     - order: kolejność posiłków w planie,
#     - day_name: "from .enums import DayName"
#     """
#     meal_name = models.CharField(max_length=255)
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
#     order = models.IntegerField()
#     day_name = models.CharField(max_length=16, choices=DayName.choices())
#
# class Page(models.Model):
#     """
#     - title: tytuł strony,
#     - description: treść strony,
#     - slug: unikalny identyfikator tworzony na podstawie tytułu
#     """
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     slug = models.SlugField(unique=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.title)
#         super(Page, self).save(*args, **kwargs)
