from django.db import models

# Create your models here.
class Location(models.Model):
    address = models.CharField(max_length=255,null=True,blank=True)
    zipcode = models.CharField(max_length=10,null=True,blank=True)
    city_id = models.FloatField(null=True,blank=True)
    latitude = models.FloatField(null=True,blank=True)
    locality = models.CharField(max_length=100,null=True,blank=True)
    longitude = models.FloatField(null=True,blank=True)
    country_id = models.FloatField(null=True,blank=True)
    locality_verbose = models.CharField(max_length=255,null=True,blank=True)

    

class UserRating(models.Model):
    votes = models.FloatField(null=True,blank=True)
    rating_text = models.CharField(max_length=100,null=True,blank=True)
    rating_color = models.CharField(max_length=20,null=True,blank=True)
    aggregate_rating = models.FloatField(null=True,blank=True)

    

class Restaurant(models.Model):
    id_number = models.IntegerField()  # Manually define the primary key
    name = models.CharField(max_length=100)
    lat_long = models.CharField(max_length=100)
    offers = models.CharField(max_length=255,null=True,blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True,blank=True)
    cuisine = models.CharField(max_length=10000)
    currency = models.CharField(max_length=10)
    price_range = models.CharField(max_length=20)
    user_rating = models.ForeignKey(UserRating, on_delete=models.CASCADE,null=True,blank=True)
    mezzo_provider = models.CharField(max_length=100,null=True,blank=True)
    order_deeplink = models.URLField(null=True,blank=True)
    book_form_web_view_url= models.URLField(null=True,blank=True)
    has_table_booking = models.BooleanField(null=True,blank=True)
    is_delivering_now = models.BooleanField(null=True,blank=True)
    opentable_support = models.BooleanField(null=True,blank=True)
    has_online_delivery=models.BooleanField(null=True,blank=True)
    include_bogo_offers=models.BooleanField(null=True,blank=True)
    switch_to_order_menu= models.BooleanField(null=True,blank=True)
    is_book_form_web_view= models.BooleanField(null=True,blank=True)
    is_table_reservation_supported= models.BooleanField(null=True,blank=True)
    average_cost_for_two=models.FloatField(null=True,blank=True)
    items = models.ManyToManyField('Dish', related_name='restaurants',null=True,blank=True)

    

class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dish_name = models.TextField(null=True,blank=True)
    price = models.TextField(null=True,blank=True)

    