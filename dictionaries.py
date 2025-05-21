#print value of shoe size
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(Shoes["size"]) 
#change value
Shoes["brand"] = "Adidas"
print(Shoes)
#add key value pair
Shoes["type"] = "sneakers"
print(Shoes)
#return a list of keys
print(list(Shoes.keys()))
# list of values
print(list(Shoes.values()))
#check if key exists in the dictionary
if "size" in Shoes:
    print("Yes, 'size' is one of the keys in the dictionary.")
#loop through dictionary
for key, value in Shoes.items():
    print(key, ":", value)
#remove color from the disctionary
Shoes.pop("color")
print(Shoes)
#empty the dictionary
Shoes.clear()
print(Shoes)  
#copy a dictionary
myDictionary = {
    "name": "Joyce",
    "age": 22,
    "course": "Software Engineering"
}
copyDictionary = myDictionary.copy()
print(copyDictionary)
#nested dictionaries
myFamily = {
    "child1": {
        "name": "John",
        "age": 15
    },
    "child2": {
        "name": "Lilly",
        "age": 12
    }
}
print(myFamily)
