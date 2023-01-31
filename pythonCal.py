#calculator by Rohan
# functions for what method they want to calculate in 
def add(x, y):
   """This function adds two numbers"""

   return x + y

def subtract(x, y):
   """This function subtracts two numbers"""

   return x - y

def multiply(x, y):
   """This function multiplies two numbers"""

   return x * y

def divide(x, y):
   """This function divides two numbers"""

   return x / y

# start
# UI opens first
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# gets user choice 
choice = input(":")

# user enters 2 numbers they want to calculate 
numb1 = int(input("Enter first number: "))
numb2 = int(input("Enter second number: "))

# if else statments for what their choice is 
if choice == '1':
   print(numb1,"+",numb2,"=", add(numb1,numb2))

elif choice == '2':
   print(numb1,"-",numb2,"=", subtract(numb1,numb2))

elif choice == '3':
   print(numb1,"*",numb2,"=", multiply(numb1,numb2))

elif choice == '4':
   print(numb1,"/",numb2,"=", divide(numb1,numb2))
else:
   print("Invalid input")