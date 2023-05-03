startRange = int(input("Enter Starting Range Number"))
endRange  = int(input("Enter upper Range Number"))
count = 0
for number in range(startRange , endRange + 1):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            count += 1
            print(number)
print("Prime numbers count in given range", count)


