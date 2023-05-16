def defangIPaddr(address):
        ans=address.replace(".","[.]")
        return ans

address = input("Enter IP addresss")
defangingAddress = defangIPaddr(address)
print(defangingAddress)