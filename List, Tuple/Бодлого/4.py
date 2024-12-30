#Нэрсийн дарааллаас хамгийн урт нэрийг ол. 
print(max(input().split(), key=len))


#Traditional way without using max function 
ners = input().split()
urt_ner = ners[0]
for ner in ners :
    if len(ner) > len(urt_ner) :
        urt_ner = ner
print(urt_ner)