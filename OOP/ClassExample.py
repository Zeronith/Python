class Employee :
    empCount = 0
    def __init__(self, name , salary):
        self.name = name 
        self.salary = salary
        Employee.empCount+=1
    
    def displayCount(self) :
        print(f"Total Employee {Employee.empCount}" ) 
    
    def displayEmployee(self) :
        print(f"Name : {self.name} , Salary : {self.salary} ")

emp1 = Employee ("Enguunee", 500000000)
emp2 = Employee ("Batzolboo",  500000000)


print(emp1.displayCount())