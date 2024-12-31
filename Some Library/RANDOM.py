import random

# Жигд тархалттай (Uniformly Distributed) бутархай тоо үүсгэх 
print(random.uniform(20,60))

# 0-ээс 1 хооронд санамсаргүй бутархай тоо үүсгэх 
print(random.random()) 

# List дотроос санамсаргүй элементийн тоогоор санамсаргүй дарааллаар жагсаалт үүсгэх
mylist = ["apple", "banana", "cherry"]
print(random.sample(mylist, k=2))

# Shuffling the element of list 
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)

# Random element choose from list
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))