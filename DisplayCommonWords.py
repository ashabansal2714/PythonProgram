str1=input("Enter first string:")
str2 = input("Enter second string:")
string1= str1.split()
string2 = str2.split()
for i in string1:
    if i in string2:
        print(i)
