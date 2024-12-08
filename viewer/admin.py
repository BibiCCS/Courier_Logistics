from django.contrib import admin

from viewer.models import City, Neighborhood, Street, Courier

# Register your models here.

admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Street)
admin.site.register(Courier)