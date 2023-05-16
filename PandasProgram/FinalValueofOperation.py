def finalValueAfterOperations(operations):
       return sum(op[1] == '+' or -1 for op in operations)

operation = input("Enter operations")
Value = operation.split()
finalValue = finalValueAfterOperations(Value)
print(finalValue)