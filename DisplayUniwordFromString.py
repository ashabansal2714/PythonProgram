str =  input("Enter any string")
splitStr= str.split()
strList =[]
for i in splitStr:
    if i not in strList:
        strList.append(i)
str=""
for i in strList:
         str = str +"  "+ i
print("String with unique words are here",str)