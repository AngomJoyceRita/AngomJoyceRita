
while True:
    first = input("Enter the first number: ")
    try:
        num1 = int(first)
        break
    except:
        print("Please enter a valid number.")
while True:
    second = input("Enter the second number: ")
    try:
        num2 = int(second)
        if num2 == 0:
            print("Second number cannot be zero.")
        else:
            break
    except:
        print("Please enter a valid number.")

result = num1 / num2
print("The result is:", result)
