from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "Male"
    GENDER_FEMALE = "Female"
    GENDER_OTHER = "Other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "English"
    LANGUAGE_FINNISH = "Finnish"
    LANGUAGE_VIETNAMESE = "vietnamese"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_FINNISH, "Finnish"),
        (LANGUAGE_VIETNAMESE, "Vietnamese"),
    )

    CURRENCY_EUR = "EUR"
    CURRENCY_USD = "USD"

    CURRENCY_CHOICES = ((CURRENCY_EUR, "EUR"), (CURRENCY_USD, "USD"))

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField(default="")
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=10, null=True, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True
    )
    superhost = models.BooleanField(default=False)
