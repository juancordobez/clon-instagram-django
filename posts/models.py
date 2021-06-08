"""Posts models."""

# Django
from django.db import models
from django.db.models.fields import EmailField

class User(models.Model):
    """User model. """

    email = models.EmailField()
    password = models.CharField()

    first_name = models.CharField()
    last_name = models.CharField()

    bio = models.TextField()

    birthdate = models.DateField()

    create = models.DateTimeField()
    modified = models.DateTimeField()
