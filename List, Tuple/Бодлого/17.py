# Сурагчдын тоон үнэлгээний жагсаалт өгөгдсөн бол 89-өөс их бол А,
# 79-өөс их В, 69-өөс их бол С, 59-өөс их бол D бусад тохиолдолд F үсгэн дүнг хэвлэ.
grade_list = input().split()
for grade in grade_list :
    if int(grade) > 89 :
        print(f"{grade} is A")
    elif int(grade) > 79 :
        print(f"{grade} is B")
    elif int(grade) > 69 :
        print(f"{grade} is C")
    elif int(grade) > 59 :
        print(f"{grade} is D")
    else :
        print(f"{grade} is F")