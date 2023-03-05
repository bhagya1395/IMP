# s=[1,2,3,4]
# l=list(map(lambda x:2*x,s))
# print(l)
#
# l=list(map(lambda x:x, 'intellipaat'))
# print(l)
#
# l1=list(map(lambda x:x,range(11)))
# print(l1)
#
# list1=[1,2,3,4,5,6,7,8]
# l=list(filter(lambda x:x%2!=0 ,list1))
# print(l)
#
# l=[1,2,3,4,5]
# l=[x for x in l if x%2==0]
# print(l)
#
# from functools import reduce
# l1=[1,2,3,4,5,6,7]
# l=reduce(lambda x,y:x+y,l1)
# print(l)
#
# l=[1,2,3,4,5]
# l1=sum([x for x in l])
# print(l1)
#
# l=[x for x in range(21) if x%2==0]
# print(l)
#
# l=[x for x in range(50) if x%2==0 if x%5==0]
# print(l)
#
# even_odd = [f"{x} is even" if x%2==0 else f"{x} is odd" for x in range(10)]
# print(even_odd)
#
# for x in range(4,7):
#     for y in range(1,11):
#         print(f"{x}*{y}={x*y}")
#
# l=[[x*y for y in range(1,11)] for x in range(4,7)]
# print(l)
#
# car={"brand":"Ford","model":"Mustang","year":1995}
# print(car.get("model"))
#
#
# car={"brand":"Ford","model":"Mustang","year":1995}
# print(car.get("car",117))
#
# car={"brand":"Ford","model":"Mustang","year":1995}
# print(car.values())
#
# car={"brand":"Ford","model":"Mustang","year":1995}
# print(car.keys())
#
# d={"brand":"Ford","model":"Mustang","year":1995}
# for v in d.values():
#     print(v)
#
# d={"brand":"Ford","model":"Mustang","year":1995}
# for k,v in d.items():
#     print(k,"--",v)
#
# d={100:"Bhagyashree",200:"Priyanka",300:"Dnyaneshwar"}
# print(d.popitem())
# print(d)
# print(sum(d.keys()))
#
# print('hello')
#
# d={100:"Bhagyashree",200:"Priyanka",300:"Dnyaneshwar"}
# print(d.pop(100 ))
# print(d)

#
# l=[[1,2,3,4,'a','b'],[6,'c',5],[7,'d'],['f','e',8]]
# list=[' '.join([str(x) for x in lst]) for lst in l]
# l1=l[0]
# a="".join(map(str,l1))
# l2=l[1]
# b="".join(map(str,l2))
# l3=l[2]
# c="".join(map(str,l3))
# l4=l[3]
# d="".join(map(str,l4))
# p=sorted(a+b+c+d)
# new_list=[]
# new_list.append(p[:6])
# new_list.append(p[6:9])
# new_list.append(p[9:11])
# new_list.append(p[11:14])
# print(new_list)
# print(type(new_list))


# l=[[1,2,3,4,'a','b'],[6,'c',5],[7,'d'],['f','e',8]]
# l1=[element for innerList in l for element in innerList]
# a="".join(map(str,l1))
# s=sorted(a)
# new_list=[]
# new_list.append(s[:6])
# new_list.append(s[6:9])
# new_list.append(s[9:11])
# new_list.append(s[11:14])
# print(new_list)
# print(type(new_list))

# s="bhagyashree"
# n=len(s)
# i=-1
# while i>=-n:
#     print(s[i],end="")
#     i=i-1

# from collections import Counter
# print(Counter('bhagyashree'))


# s='Bhagyashree'
# l=[]
# for i in s:
#     if i not in l:
#         l.append(i)
# for i in l:
#     print('{} occurs {} times'.format(i,s.count(i)))

#s='Bhagyashree'
# d=dict()
# for i in s:
#     if i not in d.keys():
#         d[i]=1
#     else:
#         d[i]=d[i]+1
# print(d)

# ip='12223114455'
# op=[(1,1),(3,2),(1,3),(2,1),(2,4),(2,5)]
#
# n=int(input('Enter the no of rows:'))
# for i in range(n):
#     print('* ' * n)

#n=int(input('Enter the rows:'))
# for i in range(n):
#         for j in range(i,n):
#                 print('',end=' ')
#         for j in range(i+1):
#                 print('*',end=' ')
#         print()
#
# n=int(input('Enter the rows:'))
# for i in range(n):
#         for j in range(i+1):
#                 print('',end=' ')
#         for j in range(i,n):
#                 print('*',end=' ')
#         print()

# ip='12223114455'
# ip1='bhagyashree'
# print(ip1.split())

#
# s='a4b2c3a1e2c4'
# output=''
# for x in s:
#     if x.isalpha():
#         output=output+x
#         previous=x
#     else:
#         output=output + previous*(int(x)-1)
# print(output)
#
# s='Bhagyashree'
# from  collections import Counter
# print(Counter(s.split()))
#
# ip=[(1,23),(72,3),(8,10),(18,3),(7,8)]
# lst=[]
# for i in ip:
#     for j in i:
#         for k in str(j):
#             if k.isnumeric():
#                 lst.append(k)
# print(",".join(sorted(set(lst))))
#
#
# ip=[(1,33),(43,3),(76,87),(15,78)]
# lst=[]
# for i in ip:
#     for j in i:
#         for k in str(j):
#             if k.isnumeric():
#                 lst.append(k)
# print(",".join(sorted(set(lst))))
#
# def findEle(lst,n):
#     for i in range(1,n):
#         leftsum=sum(lst[0:i])
#         rightsum=sum(lst[i+1:])
#         if leftsum==rightsum:
#             return lst[i]
#     return-1
# if __name__=="__main__":
#     lst=[12,1,12,4,16,30,7,10,15,20,30]
#     n=len(lst)
#     print(findEle(lst,n))
#
#
# lst=[8,3,1,8,10,2]
# n=len(lst)
# for i in range(1,n):
#     leftsum=sum(lst[0:i])
#     rightsum=sum(lst[i+1:])
#     if leftsum==rightsum:
#         print("The element present in the list is:",lst[i])

#
# l=[8,3,1,8,10,2]
# n=len(l)
# for i in range(1,n):
#     leftsum=sum(l[0:i])
#     rightsum=sum(l[i+1:])
#     if leftsum==rightsum:
#         print("The element present in the list is:",l[i])
#
# l=[(23,31),(57,65),(23,5),(54,3),(90,54),(83,2)]
# lst=[]
# for i in l:
#     for j in i:
#         for k in str(j):
#             if k.isnumeric():
#                 lst.append(k)
# print(",".join(sorted(set(lst))))
#
# s='Bhagyashree'
# d={}
# for i in s:
#     if i not in d.keys():
#         d[i]= 1
#     else:
#         d[i]=d[i]+1
# print(d)
#
# l=[x for x in range(1,100) if x%5==0]
# print(l)
#
# def factorial(num):
#     if num==0:
#         result =1
#     else:
#         result=num*factorial(num-1)
#     return result
# print("factorial of 4 is:",factorial(4))
#
# l1=[2,4,5,6,8]
# l=[x**2 for x in l1]
# print(l)
#
# number=(4,7,19,2,89,45,72,22)
# sorted_number=sorted(number)
# print(sorted_number)
#
# l=[1,2,3,4,5]
# l1=[x**2 for x in l]
# print(l1)
#
# l=[1,2,3,4,5]
# n=len(l)
# i=len(l)-1
# while i>=0:
#     print(l[i],end=" ")
#     i=i-1
#
# l=[1,2,3,4,5]
# n=len(l)
# i=-1
# while i>= -n:
#     print(l[i],end=" ")
#     i=i-1
#
# l=[2,9,5,3,6]
# m=max(l)
# x=[a for i,a in enumerate(l) if a<m]
# print(max(x))
#
#
# def decor1(func):
#     def inner():
#         x=func()
#         return x*x
#     return inner
#
# def decor(func):
#     def inner():
#         x=func()
#         return 2*x
#     return inner
#
# @decor1
# @decor
# def num():
#     return 10
#
# print(num())
#
# def decor(func):
#     def inner(name):
#         if name == "sunny":
#             print("hello sunny bad morning")
#         else:
#             func(name)
#     return inner
#
# @decor
# def wish(name):
#     print("hello",name,"Good Morning")
#
# wish("durga")
# wish("bhagya")
# wish("sunny")
#
# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for x in fib():
#     if x> 100:
#         break
#     print(x,end=" ")
#
# def firstn(num):
#     n=1
#     while n<=num:
#         yield n
#         n=n+1
# values=firstn(10)
# for x in values:
#     print(x,end=" ")
#
#
# def countdown(num):
#     while num>0:
#         yield num
#         num=num-1
# values=countdown(10)
# for x in values:
#     print(x,end="")

l=['bhagya@awatade','abcd@ascd']

