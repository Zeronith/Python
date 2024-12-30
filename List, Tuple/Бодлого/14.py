#Байгууллагуудын нэрсийн жагсаалт өгөгдсөн бол хамгийн урт нэртэй хүнтэй байгууллагын байрлалыг ол.
organizations = [
    ["Google", "California", ["Sundar Pichai",  "Thomas Kurian"]],
    ["Microsoft", "Washington", ["Satya Nadella", "Bill Gates","Prabhakar Raghavan", "Steve Ballmer"]],
    ["Amazon", "Seattle", ["Jeff Bezos", "Andy Jassy", "Dave Clark"]],
    ["Meta", "California", ["Mark Zuckerberg", "Sheryl Sandberg", "Andrew Bosworth"]],
    ["Tesla", "Texas", ["Elon Musk", "JB Straubel", "Gwynne Shotwell"]]
]
maximum = organizations[0][2][0]
location = organizations[0][1]
for organization in organizations :
    for workers in organization :
        for workers_name in workers :
            if len(workers_name) > len(maximum) :
                maximum = workers_name
                location = organization[1]
print(location)
print(maximum)
