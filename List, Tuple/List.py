# List нь эрэмбэлэх боломжтой , элемент давхардах болон өөрчлөх боломжтой өгөгдлийн цуглуулгийн төрөл юм .
fruits = ['apple', 'orange','banana']
print(fruits[0]) # Accessing list element by their index 
print(fruits) # Print all element of list
fruits.append("cherry") # Adding element in back of list
fruits.insert(1,'kiwi') # Adding element in any position of list by index
listcopy1 = fruits.copy() # Copying list into listcopy1 by copy function 
listcopy2 = list(fruits) # Assigning same value into listcopy 2 (Just saying copying in different way) 
print(listcopy1)
print(listcopy2)
fruits.remove('banana') # Deleting element by their value 
fruits.pop(1) # Deleting element by their index , if there is no index it will remove last element of list 
del fruits[2] # Delete element by their index , if there is no index it will delete whiole list
fruits.clear() # Delete all element of list 
x = listcopy1.count("banana") # Returning count of searching element
cars = ["Goy mashin", "Gal2 mashin"] 
listcopy1.extend(cars) # Combines two lists all element of cars added in back of list
print(listcopy1) 
a = listcopy1.index("banana") # Returning index of searching element
listcopy1.sort() # Sorts element of list based on their ASCII value 
print(listcopy1)
print(len(listcopy2)) # Prints number of element in the list
listcopy2.reverse() # Reversing the order of list element 
print(listcopy2) 

for x in cars : # Printing all element of cars list
    print(x)

if "orange" in listcopy1 : # Checking if orange is in listcopy1
    print("orange байна")
else :
    print("orange байхгүй")