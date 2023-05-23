from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='order_user')
DESIGNATION = (
    ("Staff", "Staff"),
    ("Student", "Student"),
)


class User(AbstractUser):
    username = models.CharField(max_length=255, default=None, null=True, unique=True)
    first_name = models.CharField(max_length=255, default=None, null=True)
    last_name = models.CharField(max_length=255, default=None, null=True)
    email = models.EmailField(max_length=255, default=None, null=True, unique=True)
    designation = models.CharField(
        max_length=255, default=None, null=True, blank=True, choices=DESIGNATION
    )
    password2 = models.CharField(
        max_length=128,
        default=None,
        null=True,
        blank=True,
        verbose_name="Confirm Password",
    )
    avatar = models.ImageField(
        upload_to="images", default="avatar.png", null=True, blank=True
    )
    slug = models.SlugField(max_length=255, default=None, null=True, unique=True)
