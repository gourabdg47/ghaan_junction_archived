from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator  # Optional: Enforce password strength


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True, validators=[RegexValidator(r"^\d{10}$")])
    password = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(8, "Password must be at least 8 characters long")]  # Optional
    )
    industry = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    current_company = models.CharField(max_length=200, blank=True)
    past_companies = models.TextField(blank=True)
    education = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    is_teacher = models.BooleanField(default=False)
    
    # Skill relationship (ManyToManyField for many-to-many association)
    skills = models.ManyToManyField('Skill', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Enforce unique skill names
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
