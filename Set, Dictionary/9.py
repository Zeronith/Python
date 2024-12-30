# машингүй хүн хэд байна вэ
import data 
counter = 0
people = data.persons
for person in people :
    if len(person["mashinuud"])==0 :
        counter+=1
print(counter)