from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Squirrel(models.Model):
    longitude = models.FloatField('Longitude')

    latitude = models.FloatField('Latitude')

    squirrel_id = models.CharField(help_text = _('Unique Squirrel ID'),
        max_length=50)

    def __str__(self):
        return self.squirrel_id



