#bymba хэдэн машинтай вэ.
import data 
humuus = data.persons
for hun in humuus :
    if hun["ner"]== "bymba" :
        print(len(hun["mashinuud"]))
# key named mashinuud takes multiple value so it implemented using list data structure
# So i used len function to find lenght of mashinuud key 