count = int(input("Enter count of given real number"))
i=0
Product = 1
for i in range(count):
    x = float(input("Enter Real number"))
    Product *= x
print("This is product of Real Number",Product)