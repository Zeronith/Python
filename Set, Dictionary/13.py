#хэдэн хүн prius машинтай вэ 
import data 
people = data.persons
counter = 0
for person in people :
    for car in person["mashinuud"] :
        if car["zagwar"] == "prius" :
            counter+=1
print(counter)