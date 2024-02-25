from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField


class Language(models.Model):

    OFFICIAL_LANGUAGES = [
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
        ('te', 'Telugu'),
        ('mr', 'Marathi'),
        ('ta', 'Tamil'),
        ('ur', 'Urdu'),
        ('gu', 'Gujarati'),
        ('kn', 'Kannada'),
        ('or', 'Odia'),
        ('ml', 'Malayalam'),
        ('pa', 'Punjabi'),
        ('as', 'Assamese'),
        ('mr', 'Maithili'),
        ('sd', 'Sindhi'),
        ('sa', 'Sanskrit'),
        ('ksh', 'Kashmiri'),
        ('ne', 'Nepali'),
        ('kok', 'Konkani'),
        ('bodo', 'Bodo'),
        ('dogri', 'Dogri'),
        ('manipuri', 'Manipuri'),
        ('santali', 'Santali'),
    ]

    name = models.CharField(max_length=100, choices=OFFICIAL_LANGUAGES)

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Ensure unique skill names
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class User(AbstractUser):

    INDUSTRY_CHOICES = [
        ('Tech', 'Technology'),
        ('Finance', 'Finance'),
        ('Healthcare', 'Healthcare'),
        ('Education', 'Education'),
        ('Retail', 'Retail'),
        ('Automotive', 'Automotive'),
        ('Hospitality', 'Hospitality'),
        ('Entertainment', 'Entertainment'),
        ('Real Estate', 'Real Estate'),
        ('Fashion', 'Fashion'),
        ('Manufacturing', 'Manufacturing'),
        # Add more industry choices as needed
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    countries = CountryField(multiple=True)
    highest_education = models.CharField(max_length=50)
    professonal_headline = models.CharField(max_length=150)
    user_bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics')
    communication_languages = models.ManyToManyField(Language, blank=True)
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES)

    skills = models.ManyToManyField(Skill, blank=True)  # Many-to-many relationship
    tutor_status = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"

