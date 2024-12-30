#мэдээллийг насаар нь эрэмбэлээд нэр болон насыг харуул
import data 
people = data.persons
temp = dict
# Manual sorting (Bubble Sort)
for i in range(len(people)):
    for j in range(0, len(people) - i - 1):
        if people[j]["nas"] > people[j + 1]["nas"]:
            # Swap the two elements
            people[j], people[j + 1] = people[j + 1], people[j]

# Print the name and age of each person
for person in people:
    print(person["ner"], person["nas"])
