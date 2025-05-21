#create a set with constructor
beverages = set(["soda", "coffee", "juice"])
print(beverages)
# add two items to the set
beverages.update(["tea", "milk"])
print(beverages)
#check
mySet = {"oven", "kettle", "microwave", "refrigerator"}
print("microwave" in mySet)
#remove
mySet.discard("kettle")
print(mySet)
# loop through set
for item in mySet:
    print(item)
# add from one list to a set
set1 = {"Able", "John", "Mary", "Sara"}
list1 = ["Tom", "Lisa"]
set1.update(list1)
print(set1)
# Join sets
ages = {22}
first_names = {"Joyce", "Rita"}
details = ages.union(first_names)
print(details)
