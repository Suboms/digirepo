from django.db import models

# Create your models here.


class Country(models.Model):
    """
    This is the model that handels the creaion of a country
    """

    name = models.CharField(max_length=5000, default="", unique=True, primary_key=True)
    country_code = models.CharField(max_length=20, default=None, unique=True, null=True)
    capital = models.CharField(max_length=5000, default=None, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Country"


class State(models.Model):
    """
    This is the model that handels the creaion of a state
    """

    country = models.ForeignKey(Country, on_delete=models.PROTECT, default="")
    name = models.CharField(max_length=6000, default="", unique=True, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "State"


class School(models.Model):
    """
    This is the model that handels the creaion of a school
    """

    name = models.CharField(max_length=255, default="", unique=True)
    abbr = models.CharField(max_length=50, default=None, blank=True, null=True)
    country = models.ForeignKey(
        Country, on_delete=models.PROTECT, max_length=255, default=""
    )
    state = models.ForeignKey(
        State, on_delete=models.PROTECT, max_length=255, default=None, null=True
    )
    address = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=255, default="")
    email = models.EmailField(max_length=255, default="")
    pob = models.CharField(max_length=255, default="", verbose_name="P.O.Box")
    date_established = models.DateField(verbose_name="Date Established")
    website = models.URLField(max_length=255, default=None, blank=True, null=True)
    domain = models.URLField(max_length=255, default=None, null=True, blank=True)
    affiliation = models.ManyToManyField("self", blank=True, symmetrical=False)
    logo = models.ImageField(upload_to="schools/", default=None, blank=True, null=True)
    description = models.TextField(default="", max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Schools"
