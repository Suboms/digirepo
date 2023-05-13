from django_countries.fields import CountryField
from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=255, default="", unique=True)

    class Meta:
        verbose_name_plural = "Country"


class State(models.Model):
    name = models.CharField(max_length=255, default="", unique=True)
    country = models.ForeignKey(
        Country, on_delete=models.PROTECT, default="--------")

    class Meta:
        verbose_name_plural = "State"


class City(models.Model):
    name = models.CharField(max_length=255, default="", unique=True)
    state = models.ForeignKey(
        State, on_delete=models.PROTECT, default="--------")

    class Meta:
        verbose_name_plural = "Cities"


class Schools(models.Model):
    name = models.CharField(max_length=255, default="", unique=True)
    country = models.ForeignKey(
        Country, on_delete=models.PROTECT, max_length=255, default="")
    state = models.ForeignKey(
        State, on_delete=models.PROTECT, max_length=255, default="")
    city = models.ForeignKey(
        City, on_delete=models.PROTECT, max_length=255, default="")
    address = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=255, default="")
    email = models.EmailField(max_length=255, default="")
    pob = models.CharField(max_length=255, default="", verbose_name="P.O.B")
    date_established = models.DateField(verbose_name="Date Established")
    website = models.CharField(
        max_length=255, default=None, blank=True, null=True)
    logo = models.ImageField(upload_to="schools/",
                             default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    description = models.TextField(default="", max_length=255)

    class Meta:
        verbose_name_plural = "Schools"
