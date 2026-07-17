# Simple calculator 
a = int(input("Enter the first number: "))
b = input("Enter the operator (+, -, *, /): ")
c = int(input("Enter the second number: "))

if b == "+":
    print(a + c)
elif b == "-":
    print(a - c)
elif b == "*":
    print(a * c)
elif b == "/":
  print(a /c)
  
else:
    print("Operator is not valid")
  
