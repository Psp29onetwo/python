"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.

"""

class User:
    def __init__(self, first_name, last_name, profession, hobbie):
        self.first_name = first_name
        self.last_name = last_name
        self.profession = profession
        self.hobbie = hobbie

    def describe_user(self):
        print(self.first_name.title() + self.last_name.title() + " have knowledge of " + self.profession + " profession and having " + self.hobbie + " hobbie.")
    
    def greet_user(self):
        print("Hello!, " + self.first_name.title() + self.last_name.title() + " i like your personal interest for " + self.profession) 
        print(" and your hobbies " + self.hobbie + " too!")
    
user = User("Paurav", "patel", "Computer science", "Exploration and coding")
user_a = User("Saumya", "Shah", "Graphic Designing", "Travelling and food")
user_b = User("Naman", "Vyas", "idk(it changes everyday)😂😂😂😁🤣", "Bike Riding")

#First instance
user.describe_user()
user.greet_user()

#Second instance
user_a.describe_user()
user_a.greet_user()

#Third instance
user_b.describe_user()
user_b.greet_user()