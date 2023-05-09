inputList= []
number = int(input("Enter number of element of input list"))

for i  in range(0,number):
    element = int(input())
    inputList.append(element)

largeNumber = inputList[0]
for i in range(len(inputList)):
    if(inputList[i]>largeNumber):
        largeNumber = inputList[i]
        position = i
print("This is the largest element", largeNumber,"and position of number",position )