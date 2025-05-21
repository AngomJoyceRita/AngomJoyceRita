#output choice brand
x = ("samsung", "iphone", "tecno", "redmi")
print(x[1])
#negative indexing
print(x[-2])
#update(tuplues are immutable)
y = list(x)
y[1] = "itel"
x = tuple(y)
print(x)
#add item
y = list(x)
y.append("Huawei")
x= tuple(y)
print(x)
#loop through tuples
for i in x:
    print(i)
#delete the first item
y = list(x)
del y[0]
x = tuple(y)
print(x)
#create a tuple with constructor
cities = tuple(["Kampala", "Gulu", "Mbale", "Mbarara", "Arua"])
print(cities)
#unpack a tuple
one, two, three, four, five = cities
print(one)
print(two)
print(three)
print(four)
print(five)
#range
print(cities[1:4])
#join tuples
first_names = ("Joyce", "Rita")
second_names = ("Angom",)
full_name = first_names + second_names
print(full_name)
#multiply tuples
colors = ("red", "yellow", "blue")
print(colors * 3)
#number of time 8 appears
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(8))







