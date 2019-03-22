from django.db import models
from location_field.models.plain import PlainLocationField
import uuid

# Create your models here.
class Location(models.Model):
		location_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
		city = models.CharField(max_length=255)
		location = PlainLocationField(based_fields=['city'], zoom=7)

		def __init__(self):
				return self.city
