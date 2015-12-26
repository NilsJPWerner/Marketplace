from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from decimal import Decimal

#Disclaimer: Our models are based on https://github.com/sczizzo/Dhaka/blob/develop/db/schema.rb
# Create your models here.


# class images(models.Model):
#   listing_id = models.IntegerField(null=False) #Maybe implement as foreignkey?
#   created_at = models.DateTimeField(auto_now_add=True, null=False)
#   updated_at = models.DateTimeField(auto_now=True, auto_now_add=True, null=False)
#   photo_file_name = models.CharField(max_length=150)
#   photo_content_type = models.CharField(max_length=20)
#   photo_file_size = models.IntegerField(null=False)

UNI_DIV = (('NA', 'Not Affiliated'),
    ('first', 'First Year'),
    ('second', 'Second Year'),
    ('third', 'Third Year'),
    ('fourth', 'Fourth Year'),
    ('grad', 'Graduate Student'),
    ('faculty', 'Faculty Member'),
    ('other', 'Other division'))

ROOMMATES = (('0', '0'), ('1', '1'),
            ('2', '2'), ('3', '3'),
            ('4', '4'), ('5+', '5+'))

BED_SIZE = (('king', 'King'),
    ('queen', 'Queen'),
    ('full', 'Full'),
    ('twin', 'Twin'))

BATHROOM = (('shared', 'Shared'),
    ('private', 'Private'))


class ExtendedUser(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, default="0", null=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures',
        default="/static/img/accounts/empty-photo.png", blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    uni_division = models.CharField(choices=UNI_DIV, max_length=50, blank=True)
    description = models.TextField(blank=True)


def user_post_save(sender, instance, created, **kwargs):
    # Create a user profile when a new user account is created
    if created:
        p = ExtendedUser()
        p.user = instance
        p.save()


class Listing(models.Model):
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # Blank is temporary, need to add a method to allow blank save
    # but then require it to be published
    # Descrition step
    listing_name = models.CharField(max_length=40, blank=True)
    summary = models.TextField(max_length=400, blank=True)
    address = models.CharField(max_length=100, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=Decimal(41.796662))
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=Decimal(-87.594183))

    # Details step
    bed_size = models.CharField(choices=BED_SIZE, max_length=10, blank=True)
    roomate_count = models.CharField(choices=ROOMMATES, max_length=5, blank=True)
    bathroom = models.CharField(choices=BATHROOM, max_length=10, blank=True)
    ac = models.BooleanField(default=False)
    in_unit_washer_dryer = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    cable_tv = models.BooleanField(default=False)
    internet = models.BooleanField(default=False)
    wheel_chair_accessible = models.BooleanField(default=False)
    pets_live_here = models.BooleanField(default=False)
    pets_allowed = models.BooleanField(default=False)



    price = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    # permalink = models.CharField(blank=False, null=False, max_length=300)
    renewed_at = models.DateTimeField(auto_now=True, null=True)
    renewals = models.IntegerField(default=0)
    published = models.BooleanField(default=True)
    #added stuff
    slug = models.SlugField(max_length=300)


    # def get_absolute_url(self):
    #     return reverse('accounts:display_listing', args=(self.slug,))

    # def get_absolute_edit_url(self):
    #     return reverse('accounts:edit_listing', kwargs={'slug': self.slug})
    #     # return reverse('edit_listing', kwargs={'slug': self.slug,})


