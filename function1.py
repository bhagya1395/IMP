 #function ==> function is a block of code which only runs when it is called.
#advantage -code reuseability


def wish():
    print("hello good morning")
wish()
wish()

def wish(name):
    print("hello",name,"Good Morning")
wish('Bhagya')

def squareit(num):
    print("the square of",num,"is:",num*num)
squareit(4)

#return statement: it is special statement that you can use inside a function or method to send the function's result bact to the caller

def add(x,y):
    return x+y
result=add(10,20)
print("The sum is:",result)
print("The sum is:",add(100,300))

#if we are not writing the return statement then default value is None.

def even_odd(num):
    if num%2==0:
        print("Given num is even")
    else:
        print("Given num is odd")
even_odd(5)


def fact(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result
for i in range(1,6):
    print("The factorial of",i,"is",fact(i))

#in other language function can return atmost one value
#But in python function can return any number of values

def sum_sub(x,y):
    sum=x+y
    sub=x-y
    return sum,sub
a,b=sum_sub(100,20)
print("the sum is:",a)
print("The sub is:",b)

def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
t=calc(100,50)
print("The results are:")
for i in t:
    print(i)


#Types of arguments:
#1==>positional arguments--the no of arguments & position of arguments must be matched. If ew change the order then result may be changed

def sub(a,b):
    return a-b
print("the sub is:", sub(20,10))

#2==>keyword arguments--order of arguments is not important but number of arguments must be matched.
def wish(name,msg):
    print('hello',name,msg)
wish("bhagya","good morning")
wish(msg="good morning",name="bhagya")
wish("bhagya",msg="how r u")

#3==>default arguments--sometimes we can provide default values for oour positional arguments.
#if we are not passing any value then only default value will be considered
def wish(name="Guest"):
    print("Hello",name,"Good Morning")
wish("shubh")
wish()

#4==>Variable length arguments--sometimes we can pass varibale number of arguments to our function,such type of arguments are
#called variable length arguments.declare using * symbol
#we can call this function by passing any number of arguments including zero number.internally all these values represented
#in the form of tuple
def sum(*n):
    total=0
    for n1 in n:
        total =total +n1
        print("The Sum=",total)
sum()
sum(10)
sum(10,20,30)
sum(10,20,30,40)

def f1(n1,*s):
    print(n1)
    for s1 in s:
        print(s1)
f1(10)
f1(20,40,'A','B')

#we can declare keyword variable length arguments also
#we have to use **
#we can call this function by passing any number of keyword arguments.Internally these keyword arguments will be stored
#inside a dictionary.

def display(**kwargs):
    for k,v in kwargs.items():
        print(k,"=",v)
display(n1=10,n2=20,n3=30)
display(rno=100,name="durga",marks=70,subject="java")

#Types of Variables:
#1. Global variable==> The variable which are declared outside of function are called global variables.
#These variables can be accessed in all functions of that module.
# a=10 #global variable
# def f1():
#     print(a)
# def f2():
#     print(a)
# f1()
# f2()
#2. Local Variable==> The variables which are declared inside a function are called local varibles.
#Local variables are available only for the function in which we declared it.i.e from outside of function we cannot access.
# def f1():
#     p=10
#     print(p)
# def f2():
#     print(p)
# f1()
# f2()

#global keyword:
# to declare global variable inside function
# to make global variable available to the function so that we can perform required modifications.
c=10
def f1():
    c=777
    print(c)
def f2():
    print(c)
f1()
f2()

a=10
def f1():
    global a
    a=777
    print(a)

def f2():
    print(a)
f1()
f2()

def f1():
    global a
    a=20
    print(a)

def f2():
    print(a)
f1()
f2()


#If global variable and local variable having the same name then we can access global variable inside a function as follows
# a=10
# def f1():
#     a=999
#     print(a)
#     print(globals()['a'])
# f1()

# e='butter'
# def f(a):
#     print(a)+e
# f('bitter')
#Recursive Functions==>A function that calls itself  is known as recursive function.
#main advantages- we can reduce length of the code and improves readability & we can solve complex problems very easily.
def fact(n):
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return result
print("Factorial of 4 is:",fact(4))
print("Factorial of 5 is:",fact(5))

#Anonymous Function: we can declare a function without any name,such type of nameless functions are called anonymous functions or lambda function.
#lambda function:
# syntax ==> lambda argument_list:expression
#by using lambda functions we can write very concise code so that readability of the pgm will be improved.
s=lambda x:x*x
print("The square of 4 is:",s(4))

s=lambda x,y:x+y
print(s(10,20))

s=lambda a,b:a if a>b else b
print(s(10,50))

#lambda function internally returns expression value and we are not required to write return statement explicitly.
#we can pass function as argument to another function. in such cases lambda functions are best choice.

# Filter() Function:==>to filter values from the given sequesnce based on some condition
# filter(function,sequence)
def isEven(x):
    if x%2==0:
        return True
    else:
        return False
l=[10,3,4,2,5,6]
l1=list(filter(isEven,l))
print(l1)

l1=list(filter(lambda x:x%2!=0,l))
print(l1)

# Map() function==>The function can be applied on each element of sequence and generates new sequence.
#map(function,sequence)
def squareit(x):
    return x*x
l=[1,2,3,45,5]
l1=list(map(squareit,l))
print(l1)

l1=list(map(lambda x:x*x,l))
print(l1)

l2=[1,2,3,4]
l3=[5,6,7,4]
n=list(map(lambda x,y:x+y,l2,l3))
print(n)

# Reduce() function==>reduce() function reduces sequence of elements into a single element by applying the specified function.
#reduce(function,sequence)

from functools import*
l=[10,20,30,40]
result=reduce(lambda x,y:x+y,l)
print(result)

from functools import*
l=[10,20,30,40]
result=reduce(lambda x,y:x*y,l)
print(result)

from functools import*
l=reduce(lambda x,y:x+y,range(1,100))
print(l)

#Function Aliasing==> For the existing function we can give another name,which is nothing but function aliasing.
def wish(name):
    print("good morning",name)
greeting=wish
greeting('Bhagya')
wish('Bhagya')

def wish(name):
    print("good morning",name)
greeting=wish
greeting('Pawan')
wish('Durga')
del wish
#wish('saarthi')
greeting('saarthi')


def outer():
    print("outer function started")
    def inner():
        print("inner function execution")
    print("outer function returning inner function")
    return inner
f1=outer()
f1()
f1()
f1()

#Function Decorators:Decorator is a function which can take a function as argument and extend its functionaliy and returns
# modified function with extended functionality.
# main objective of decorator  functions is we can extend the functionality of existing functions without modifies that function.
def decor(func):
    def inner(name):
        if name=="sunny":
            print("Hello sunny bad morning")
        else:
            func(name)
    return inner
@decor
def wish(name):
    print("Hello",name,"Good Morning")

wish("bhagya")
wish("sunny")

def decor(func):
    def inner(name):
        if name=='sunny':
            print("hello sunny Bad Morning")
        else:
            func(name)
    return inner

def wish(name):
    print("Hello",name,"Good Morning")

decorfunction=decor(wish)
wish("durga")
wish("sunny")
decorfunction("durga")
decorfunction("sunny")

def smart_division(func):
    def inner(a,b):
        print("we are dividing",a,"with",b)
    if b==0:
        print("OOPS....cannot divide")
    else:
        return func(a,b)
    return inner
@smart_division
def division(a,b):
    return a/b
print(division(20,2))
print(division(20,0))

#Decorator Chaining:
#we can define multiple decorators for the same function & all these decorators will form Decorator Chaining.
def decor1(func):
    def inner():
        x=func()
        return x*x
    return inner
def decor(func):
    def inner():
        x=func()
        return 2*x
    return inner

@decor1
@decor
def num():
    return 10
print(num())