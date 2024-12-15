from django.db import models

from django.db.models import CharField, Model, ForeignKey, DO_NOTHING, IntegerField,  TextField, CASCADE

# Create your models here.


class Microzones(Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class County(Model):
    name = models.CharField(max_length=128)
    microzones = models.ForeignKey(Microzones, on_delete=DO_NOTHING, related_name='microzones', blank=True, null=True)

    def __str__(self):
        return self.name

class City(Model):
    name = CharField(max_length=128)
    county = models.ForeignKey(County, on_delete=CASCADE, related_name='cities')


    def __str__(self):
        return self.name

class Neighborhood(Model):
    name = CharField(max_length=128)
    city = models.ForeignKey(City, on_delete=CASCADE,  related_name='neighborhoods')

    def __str__(self):
        return self.name

class Street(Model):
    name = CharField(max_length=128)
    number = CharField(max_length=64)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=CASCADE, related_name='streets')

    def __str__(self):
        return self.name

class Courier(Model):
    name = CharField(max_length=128)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=DO_NOTHING, related_name='couriers')

    def __str__(self):
        return self.name