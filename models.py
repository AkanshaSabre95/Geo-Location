
from django.contrib.gis.db import models

# Create your models here.
from django.contrib.gis.db.models import PointField


class Customer(models.Model):
    customer_id = models.AutoField
    customer_name = models.CharField(max_length=50)
    point = PointField()

    @property
    def lat_lng(self):
        return list(getattr(self.point, 'coords', [])[::-1])


class Bookmark(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE,
                                    primary_key=True)
    title = models.CharField(max_length=20)
    url = models.URLField(default=" ")
    Source_name = models.CharField(max_length=20)

class CustomerBookmark(models.Model):
    bookmark = models.ForeignKey(Bookmark, on_delete=models.CASCADE)