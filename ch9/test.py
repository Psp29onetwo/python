class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title(), str(self.age) + " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")
dog = Dog("psp", 21)
dog.sit()