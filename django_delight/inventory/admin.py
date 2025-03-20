from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Ingredient)
admin.site.register(models.MenuItem)
admin.site.register(models.RecipeRequirements)
admin.site.register(models.Purchases)