s=0
for i in range(100, 1000) :
    ii=i
    while int(ii)!=0 :
        s=s*10+int(ii)%10
        ii=int(ii)//10
    if(s==i) :
        print(i)
    s=0