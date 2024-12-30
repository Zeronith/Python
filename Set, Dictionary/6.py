# 20-оос доош насны хүмүүсийн нэрсийг гарга.
import data 
counter = 0
people = data.persons 
for person in people :
    if person["nas"] < 20 :
        counter+=1
print(counter)