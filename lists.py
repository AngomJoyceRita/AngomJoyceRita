#create a list and output the second item
names = ["John", "Mary", "Leo", "Jane", "Peter"]
print(names[1])
#change the first value
names[0]="Patric"
print(names)
#add a 6th item to the list
names.append("Ron")
print(names)
#add item in 3rd position
names.insert(2, "Bathel")
print(names)
#remove the 4th item from the list
names.pop(3)
print(names)
#use negative index to print the last item
print(names[-1])
#using range to print
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Brown"]
print(colors[2:5])
#copy of a list
countries = ["Canada", "France", "Zambia"]
CC = countries.copy()
for c in CC:
    print(c)   
#sorting a list in ascending and descending order
animals = ["Dog", "Cat", "Horse", "Fish", "Monkey", "Zebra"]
animals.sort() 
print(animals)#ascending
animals.sort(reverse=True)
print(animals)#descending
#animals with 'a' in them
for x in animals:
    if 'a' in x.lower():
        print(x)
#join lists
firstNames = ["Joyce", "Rita"]
lastNames = ["Angom"]  
firstNames.extend(lastNames)  
print(firstNames)    