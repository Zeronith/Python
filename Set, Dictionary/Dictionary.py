# Dictionary is unique combination of key and value 


# Note : Element in dictionary context refers as both value and key 
# Creating Dictionary 
mydictionary = {
    "owog" : "Baldan",
    "ner" : "Saraa" ,
    "nas" : 25
}
print(mydictionary)

#Accessing dictionary element by their key 
n = mydictionary["ner"]
print(n)
m = mydictionary.get("ner")
print(m)

# For Loops 1 (Iterates through only keys and prints only keys) 
print("For Loops 1 example :") 
for info in mydictionary :
    print(info)

# For Loops 2 (Iterates through only keys but prints value by accessing by their key )
print("For Loops 2 example :") 
for info in mydictionary :
    print(mydictionary[info])

# For Loops 3 (Iterates through value and prints value)
print("For Loops 3 example :")
for info in mydictionary.values() :
    print(info)
    
# For Loops 4 (Iterates through key and value both with help of items() function )
print("For Loops 4 example :") 
for info in mydictionary.items() :
    print(info)

# If condition 
if "ner" in mydictionary :
    print("There is ner key in dictionary")

# Adding element in dictionary 
Хүн = {
    "Нэр" : "Энгүүнбаяр" ,
    "Овог" : "Ганзориг",
    "Нас" : "19"
}
Хүн["Хүйс"] = "Эрэгтэй" # Just access to the dictionary by key that doesnt have and it looks like it creates new key and value automatically 
print(Хүн)

# Deleting element from dictionary 
Хүн.pop("Хүйс") # i dont know seems like both pop and del does their own job haha
print(Хүн)
del Хүн["Нас"] # After little bit of research its same as the set which raises KeyError when deleting key isnt in dictionary 
# del is just chill guy you know , and pop is pretty responsible and always reports about what the hell happened but kind of annoying guy hha 
print(Хүн)


# Deleting all element of dictionary 
Хүн.clear()
print(Хүн)

# Copying dictionary to another dictionary 
Энгүүнбаяр = Хүн.copy() # currently Хүн dictionary havent got any element 
print(Энгүүнбаяр)

# Байгуулагч ашиглан үүсгэх (I dunno about context of it so i dont know how to translate it to english)
н = dict(Хүн)  # it looks like the constructor he referred is keyword that defines dict i guess
# I'm not sure about it so dont take that as granted or correct , 
print(н)

# I guess this is just another way to add element using function 
машин = {
  "бренд": "Ford",
  "загвар": "Mustang",
  "он": 1964
}
машин.update({"өнгө": "цагаан"})
print(машин)



# Nested list and set and dictionary 
хүн = {
    "нэр": "Балдан",
    "овог": "Баатар",
    "хобби": {"ном","кино","унтах","дуу"},
    "найзууд": ["Баагий","Баагий","Болд","Сарнай"],
    "машинууд": [
        {
            "он" : 2008,
            "өнгө" : "цагаан",
            "загвар" : "приус"
        },
        {
            "он" : 2019,
            "өнгө" : "хар",
            "загвар" : "570"
        }
    ]
}
print(хүн)