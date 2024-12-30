# а аас б хүртэлх тооноос цифрүүдийн нийлбэр нь к байх тоонуудыг олох
a = int(input())
b = int(input())
k = int(input())

for i in range (a, b) :
    if k == sum(int(j) for j in str(i)) :
        print(i)
        