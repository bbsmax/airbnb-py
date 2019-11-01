from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GNEDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    LANGUAGE_KO = "ko"
    LANGUAGE_EN = "en"
    LANGUAGE_CHOICES = (
        (LANGUAGE_KO, "Ko"),
        (LANGUAGE_EN, "En"),
    )

    CURRENCY_KWD = "kwd"
    CURRENCY_USD = "usd"
    CURRENCY_CHOICES = (
        (CURRENCY_KWD, "kwd"),
        (CURRENCY_USD, "usd"),
    )
    avator = models.ImageField(null=True)
    bio = models.TextField(default="")
    gender = models.CharField(max_length=10, blank=True, choices=GNEDER_CHOICES)
    language = models.CharField(max_length=10, blank=True, choices=LANGUAGE_CHOICES)
    currency = models.CharField(max_length=10, blank=True, choices=CURRENCY_CHOICES)
    birthdate = models.DateField(blank=True, null=True)
    superhost = models.BooleanField(default=False)