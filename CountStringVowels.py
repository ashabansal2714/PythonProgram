def count_vowels(string):
    vowels ="aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
           count += 1
    return count 
     
inputString = input("Enter Input string")
num_vowels = count_vowels(inputString)
print(num_vowels)
