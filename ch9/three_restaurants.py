"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.

"""

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("At " + self.restaurant_name + " " + self.cuisine_type + " cuisine is famous.")
    def open_restaurant(self):
        print("Welcome!, " + self.restaurant_name + " is open for you.")
restaurant = Restaurant("Hayatt", "Indian")
restaurant_a =  Restaurant("TGB", "South Indian")
restaurant_b =  Restaurant("Burj-Al-Arab", "Chinese")

# First instance

restaurant.open_restaurant()
restaurant.describe_restaurant()
print("\n")

# Second instance

restaurant_a.open_restaurant()
restaurant_a.describe_restaurant()
print("\n")

# Third instance

restaurant_b.open_restaurant()
restaurant_b.describe_restaurant()