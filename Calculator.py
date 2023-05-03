a = int(input("Enter first number"))
operator = input("Enter operatore (+,-,*,/,%) : ")
b = int(input("Enter second number"))

if operator == '+':
   print(a+b)
elif operator == '-':
   print(a-b)
elif operator == '*':
 print(a * b)
elif operator == '/':
    print(a/b)
elif operator =='%':
   print(a%b)
else:
    print("Invalid Operation")
