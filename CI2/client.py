import Pyro4

uri = "PYRONAME:string.concatenator"
concatenator = Pyro4.Proxy(uri)

# Input from user
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

result = concatenator.string_concat(s1,s2)
print(f"Concatenation of the string is :{result}")