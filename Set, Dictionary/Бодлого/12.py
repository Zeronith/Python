# насанд хүрээгүй хүн хэд байна вэ
import data 
counter = 0
people = data.persons 
for person in people :
    if person["nas"] < 18 :
        counter+=1
print(counter)