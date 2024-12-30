#Нэрсийн дарааллаас хамгийн богино нэрийг олж 'Сайн уу?' гэж соль.

list1 = input().split()
bogino_ner = list1[0]
for ner in list1 :
    if len(bogino_ner) > len(ner) :
        bogino_ner = ner
list1[list1.index(bogino_ner)]="Sainuu"
print(list1)