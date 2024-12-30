# 20-оос дээш насны хэдэн хүн байгааг тоол.
import data 
counter = 0
humuus = data.persons
for hun in humuus :
    if hun["nas"]>20 :
        counter+=1
print(counter)