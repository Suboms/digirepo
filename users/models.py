from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from schools.models import *

# user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='order_user')
DESIGNATION = (
    ("Staff", "Staff"),
    ("Student", "Student"),
)


class User(AbstractUser):
    """
    This is the model that handels the creation of users for both individuals and schools
    """

    email = models.EmailField(max_length=255, default=None, null=True, unique=True)
    first_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None, null=True, blank=True
    )
    school_name = models.CharField(
        max_length=255,
        default=None,
        null=True,
        blank=True,
        unique=True,
        verbose_name="School Name",
    )
    designation = models.CharField(
        max_length=255, default=None, null=True, blank=True, choices=DESIGNATION
    )
    password2 = models.CharField(
        max_length=128,
        default="",
        null=True,
        blank=True,
        verbose_name="Confirm Password",
    )
    avatar = models.ImageField(
        upload_to="images",
        default="avatar.png",
        null=True,
        blank=True,
        verbose_name="Profile Picture",
    )
    slug = models.SlugField(
        max_length=255, default=None, null=True, blank=True, unique=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
