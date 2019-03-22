from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
import uuid

from locations.models import Location

# Create your models here.
# class Broker(models.Model):
# 		user = models.OneToOneField(User, on_delete=models.CASCADE)

# 		broker_id = models.UUIDField(primary_key=True, default=uuid.uuid4)

# 		def __init__(self):
# 				return f'{self.user.first_name} {self.user.last_name}'

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

class Property(models.Model):
		SINGLE_HOME = 'SINGLE_FAMILY_HOME'
		CONDO_HOME = 'CONDO_HOME'
		MOBILE_HOME = 'MOBILE_HOME'
		CONDO = 'CONDO'
		PLEX = 'PLEX'
		LOFT_OR_STUDIO = 'LOFT/STUDIO'
		LOT = 'LOT'
		HOBBY_FARM = 'HOBBY FARM'
		INTERGEN = 'INTERGENERATIONAL'

		PROPERTY_TYPE_CHOICES = (
				(SINGLE_HOME, 'Single-family home'),
				(CONDO_HOME, 'Condominium home'),
				(MOBILE_HOME, 'Mobile home'),
				(CONDO, 'Condo'),
				(PLEX, 'Plex'),
				(LOFT_OR_STUDIO, 'Loft/Studio'),
				(LOT, 'Lot'),
				(HOBBY_FARM, 'Hobby Farm'),
				(INTERGEN, 'Intergenerational'),
		)

		property_type = models.CharField(
				max_length=20,
				choices=PROPERTY_TYPE_CHOICES,
				default=SINGLE_HOME
		)

		property_id = models.UUIDField(primary_key=True, default=uuid.uuid4)

		is_for_sale = models.BooleanField(default=True)

		cost = models.IntegerField(default=0)

		location = models.ForeignKey(Location, on_delete=models.CASCADE)

		num_of_bedrooms = models.IntegerField(default=0)

		num_of_bathrooms = models.IntegerField(default=0)

		num_of_parking_spaces = models.IntegerField(default=0)

		num_of_garages = models.IntegerField(default=0)

		# added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

		has_pool = models.BooleanField(default=False)

		has_waterfront = models.BooleanField(default=False)

		has_elevator = models.BooleanField(default=False)

		added_on = models.DateField()

		class Meta:
				ordering = ['-added_on']
				verbose_name_plural = 'properties'

		def __init__(self):
				if self.is_for_sale == True:
						return f'{self.property_type} for sale'
				else:
						return f'{self.property_type} for rent'
