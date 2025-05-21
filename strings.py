#conctinate a string and an integer
mystr = "I am "
age = 25
message = mystr + str(age)  
print(message)
#remove extra spaces
txt = "      Hello,       Uganda!       "
txt2 = " ".join(txt.split())
print(txt2)
#txt to uppercase
print(txt.upper()) 
#replace u with v
print(txt.replace("U", "V"))
#return a range of characters
y = "I am proudly Ugandan"
print(y[1:4])
# correct the error
x = 'All "Data Scientists" are cool!'  
print(x)
