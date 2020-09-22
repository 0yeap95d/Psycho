from django.utils import timezone
from django.db import models


class Store(models.Model):
    id = models.IntegerField(primary_key=True)
    store_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=20, null=True)
    area = models.CharField(max_length=50, null=True)
    tel = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=200, null=True)
    latitude = models.FloatField(max_length=10, null=True)
    longitude = models.FloatField(max_length=10, null=True)
    category = models.CharField(max_length=200, null=True)

    def __str__(self):
        return [self.id, self.store_name, self.branch, self.area, self.address]

    @property
    def category_list(self):
        return self.category.split("|") if self.category else []


class Review(models.Model):
    rid = models.IntegerField(primary_key=True)
    store = models.CharField(max_length=10, default=False)
    user = models.CharField(max_length=10, default=False)
    score = models.CharField(max_length=10, default=False)
    content = models.CharField(max_length=500, null=True)
    reg_time = models.CharField(max_length=50, default=False)

    def __str__(self):
        return [self.rid, self.store, self.user, self.score, self.content, self.reg_time]


class Hotel(models.Model):
    id = models.IntegerField(primary_key=True)
    tel = models.CharField(max_length=15, default=False)
    address1 = models.CharField(max_length=100, default=False)
    address2 = models.CharField(max_length=100, default=False)
    name = models.CharField(max_length=50, default=False)
    latitude = models.CharField(max_length=20, default=False)
    longitude = models.CharField(max_length=20, default=False)

    def __str__(self):
        return [self.id, self.tel, self.address1, self.address2, self.name, self.latitude, self.longitude]
