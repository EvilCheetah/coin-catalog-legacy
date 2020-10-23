from django.contrib import admin

# Register your models here.
from .models import(
    Region,
    Country,
    Category
)

admin.site.register(Region)
admin.site.register(Country)
admin.site.register(Category)
