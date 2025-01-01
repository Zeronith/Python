'''
Гурван бүхэл тоо бүхий гишүүн өгөгдөлтэй класс үүсгэн дараах гишүүн функцуудыг тодорхойлно уу

1.гурвалжны гурван талыг хэвлэх
2.гурвалжин мөн эсэхийг шалгах
3.гурвалжны хурц, мохоо, тэгш өгцөгт эсэхийг олох
4.гурвалжны пиреметр олох
5.гурвалжны талбай олох


Тоон дараалал бүхий гишүүн өгөгдөлтэй класс үүсгэн дараах гишүүн функцуудыг тодорхойлно уу
1.их элемент олох
2.бага элемент олох
3.элементүүдийн нийлбэр олох
4.k аас их элементүүдийг тоог олох
5.k аас бага элементүүдийг тоог олох
6.k аас их элементүүдийг p ээр солих
7.дундаж утга олох
8.дарааллыг эрэмбэлэх
9.урвуу эрэмбэ
10өсөх дэд дараалал олох
'''
import math
import random
class three :
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def print_side(self) :
        print(f"1st side {self.side1}, 2nd side {self.side2}, 3rd side {self.side3}")
    def check_tri (self) :
        if self.side1 + self.side2 > self.side3 and  self.side3 + self.side1 > self.side2 and self.side2 + self.side3 > self.side1 :
            return True
        else :
            return False
    def define_tri (self) :
        if self.side1**2 +self.side2 **2 ==self.side3**2 :
            print("Right triangle ")
        elif self.side1**2 + self.side2**2 < self.side3 **2 :
            print("Acute triangle")
        else :
            print("Obtuse triangle")
    def area(self) :
        p = (self.side1 + self.side2 +self.side3)/2
        return  math.sqrt(p*(p-self.side1)*(p-self.side2)*(p-self.side3))
    def perimeter(self) :
        return self.side1+self.side2+self.side3
        

class numbers :
    def __init__(self):
        self.mylist = []
        for i in range (0,10) :
            self.mylist.append(random.randint(0,10))
    def bubble_sort(self) :
        for i in range(len(self.mylist)) :
            for j in range(len(self.mylist)-i-1) :
                if self.mylist[j] > self.mylist[j+1] :
                    self.mylist[j] , self.mylist[j+1] = self.mylist[j+1] , self.mylist[j]
    def maximum(self) :
        maxim = self.mylist[0]
        for number in range(1, len(self.mylist)) :
            if self.mylist[number] > maxim :
                maxim = self.mylist[number] 
        return maxim
    def minimum(self) :
        min = self.mylist[0]
        for i in range (1, len(self.mylist)) :
            if self.mylist[i] < min :
                min = self.mylist[i]
        return min
    def max_count(self, k) :
        counter = 0
        for i in range (len(self.mylist)) :
            if self.mylist[i] > k :
                counter+=1
        return counter 
    def min_count(self, k) :
        counter = 0 
        for i in range (len(self.mylist)) :
            if self.mylist[i] <= k :
                counter+=1
        return counter 
    def sum(self) :
        sum = 0
        for i in range(len(self.mylist)) :
            sum+=self.mylist[i]
        return sum
    def rep(self, k , p ) :
        for i in range(len(self.mylist)) :
           if self.mylist[i] > k :
               self.mylist.pop(i) 
               self.mylist.insert(i, p)
    def avg(self) :
        return self.sum()/len(self.mylist)    
        
zero = numbers()
print(zero.mylist)
zero.bubble_sort()
print(zero.mylist)
print(zero.maximum())
print(zero.minimum())
print(zero.max_count(5))
print(zero.min_count(5))
print(zero.sum())
print(zero.avg())
zero.rep(5, 0)
print(zero.mylist)