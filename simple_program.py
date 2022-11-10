def add(x, y):
    return x + y 

def subtract(x, y):
   return x - y 

def multiply(x, y): 
  return x * y 

def divide(x, y): 
  return x / y 

print("Select operation.1-add,2-sub,3-mul,4-div") 
choice = input("Enter choice(1/2/3/4): ") 
x = float(input("Enter first number: ")) 
y = float(input("Enter second number: ")) 

if choice == '1’: 
  print(x, "+", y, "=", add(x, y)) 
elif choice == '2’: 
  print(x, "-", y, "=", subtract(x, y)) 
elif choice == '3’: 
  print(x, "*", y "=", multiply(x, y)) 
elif choice == ‘4’:
  if y!=0:
    print(x, "/", y, "=", divide(x, y))
  else:
    print(“Divisor cannot be 0”) 
else: 
  print("Invalid Input")
