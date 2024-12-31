txt = "сайн уу"
x = txt.capitalize()
print (x) 

txt = "Сайн Байна уу!"
x = txt.casefold() # for UNICODE 
y = txt.lower() # for english   
print (x)

txt = "hello enguunbayar baina "
print(txt.upper()) 


txt = "enguunbayar"
x = txt.center(20 , "\n")
print(x)


txt = "Сайн байна уу . Намайг Энгүүнбаяр гэдэг юм байна "
x = txt.count("байна")
print(x)


txt = "Сайн уу, хичээлд тавтай морил."
x = txt.find("хичээл")
print(x)


txt = "Зөвхөн {үнэ:.2f} төгрөг!"
print(txt.format(үнэ = 50))


txt = "Сайн уу, хичээлд тавтай морил."
x = txt.index("хичээл")
print(x)


txt = "50800"
x = txt.isdigit()
print(x)


txt = "hello world!"
x = txt.islower()
print(x)



txt = "565543"
x = txt.isnumeric()
print(x)



txt = "   "
x = txt.isspace()
print(x)


txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)


txt = "THIS IS NOW!"
x = txt.isupper()
print(x)


myTuple = ("Сайн", "байна", "уу")
x = "#".join(myTuple)
print(x)


txt = "50"
x = txt.zfill(10)
print(x)



txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")


txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)



txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)



txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)


txt = "welcome to the jungle"
x = txt.split()
print(x)


txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)


txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)



txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")



txt = "     banana     "
x = txt.swapcase()
print("of all fruits", x, "is my favorite")


txt = "Welcome to my world"
x = txt.title()
print(x)