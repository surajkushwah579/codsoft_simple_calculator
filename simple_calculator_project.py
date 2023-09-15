# Addition fuction
def add(x,y):
    return x+y

# Subtraction function
def sub(x,y):
    return x-y

# Multipliction function
def mul(x,y):
    return x*y

# Division function
def div(x,y):
    if y==0:
        return"cannot divide by zero"
    return x/y


while True:

    # Select the operation to performe
    print("select operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multipliction")
    print("4. Division")
    print("5. Exit")

    choice=input("Enter choice")

    if choice=="5":
        print("Exiting the calculator")
        break

    num1=float(input("Enter first number"))
    num2=float(input("Enter second number"))

    if choice=='1':  # choice 1 for additon
       
        print("Result: ",add(num1,num2))

    elif choice=='2': # choice 2 for subtraction

        print("Result: ",sub(num1,num2))
    elif choice=='3': # choice 3 for multipliction

        print("Result: ",mul(num1,num2))

    elif choice=='4':# choice 4 for Division

        print("Result:",div(num1,num2))

    else:

        print("invalid")
        


