# Класс нь өгөгдөл болон функцуудаас тогтох өгөгдлийн хийсвэр төрөл юм . 
# Бидний өмнө үзсэн цуглуулга төрөлтэй төстэй боловч өгөгдөлд хандах хандалт нь ялгаатай байдгаараа онцлог юм
# Цуглуулга өгөгдлийн талбар нь хандах эрх нээлттэй байдаг бол классын талбарт хандах эрхийг хязгаарлаж болдог 
# Үүнийг өгөгдөл далдлалт ба битүүмжлэл гэдэг 


# Класс тодорхойлох  MyClass гэсэн нэтэй классыг x = 5 бүхий гишүүн өгөгдөлтэй
# тодорхойлж классын p1 объектоор дамжуулж гишүүн өгөгдлийн утгийг хэвлэж байна 


class MyClass : # Класс зарлах 
    x = 5       # Гишүүн өгөгдөл  
p1 = MyClass()  # Классын объект зарлах 
print(p1.x)

# Байгуулагч функц Pythoлд классын байгуулагч функцийн init() гэж тодорхойлсон байдаг 
# Шинэ объект үүсгэхэд класс ашиглагдах үед байгуулагч функц автоматаар ажилладаг .
# Байгуулагч функц нь классын гишүүн өгөгдөлд анхны утга оноох болон санах ой хувиарлах үүрэгтэй 

class Person : 
    def __init__(self, name , age ): # Constructor function 
       self.name = name 
       self.age = age 
       
p1 = Person ("John" , 36) # Creating object with help of constructor function 

print(p1.name, p1.age)



# Self paramemer нь тухайн классын өгөгдөлт хандахад ашиглагддаг . 
# Энэ нь заавал  Self нэртэй байх албагүй ба классын аль ч функцийн эхний параметр байх ёстой

class Human :
    def __init__(self, gender , age ):
        self.gender = gender
        self.age = age 
    def introd(obj) : 
        print(f"Hello , i am human . im {obj.age} years old and my gender is {obj.gender}")
p1 = Human ("Male" , 20) 
p1.introd()



class Ninja :
    def __init__(self, age , gender , experience):
         self.age = age
         self.gender = gender
         self.experience = experience
    def printinfo(self) :
        print(f"Hello , I am ninja and this is my introduction , im {self.age} year old , and  i am {self.gender} , also i have almost {self.experience}")
enguunee = Ninja(19 , "Male", 19)
enguunee.printinfo()

enguunee.age = 20 # Changing member variable
enguunee.printinfo()

# del enguunee.gender # Deletes member variable 
# print(enguunee.gender) # Cause error cause gender member is already deleted
# enguunee.printinfo() # It will also cause error cause printinfo also uses gender

del enguunee # deletes object
print(enguunee)
