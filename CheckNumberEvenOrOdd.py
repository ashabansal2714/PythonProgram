def IsEven(number):
     if number%2 == 0:
        return True
     else: 
         return False


num = int(input("Enter number"))
if IsEven(num):
    print(num,"This is Even Number")
else:
     print(num,"This is odd Number")
