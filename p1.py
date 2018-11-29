class Total:
    def __init__(self,price):
        self.price=price
    
    def __add__(self,other):
        return self.price + other.price
    
    def __mul__(self,other):
        return self.price * other.price
    
    def __gt__(self,other):
        return self.price > other.price
    
    def __lt__(self,other):
        return self.price < other.price
    
t1=Total(225)
t2=Total(200)

print("Total\t",t1+t2)
print("Multiply\t",t1*t2)
print("Greater Then\t",t1>t2)
print("Lowest number\t",t1<t2)

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def __mul__(self,other):
        return self.salary * other.days

class Time:
    def __init__(self,days):
        self.days=days

e=employee("akash",1200000)
t=Time(30)

print("Salary=> ",e*t)