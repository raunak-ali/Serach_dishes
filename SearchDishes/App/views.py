from django.shortcuts import render
import pandas as pd
import openpyxl
import csv
import json
import ast
import re
from django.db.models import Q
from .forms import DishForm
from .models import Restaurant, Dish, Location, UserRating


def search(request):
    form = DishForm()
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            dish_name = form.cleaned_data.get('dish_name')
            price = form.cleaned_data.get('price')
            # Initialize the query without any filters
            query = Q()

            # Perform the search using Q objects
            # Check if the dish_name field is not empty
            if dish_name:
                query |= Q(dish_name__icontains=dish_name)

            # Check if the price field is not empty
            if price:
                query |= Q(price__icontains=price)

            # Perform the search based on the combined query
            results = Dish.objects.filter(query)
            print(results)
        else:
            results = None
        return render(request,"results.html",{'results': results, 'form': form})
    return render(request,"form.html",context={"form":form})
    

    


def Populate(request):
    # Create empty lists to store instances
    restaurants = []
    dishes = []
    locations = []
    user_ratings = []

    # Assuming your Excel sheet is named "restaurants_data.xlsx"
     # Assuming your Excel sheet is named "restaurants_data.xlsx"
    df = pd.read_csv('/workspaces/Serach_dishes/EXCELDATA/restaurants_small (1).csv')
    #print(df)
    # Extracting the relevant columns from the Excel sheet
    restaurants_data = df[['id', 'name', 'lat_long', 'items','full_details']]
    restaurants_data['full_details']
    result=[]
    full_details = restaurants_data['full_details']
    full=pd.DataFrame()
    for f in full_details:
        if(type(f) == str):
            data = json.loads(f)
            Details=pd.json_normalize(data)
            #print(Details)
            full=pd.concat([Details, full],axis=0)
        else :
            last_index = len(full)
            full.loc[last_index] = None
            #full=pd.concat([Details, full],axis=0)
    print(full['location.city_id'])
    
    #Taking carre of  dishes/menu per restaurant
    menu=pd.DataFrame()
    menu['res_name']=''
    menu['dish_name']=''
    menu['price']=''
    items = restaurants_data['items']
    index=0
    for i in items:
        print("IN ITEMS")
        
        i=i.strip("{}")
        i=i.replace('"', '')
        Items=i.split(",")
        #print(I)
        for I in Items:
            Pairs=I.split(":")
            if len(Pairs)==1:
                #print(Pairs)
                last=len(menu)
                name=restaurants_data.iloc[index]['name']
                menu.loc[last] = [name,Pairs[0],""]
            else:
                last=len(menu)
                name=restaurants_data.iloc[index]['name']
                menu.loc[last] = [name,Pairs[0],Pairs[1]]
                #print(Pairs[0])
        index+=1
    p=0
    # Loop through the data and create instances for each row
    full.fillna(0, inplace=True)
    restaurants_data.fillna(0, inplace=True)
    menu.fillna(0, inplace=True)
    for x  in range(len(full)):
        print("Making objects")

        # Create Location instance
        location = Location.objects.create(
            address=full.iloc[x]['location.address'],
            zipcode=full.iloc[x]['location.zipcode'],
            city_id=full.iloc[x]['location.city_id'],
            latitude=full.iloc[x]['location.latitude'],
            locality=full.iloc[x]['location.locality'],
            longitude=full.iloc[x]['location.longitude'],
            country_id=full.iloc[x]['location.country_id'],
            locality_verbose=full.iloc[x]['location.locality_verbose']
        )
        print('LOCATION',location)
        locations.append(location)

    
        user_rating = UserRating.objects.create(
            votes=full.iloc[x]['user_rating.votes'],
            rating_text=full.iloc[x]['user_rating.rating_text'],
            rating_color=full.iloc[x]['user_rating.rating_color'],
            aggregate_rating=full.iloc[x]['user_rating.aggregate_rating']
        )

        print(user_rating)
        user_ratings.append(user_rating)

        # Create Restaurant instance
        restaurant = Restaurant.objects.create(
            id_number=restaurants_data.iloc[x]['id'],
            name=restaurants_data.iloc[x]['name'],
            lat_long=restaurants_data.iloc[x]['lat_long'],
            location=location,
            currency=full.iloc[x]['currency'],
            price_range=full.iloc[x]['price_range'],
            user_rating=user_rating,
            mezzo_provider=full.iloc[x]['mezzo_provider'],
            order_deeplink=full.iloc[x]['order_deeplink'],
            has_table_booking=full.iloc[x]['has_table_booking'],
            is_delivering_now=full.iloc[x]['is_delivering_now'],
            opentable_support=full.iloc[x]['opentable_support'],
            book_form_web_view_url= full.iloc[x]['book_form_web_view_url'],
            has_online_delivery=full.iloc[x]['has_online_delivery'],
            include_bogo_offers=full.iloc[x]['include_bogo_offers'],
            switch_to_order_menu= full.iloc[x]['switch_to_order_menu'],
            is_book_form_web_view= full.iloc[x]['is_book_form_web_view'],
            is_table_reservation_supported= full.iloc[x]['is_table_reservation_supported'],
            average_cost_for_two=full.iloc[x]['average_cost_for_two'],
        
        
        
        )
        print(restaurant)
        restaurants.append(restaurant)

    
        
        while(menu.iloc[p]['res_name']==restaurants_data.iloc[x]['name']):
                dish = Dish.objects.create(
                    restaurant=restaurant,
                    dish_name=menu.iloc[p]['dish_name'],
                    price=menu.iloc[p]['price']
                )
                p+=1
                print(dish)
                dishes.append(dish)
        
        
    Restaurant.objects.bulk_create(restaurants)
    Dish.objects.bulk_create(dishes)
    Location.objects.bulk_create(locations)
    UserRating.objects.bulk_create(user_ratings)
                
        
   


                
                

      

        

    return render(request,"index.html")