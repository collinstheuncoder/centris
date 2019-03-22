from django.db import models
import uuid

from locations.models import Location

# Create your models here.
class Agency(models.Model):
		agency_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
		name = models.CharField(max_length=200)
		location = models.ForeignKey(Location, on_delete=models.PROTECT)

		class Meta:
				verbose_name_plural = 'agencies'

		def __init__(self):
				return self.name
