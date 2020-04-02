'''
9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
'''

from ch9.admin import administrator


class privileges():
    def __init__(self, privileges):
        self.previleges = privileges

    def show_privileges(self):
        for i in range(len(self.privileges)):
            print("This Admin have privileges like : " + self.privileges[i])

foo = ["Add post", "Delete post", "Ban user"]
admin = administrator(foo)
admin.show_privileges()