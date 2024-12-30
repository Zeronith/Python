# найзуудын тоогоор эрэмбэлээд нэр болон найзын тоог харуул
import data
people = data.persons
for i in range(len(people)) :
    for j in range (len(people)-i-1) :
        if(len(people[j]["naizuud"])>len(people[j+1]["naizuud"])) :
            people[j] , people[j+1] = people[j+1] , people[j]
for person in people :
    print(person["ner"] , len(person["naizuud"]))