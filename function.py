def wish():
    print('hello good morning')
wish()
wish()

def wish(name):
    print("hello",name,"Good Morning")
wish('durga')
wish('komal')

def squareit(number):
    print("the Square of",number,"is",number*number)
squareit(4)

def add(x,y):
    return x+y

result=add(10,20)
print(result)
print(add(10,29))

def even_odd(num):
    if num%2==0:
        print("the",num,"is even number")
    else:
        print("the", num, "is odd number")
even_odd(10)
even_odd(11)

def fact(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result
for i in range(1,5):
    print("The factorial of",i,"is:",fact(i))


def fact(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result
for i in range(1,5):
    print("the factorial of given",i,"is:",fact(i))

def sum_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
x,y =sum_sub(100,50)
print('the sum is:',x)
print('the substraction is:',y)

def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
t=calc(100,50)
print("the results are")
for i in t:
    print(i)

def sum(*n):
    total=0
    for n1 in n:
        total=total+ n1
    print("The sum=",total)

sum()
sum(10)
sum(10,20)
sum(10,20,30)

def display(**kwargs):
    for k,v in kwargs.items():
        print(k," : ",v)
display(n1=10,n2=20,n3=40)
#
# a=10
# def f1():
#     print(a)
# def f2():
#     print(a)
# f1()
# f2()

# def f1():
#     a=10
#     print(a)
# def f2():
#     print(a)
# f1()
# f2()

# a=10
# def f1():
#     global a
#     a=777
#     print(a)
# def f2():
#     print(a)
# f1()
# f2()

# def f1():
#     global a
#     a=10
#     print(a)
# def f2():
#     print(a)
#
# f1()
# f2()
#
# a=10
# def f1():
#     a=777
#     print(a)
#     print(globals()['a'])
# f1()


# def factorial(n):
#     if n==0:
#         result=1
#     else:
#         result=n*factorial(n-1)
#     return result
# print(factorial(4))
#
#
# l=[1,3,5,7,8]
# l1=[3,3,4,5,7]
# l2=list(map(lambda x,y:x*y,l,l1))
# print(l2)
#
#
# from functools import*
# l=[2,3,4,5,6]
# result=reduce(lambda x,y:x+y,l)
# print(result)
#
# s=input('Enter some string:')
# output=' '
# for ch in s:
#     if ch.isalpha():
#         x=ch
#     else:
#         d=int(ch)
#         output=output+x*d
# print(output)
#
# s='aaaabbbcc'
# previous=s[0]
# output=' '
# c=1
# i=1
# while i<len(s):
#     if s[i]==previous:
#         c=c+1
#     else:
#         output=output + str(c)+previous
#         previous=s[i]
#         c=1
#     if i==len(s)-1:
#         output=output+str(c)+previous
#     i=i+1
#     print(output)

# print(ord('a'))
#
# s='D33j7k3h3'
# output=" "
# for ch in s:
#     if ch.isalpha():
#         output=output+ch
#         x=ch
#     else:
#         d=int(ch)
#         newc=chr(ord(x)+d)
#         output=output +newc
# print(output)
#
#
# string1 = 'Aj44Ek2U2J'
# list1 = []
# digit_string = ''
# latest_char = None
#
# for ele in string1:
#     if ele.isalpha():
#         if digit_string:
#             def next_char(latest_character, int_string):
#                 ord_latest = ord(latest_character)
#                 ord_sum = ord_latest + int(int_string)
#                 if ord_sum > ord('Z'):
#                     ord_diff = ord_sum - ord('Z')
#                     ord_reminder = ord_diff % 26
#                     next_character = chr((ord('A') - 1) + ord_reminder)
#
#                     return next_character
#                 else:
#                     ord_latest = ord(latest_character)
#                     ord_sum = ord_latest + int(int_string)
#                     next_character = chr(ord_sum)
#                     return next_character
#             next_char = next_char(latest_char, digit_string)
#             list1.append(next_char)
#             digit_string = ''
#         latest_char = ele
#         list1.append(latest_char)
#
#     elif ele.isdigit():
#         digit_string += ele
#
# output = ''.join(list1)
# print(output)
#
#
#
# s='AAABBBBBBCCCCDDDDASDFGJYHTREWSD'
# output=''
# for ch in s:
#      if ch not in output:
#          output=output +ch
# print(output)
#
# l='ABACDDEEF'
# l1=[]
# for ch in l:
#     if ch not in l1:
#         l1.append(ch)
# print("".join(l1))

# s=input("enter some string:")
# l=[]
# for ch in s:
#     if ch not in l:
#         l.append(ch)
# for ch in l:
#     print('{} occurs {} times'.format(ch,s.count(ch)))
#
#
#
# s=input("enter some string:")
# l=[]
# for ch in s:
#     if ch not in l:
#         l.append(ch)
# for ch in sorted(l):
# #     print('{} occurs {} times'.format(ch,s.count(ch)))
#
# s='ABABABCBD'
# l=set(s)
# for ch in l:
#     print('{} occurs {} times'.format(ch, s.count(ch)))
#
# from functools import*
# l=[1,2,3,4,5]
# s=reduce(lambda x,y:x*y,l)
# print(s)
#
# l1=[1,2,3,4]
# l=list(map(lambda x:x**2,l))
# print(l)
#
# l=list(filter(lambda x:x%2==0,range(11)))
# print(l)

# def decor(func):
#     def inner():
#         func()     #existing functionality
#         #add new functionality
#         print("welcome")
#     return inner
# @decor
# def printer():
#     print("welcome")
#     print("welcome")
#
# printer()
# # a=decor(printer)
# # a()
#
# def decor(addition):
#     def inner():
#         result=addition()
#         num3=float(input("Enter third number:"))
#         result=result+num3
#         return result
#     return inner
# @decor
# def addition():
#     num1=float(input("Enter first number:"))
#     num2=float(input("Enter second number:"))
#     result=num1+num2
#     return result
# print(addition())
# addition=decor(addition)
# print(addition())

# def decor1(func):
#     def inner():
#         return func().upper()
#     return inner
# def decor2(func):
#     def inner():
#         return func().split()
#     return inner
# @decor2
# @decor1
# def get_name():
#     name=input("Enter first name:")
#     sirname=input("enter sirname:")
#     full_name=name+" "+sirname
#     return full_name
#
# print(get_name())
# #
# # a=decor2(decor1(get_name))
# # print(a())

def decor(func):
    def inner(*args):
        for num in args[1:]:
            if num==0:
                return "cannot divide by zero"
        return func(*args)
    return inner

@decor
def div1(a,b):
    return a/b

@decor
def div2(a,b,c):
    return a/b/c

print(div1(10,2))
print(div2(10,0,2))
print(div2(10,2,2))
print(div1(0,2))
print(div2(100,50,2))