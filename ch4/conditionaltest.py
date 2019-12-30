cars = ['audi', 'bmw', 'subaru', 'toyota']
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
car = 'audi'
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
car = 'bmw'
print("\nIs car == 'bmw'? I predict False.")
print(car == 'bmw')
car = 'subaru'
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
car = 'bmw'
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
car = 'toyota'
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print("\nis cars have 'toyota'?")
if car in cars:
	print(car+" is in the list")
car1 = 'subaru'
if car and car1 in cars:
 print(car + " and "+ car1 +" is in the list\n")

if car or car1 in cars:
 print(car+ "is in the list")
if car not in cars:
	print(car + " is not in cars")
