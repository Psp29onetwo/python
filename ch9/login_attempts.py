"""
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3(Users.py) (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.

"""

class User:
    def __init__(self, first_name, last_name, profession, hobbie, login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.profession = profession
        self.hobbie = hobbie
        self.login_attempts = login_attempts
    def describe_user(self):
        print(self.first_name.title() + self.last_name.title() + " have knowledge of " + self.profession + " profession and having " + self.hobbie + " hobbie.")
    
    def greet_user(self):
        print("Hello!, " + self.first_name.title() + self.last_name.title() + " i like your personal interest for " + self.profession) 
        print(" and your hobbies " + self.hobbie + " too!")
    def increment_login_attempts(self):
        self.login_attempts += 1
        print("Logged in " + str(self.login_attempts) + "th time")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("LogIn attemps has been resetted to " + str(self.login_attempts))

user = User("Paurav", "patel", "Computer science", "Exploration and coding")

# Inccrementing the Login attempts
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

#resetting the Login attempts
user.reset_login_attempts()
