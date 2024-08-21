from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class Library(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=255)

