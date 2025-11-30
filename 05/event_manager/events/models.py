from django.db import models


class Event(models.Model):
    name = models.TextField()
    date = models.DateField()
    location = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
