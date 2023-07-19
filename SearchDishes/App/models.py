from django.db import models

# Create your models here.
class Location(models.Model):
    address = models.CharField(max_length=255,null=True,blank=True)
    zipcode = models.CharField(max_length=10,null=True,blank=True)
    city_id = models.IntegerField(null=True,blank=True)
    latitude = models.FloatField(null=True,blank=True)
    locality = models.CharField(max_length=100,null=True,blank=True)
    longitude = models.FloatField(null=True,blank=True)
    country_id = models.IntegerField(null=True,blank=True)
    locality_verbose = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.address

class UserRating(models.Model):
    votes = models.IntegerField()
    rating_text = models.CharField(max_length=100)
    rating_color = models.CharField(max_length=20)
    aggregate_rating = models.FloatField()

    def __str__(self):
        return f"Rating: {self.aggregate_rating}"

class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=False)  # Manually define the primary key
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
    has_table_booking = models.BooleanField()
    is_delivering_now = models.BooleanField()
    opentable_support = models.BooleanField()
    has_online_delivery=models.BooleanField()
    include_bogo_offers=models.BooleanField()
    switch_to_order_menu= models.BooleanField()
    is_book_form_web_view= models.BooleanField()
    is_table_reservation_supported= models.BooleanField()
    average_cost_for_two=models.IntegerField(null=True,blank=True)
    items = models.ManyToManyField('Dish', related_name='restaurants',null=True,blank=True)

    def __str__(self):
        return self.name

class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dish_name = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.dish_name