InputList = []
Number = int(input("Enter number of element of input list "))

for i in range(0,Number):
    elements = int(input())
    InputList.append(elements)
num = int(input("Enter the Number need to be inseted"))
position = int(input("Enter Index of inserted number"))

InputList.insert(position,num)
print("Sucessfully Inserted",InputList)