'''
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
'''

class administrator():
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        for i in range(len(self.privileges)):
            print("This Admin have privileges like : " + self.privileges[i])
        


foo = ["Add post", "Delete post", "Ban user"]
admin = administrator(foo)
admin.show_privileges()
