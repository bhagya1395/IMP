class Student:
    def __init__(self):
        self.name='durga'
        self.age=40
        self.marks=80

    def talk(self):
        print("Hello I am:",self.name)
        print("My Age is:", self.age)
        print("My Marks are:", self.marks)
t=Student()
t.talk()
#
# class Student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#
#     def talk(self):
#         print("Hello I am:",self.name)
#         print("My Age is:", self.age)
#         print("My Marks are:", self.marks)
# t=Student('bhagya',10,40)
# t.talk()



#
# class Student:
#     def __init__(self,x,y,z):
#         self.name=x
#         self.age=y
#         self.marks=z
#
#     def talk(self):
#         print("Hello I am:",self.name)
#         print("My Age is:", self.age)
#         print("My Marks are:", self.marks)
# t=Student('bhagya',10,40)
# t1=Student('pratiksha',15,70)
# t.talk()
# t1.talk()

#Instance Variable: if the value of variable is varied from object to object
#for every object a separate copy of instance variables will be created.

#Inside Constructor by using self variable:

# class Employee:
#     def __init__(self):
#         self.name='durga'
#         self.age=10
# e=Employee()
# print(e.__dict__)

# #Inside Instance Method by using self variable:
#
# class Employee:
#     def __init__(self):
#         self.a=10
#         self.b=20
#
#     def m1(self):
#         self.c=30
#
# e=Employee()
# e.m1()
# print(e.__dict__)
#
#
# #Outside of  the class by using object reference variable:
# class Employee:
#     def __init__(self):
#         self.a=10
#         self.b=20
#
#     def m1(self):
#         self.c=30
#
# e=Employee()
# e.m1()
# e.d=40
# print(e.__dict__)

# class Employee:
#     def __init__(self):
#         self.a=10
#         self.b=20
#
#     def m1(self):
#         print(self.a)
#         print(self.b)
#
# e=Employee()
# e.m1()
# print(e.a,e.b)
#
# #INHERITANCE:
# class A:
#     def m1(self):
#         print("hello")
# class B:
#     def m2(self):
#         print("good morning")
# class C(A,B):
#     def m3(self):
#         print("hii")
#
# c=C()
# c.m1()
# c.m2()
# c.m3()


class Test:
    def __init__(self):
        print("Constructor Execution.....")
    def m1(self):
        print("Method Execution......")
t1= Test()
t1=Test()
t1.m1()


class Student:
    def __init__(self,x,y,z):
        self.name=x
        self.age=y
        self.rollno=z
    def display(self):
        print("student name:{}\n age:{}\n rollno:{}".format(self.name,self.age,self.rollno))

s1=Student('bhagya',27,1)
s1.display()

class Emp:
    def __init__(self):
        self.ename="bhagya"
        self.eno=12
        self.esalary=10000
e=Emp()
print(e.__dict__)



class Emp:
    def __init__(self):
        self.ename="bhagya"
        self.eno=12
        self.esalary=10000

    def m1(self):
        self.eaddr="pune"
e=Emp()
e.m1()
print(e.__dict__)



class Emp:
    def __init__(self):
        self.ename="bhagya"
        self.eno=12
        self.esalary=10000

    def m1(self):
        self.eaddr="pune"
e=Emp()
e.m1()
e.d=40
print(e.__dict__)


#Passing members of one class to another class

class Student:
    def __init__(self,n,r):
        self.name=n
        self.rollno=r
    def disp(self):
        print("Student name:",self.name)
        print("Student rollno:", self.rollno)

class User:
    @staticmethod
    def show(s):
        print("User Name:",s.name)
        print("User Rollno:",s.rollno)
        s.disp()
stu=Student("Bhagya",101)
User.show(stu)

# NESTED CLASS
class Army:
    def __init__(self):
        self.name="Rahul"
        self.gn=self.Gun()
    def show(self):
        print("Army Name:",self.name)

    class Gun:
        def __init__(self):
            self.name="AK47"
            self.capacity='75 Rounds'
            self.length='34.4 in'
        def disp(self):
            print(self.name)
            print(self.capacity)
            print(self.length)
a=Army()
print(a.name)
a.show()

print(a.gn.name)
# g=a.gn
g=Army().Gun()
print(g.name)
print(g.capacity)
print(g.length)
g.disp()


#SINGLE INHERITANCE

class Father:
    money=1000
    def show(self):
        print('Parent class of instance method')
    @classmethod
    def showmoney(cls):
        print("parent class of class method ",cls.money)
    @staticmethod
    def stat():
        a=10
        print("parent class static method",a)
class Son(Father):
    def disp(self):
        print("Child class instance method")
s=Son()
s.disp()
s.show()
s.showmoney()
s.stat()
print()

#CONSTRUCTOR IN INHERITANCE:
class Father:
    def __init__(self):
        self.money=1000
        print("Father class constructor")
    def show(self):
        print("Father class instance method")
class Son(Father):
    def disp(self):
        print("Son class instance method:",self.money)
s=Son()
s.disp()
s.show()
print(s.money)
print()

class Father:
    def __init__(self,m):
        self.money=m
        print("Father class constructor")
    def show(self):
        print("Father class instance method")
class Son(Father):
    def disp(self):
        print("Son class instance method:",self.money+1000)
s=Son(2000)
s.disp()
s.show()
print(s.money)
print()

#CONSTRUCTOR OVERRIDING:
class Father:
    def __init__(self):
        self.money=1000
        self.car='MARUTI SUZUKI'
        print("Father class constructor")
    def show(self):
        print("Parent class instance method")
class Son(Father):
    def __init__(self):
        self.money=5000
        self.car='BMW'
        print("child class constructor")
    def disp(self):
        print("child class instance method")
s=Son()
print(s.money)
print(s.car)
s.disp()
s.show()
print()

#CONSTRUCTOR USING SUPER() METHOD
class Father:
    def __init__(self,m,r):
        self.money=m
        self.car=r
        print("Father class constructor")
    def show(self):
        print("Parent class instance method")
class Son(Father):
    def __init__(self,m,r,m1,r1):
        super().__init__(m,r)    #..............calling parent class constructor
        self.money1=m1
        self.car1=r1
        print("child class constructor")
    def disp(self):
        print("child class instance method",self.money,self.car,   "son constructor:",self.money1,self.car1)
s=Son(1000,'Maruti suzuki',5000,'Maruti Suzuki')
print(s.money)
print(s.car)
s.disp()
s.show()
print()

#MULTI-LEVEL INHERITANCE

class Father:
    def __init__(self):
        print("Father class constructor")
    def showF(self):
        print("Father class method")
class Son(Father):
    def __init__(self):
        super().__init__()    #.......calling father class construtor
        print("SON class constructor")
    def showS(self):
        print("Son class method")
class Grandson(Son):
    def __init__(self):
        super().__init__()     #......calling son class constructor
        print("Grandson class constructor")
    def showG(self):
        print("Grandson class method")
s=Grandson()
s.showF()
s.showG()
s.showS()
print()

#HIERARCHICAL INHERITANCE
class Father:
    def __init__(self):
        print("Father class constructor")
    def showF(self):
        print("Father class method")
class Son(Father):
    def __init__(self):
        print("Son class constructor")
    def showS(self):
        print("Son class method")
class Daughter(Father):
    def __init__(self):
        print("Daughter class constructor")
    def showD(self):
        print("Daughter class method")

s=Son()
s.showF()
s.showS()
s1=Daughter()
s1.showF()
s1.showD()
print()

# MULTIPLE INHERITANCE  &&&& MRO-Method Resolution Order
class Father:
    def __init__(self):
        super().__init__()  # ..........calling parent class constructor
        print("Father class constructor")
    def showF(self):
        print("instance method of Father class")
class Mother:
    def __init__(self):
        super().__init__()  # ..........calling parent class constructor
        print("Mother class constructor")
    def showM(self):
        print("Mother class instance method")
class Son(Father,Mother):
    def __init__(self):
        super().__init__()    # ..........calling parent class constructor
        print("Son class constructor")
    def showS(self):
        print("Son class instance method")
s=Son()
s.showF()
s.showM()
s.showS()
print()

#DUCK TYPING:
class Duck:
    def walk(self):
        print("thapak thapak thapak thapak")
class Horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak")
class Cat:
    def talk(self):
        print("Meow Meow Meow Meow")
def myfunction(obj):
    obj.walk()

# d=Duck()
# myfunction(d)

# c=Cat()
# myfunction(c)


#STRONG TYPING
class Duck:
    def walk(self):
        print("thapak thapak thapak thapak")
class Horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak")
class Cat:
    def talk(self):
        print("Meow Meow Meow Meow")
def myfunction(obj):
    if hasattr(obj,'walk'):
        obj.walk()
    if hasattr(obj,'talk'):
        obj.talk()

d=Duck()
myfunction(d)

h=Horse()
myfunction(h)

c=Cat()
myfunction(c)
print()

#METHOD OVERLOADING
class Myclass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            print("provide atleast two numbers")
        return s
obj=Myclass()
print(obj.sum(10,20))
print()

class Add:
    def result(self,x,y):
        print("the Addition is:",x+y)
class Multi(Add):
    def result(self,a,b):
        super().result(10,20)     #....calling parent class method
        print("the multiplication is:",a*b)
s=Multi()
#s.result(10,20)




class Bank:
    bank_name='BOI'
    rate_of_interest=12.25
    @staticmethod
    def simple_int(prin,n):
        si=(prin*n*Bank.rate_of_interest)/100
        print(si)

Bank.simple_int(10000,3)



class Abhi:
    def __init__(self,nm,ag):
        self.name = nm
        self.age = ag
    def display(self):
        print("name is",self.name ,"& age is",self.age)


a1=Abhi('Abhi',28)
a2=Abhi('Aashu',29)
print(a1.age)
a1.age=29
print(a1.age)
a1.display()
print(getattr(a1,'age'))
setattr(a1,'name','shubham' )
print(a1.__dict__)
print(a2.__dict__)
delattr(a2,'age')
print(a2.__dict__)
print(hasattr(a1,'age'))
print(Abhi.__dict__)
print(Abhi.__doc__)
print(Abhi.__name__)
print(Abhi.__module__)


class Abhi:
    def __init__(self,nm,ag):
        self.name = nm
        self.age = ag
    def display(self):
        print("name is",self.name ,"& age is",self.age)


a1=Abhi('Abhi',28)
a2=Abhi('Aashu',29)
a1.marks=100
print(a1.__dict__)
print(a2.__dict__)
del a2.age
print(a2.__dict__)


class Employee:
    company='Infosys'
    def __init__(self,nm,ag):
        self.name=nm
        self.age=ag

    def display(self):
        print("Employee name is",self.name,"& age is",self.age)

e1=Employee('shubham',28)
e1.display()
print(Employee.company)
print(e1.company)
Employee.company="TCS"
print(Employee.company)


class Employee:
    company='Infosys'
    def __init__(self,nm,ag):
        self.name=nm
        self.age=ag
    @classmethod
    def get_company(cls):
        print(cls.company)
e1=Employee('shubham',28)
Employee.get_company()

class Bank:
    bank_name='SBI'
    rate_of_interest=12.25
    @staticmethod
    def simple_interest(prin,n):
        si=(prin*n*Bank.rate_of_interest)/100
        print(si)

Bank.simple_interest(10000,2)


n1=10
n2=20
print(n1+n2)
print(n1.__add__(n2))
print(int.__add__(n1,n2))


class Decorator(object):
    def __init__(self,func):
        self.function=func


    def __call__(self, a,b):
        result=self.function(a,b)
        return result**2
        #original func
        #square

@Decorator
def add(a,b):
    return a+b

#add=Decorator(add)
print(add(1,2))               #add.__call__(a,b)


nums=[12,2,3,4,5,6,6]
sq=[]
for n in nums:
    sq.append(n*n)
print(sq)


l=[n*n for n in range(1,11) if n%2==0 if n%3==0]
print(l)


l=[n*n if n%2==0 else n*n*n for n in range(1,11)]
print(l)

print([i*j for i in range(3,6) for j in range(5,7)])

num=[10,20,-3,-56,-6,8,9,30,20,0,-1,0]
l1=['positive' if n>0 else 'negative' if n <0 else 'zero' for n in num]
print(l1)


d1={n:n*n for n in range(1,6) if n %2==0}
print(d1)

l=['Even' if n%2==0 else 'Odd' for n in range(1,11)]
print(l)

import pickle
data=[12,'bhagya',34,'shubh']
f=open("xyz3.txt",'wb')
pickle.dump(data,f)
f.close()


import pickle
data=[12,'bhagya',34,'shubh']
f=open("xyz3.txt",'rb')
data1=pickle.load(f)
print(data1)
f.close()


import pickle
data=[1,2,3,4,5]
data1=pickle.dumps(data)
print(data1)
print(pickle.loads(data1))

# l1 = [125 / 234 , 345 / 566 , 5656 / 9485645, 'dfgd', '&', 9898 & 23090 , 7823]
# # output = [125,234,345,566,5656,9485645,9898,23090,7823]
# for x in l1:
#     y=x.replace('/',',')
#     print(y)


s=['bhagya@awatade','viyansh@awatade']
for x in s:
    y=x.split('@')
    for i in y:
        print(y)


num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)

