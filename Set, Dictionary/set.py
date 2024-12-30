#Set нь индексгүй , давхардаж болохгүй өгөгдлийн цуглуулга төрөл юм 

# Create set
myset = {"apple " , "orange" , "banana"}
print(myset)

# Adding element into set
myset.add("cherry")
print(myset)

#Adding multiple element into set Example 1
myset.update(["ninja" , "blackbear"])
print(myset)


#Adding multiple element into set Example 2
x={"Banana", "Apple" , "Kiwi"}
y={"Mandarin" , "Oor yu c bdgin" , "Tarvas"}
x.update(y)
print(x)

#Finding length of set 
print(len(x))

#Deleting element from set
myset.remove("banana") # Remove raises KeyError when element is not found
myset.discard("Banana") # Discard just dont care about if its found or not 
print(myset)

# For loop
for element in myset :
    print(element)

# Checks if element is in set or not 
print("apple" in myset) # If there is returns true , if there isnt returns false


# Takes last element of myset and appends into x 
x.add(myset.pop())
print(x)
print(myset)

# Deletes all element of set 
myset.clear()
print(myset)

# Delete set
del myset

# Creating Z set by element that in x but doesnt in y 
x = {"apple" , "Thehell" , "ninja"}
y = {"Thehell" , "ninja" }
z = x.difference(y)
print(z)

# Updating x set by element that in x but doesnt in y
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)


# Checks if both sets has duplicated element
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y) # Returns true if there isnt duplicated element
print(z)

# Checks if x is subset of y  
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

# Checks if x is superset of y
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z) 

# Creates set for not duplicated 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

# Updates set for not duplicated element 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

# Creates set from all unique element of both set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)