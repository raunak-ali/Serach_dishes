# Serach_dishes
A Template based django search application that can search through the names of dishes and recommend the best match for the same.
# Populating Sqlite DB from he given csv/excel:-
Model Structure:-
Restaurants:-
    id  
    Name
    lat_long
    Offers
    Location(Foreign Key)
    Cousine
    Currency
    price_range
    User_Rating(Fore0gn_Key)
    mezzo_provider
    order_deeplink(Link)
    has_table_booking(Numerical boolean)
    is_delivering_now(Numerical boolean)
    opentable_support(Numerical boolean)
    items(LList of Dish id's)

Dishes:-
    id
    Restaurant(Foreign-Key)
    Dish Name(TEXT)
    Price(INT)
Location:-
   
    Address
    Zipcode
    city_id
    latitude
    locality
    longitude
    country_id
    locality_verbose
User_Rating:-
    Votes
    Rating text
    Rating color
    aggregate_rating