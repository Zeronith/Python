#Нэрсийн дарааллаас хамгийн урт нэрийг олж бүх үсгийг том болго.
ners = input().split()
urt_ner = ners[0]
for ner in ners :
    if(len(urt_ner) < len(ner)) :
        urt_ner = ner
print(urt_ner.upper())