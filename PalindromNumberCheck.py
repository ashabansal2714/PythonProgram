number = int(input("Enter Number"))
temp = number
rev=0
while(number != 0):
    digit= number % 10
    rev =  rev * 10 + digit
    number = number // 10

if(temp == rev) :
    print("Successfully get palindrom number",rev)
else:
    print("Oops! Number is not palindrom",rev)
