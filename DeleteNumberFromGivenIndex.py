inputList = []
Number = int(input("Enter element number for a List"))

for i in range(0,Number):
    element = int(input())
    inputList.append(element)

position = int(input("Enter number need to be deleted from given postion"))

inputList.pop(position)

print("Successfully Deleted number from given list",inputList)
    

