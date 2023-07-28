from django.contrib import admin
from App.models import Location,UserRating,Restaurant,Dish,User_Profile
# Register your models here.


admin.site.register(User_Profile)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('address', 'zipcode', 'city_id', 'latitude', 'longitude', 'country_id', 'locality_verbose')

@admin.register(UserRating)
class UserRatingAdmin(admin.ModelAdmin):
    list_display = ('votes', 'rating_text', 'rating_color', 'aggregate_rating')

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'lat_long', 'offers', 'location', 'cuisine', 'currency', 'price_range', 'user_rating',
                    'mezzo_provider', 'order_deeplink', 'has_table_booking', 'is_delivering_now', 'opentable_support')

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'dish_name', 'price')
# Register your models here.
