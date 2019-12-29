#Changingguestlist.py program
Guest_for_dinner = ['Hiren','Naman','Saumya','Srinath','Kundan']
Cantmakeit = Guest_for_dinner.pop()
print(Cantmakeit+"Can't make it")
print(Guest_for_dinner)
Guest_for_dinner.append('Raju')
print(Guest_for_dinner)
message = "Would you like to have dinner today at my place?"
print(Guest_for_dinner[0] + ", "+ message)
print(Guest_for_dinner[1] + ", "+ message)
print(Guest_for_dinner[2] + ", "+ message)
print(Guest_for_dinner[3] + ", "+ message)
print(Guest_for_dinner[4] + ", "+ message)

#new program begins here
print("Oh!, we have biger dinner table we can invite more friends")
Guest_for_dinner.insert(0 ,'Jay')
Guest_for_dinner.insert(3 , 'Dhruv')
Guest_for_dinner.insert(-1 , 'Devansh')
print(Guest_for_dinner[0] + ", "+ message)
print(Guest_for_dinner[1] + ", "+ message)
print(Guest_for_dinner[2] + ", "+ message)
print(Guest_for_dinner[3] + ", "+ message)
print(Guest_for_dinner[4] + ", "+ message)
print(Guest_for_dinner[5] + ", "+ message)
print(Guest_for_dinner[6] + ", "+ message)
print(Guest_for_dinner[7] + ", "+ message)
