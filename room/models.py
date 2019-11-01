from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from user import models as user_models


class AbstractItem(core_models.AbstractTimeStamp):
    name = models.CharField(max_length=80)

    class Meta:
        abstract = True


class RoomType(AbstractItem):
    def __str__(self):
        return self.name


# Create your models here.
class Room(core_models.AbstractTimeStamp):
    name = models.CharField(max_length=140)
    description = models.TextField(default="")
    country = CountryField()
    city = models.CharField(max_length=80)
    address = models.CharField(max_length=140)
    guest = models.IntegerField()
    bedroom = models.IntegerField()
    bed = models.IntegerField()
    bathroom = models.IntegerField()
    price = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_type = models.ManyToManyField(RoomType)

    def __str__(self):
        return self.name
