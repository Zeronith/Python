#Болд шинэ ажилтан бүртгэж байв. Гэтэл бүртгүүлсэн хүмүүс дахиж бүртгүүлж түүнд асуудал үүсгэв. 
#Давхардсан нэрсийг устгах программ бичиж түүнд туслацгаая.
counter=0
new_employees = input().split()
for i in range (0 , len(new_employees)) :
    for j in range (i+1 , len(new_employees)) :
        if(j<len(new_employees) and new_employees[i]==new_employees[j]) :
            del new_employees[j] 
print(new_employees)
            