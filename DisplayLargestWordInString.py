str = input("Enter Input string")

splitInput = str.split()
print(splitInput)
max=0
largeWord =""
for i in splitInput:
    if len(i) > max:
        largeWord = i
        max = len(i)
print(largeWord,"is largest word in given string , which Length is", max)