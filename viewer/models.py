from django.db import models

from django.db.models import CharField, Model, ForeignKey, DO_NOTHING, IntegerField,  TextField, CASCADE

# Create your models here.


class City(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name

class Neighborhood(Model):
    name = CharField(max_length=128)
    city = models.ForeignKey(City, on_delete=CASCADE)

    def __str__(self):
        return self.name

class Street(Model):
    name = CharField(max_length=128)
    number = CharField(max_length=64)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=CASCADE)

    def __str__(self):
        return self.name

class Courier(Model):
    name = CharField(max_length=128)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=DO_NOTHING)

    def __str__(self):
        return self.name