InputList = []
number = int(input("Enter number of elements : "))
oddNumberCount=0
evenNumberCount=0
for i in range(0, number):
    element = int(input())
    InputList.append(element) 
 
for i in range(len(InputList)):
    if(InputList[i]%2 != 0):
        oddNumberCount += 1
    elif(InputList[i]%2==0):
        evenNumberCount += 1
print("The number of odd numbers in the list are:",oddNumberCount)
print("The number of even numbers in the list are:",evenNumberCount)
