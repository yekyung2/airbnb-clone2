from django.db import models

# Create your models here.
class Room(models.Model):

    """Room Model Definition"""

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True