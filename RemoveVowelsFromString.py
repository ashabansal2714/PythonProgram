string = input("Enter String")
result=""
vowels ="aeiouAEIOU"
count = 0
for i in range(0,len(string)):
    if string[i] not in vowels:
        result = result + string[i]
    elif string[i] in vowels :
            count+= 1
    else:
         continue;
        
print("Remove set of vowels from given string:",result, "  Count of removed vowels:",count)
