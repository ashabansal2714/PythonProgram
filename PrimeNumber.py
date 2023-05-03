def is_prime(num):
    if num > 1:
      for i in range(2, int(num/2)+1):
          if (num % i) == 0:
              return False
    return True

number = int(input("Enter Number"))
if is_prime(number):
    print(number,"The number is prime number")
else:
    print(number,"The number is not prime number")
