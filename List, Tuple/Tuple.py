#Tuple нь эрэмбэлэх боломжгүй , элемент давхардаж болох ч элемент өөрчлөх боломжгүй өгөгдлийн цуглуулгийн төрөл юм .
mytuple = ("apple", "banana", "cherry") # Creating tuple
print(mytuple) # Printing tuple
print(mytuple[1]) # Printing element by their index 
print(len(mytuple)) # Finding number of element in mytuple 
print(mytuple.count("banana")) # Printing count of element in tuple
print(mytuple.index("banana")) # Printing the index of parametrized element 
for x in mytuple :
    print(x)

if "apple" in mytuple :
    print("There is apple in mytuple")
else :
    print("There is no such a thing like apple here ")


del mytuple # Deleting tuple  

