#reverse direction:
#1.
# s='bhagya'
# for x in s[::-1]:
#     print(x,end='')

         #OR

# s='bhagya'
# n=len(s)
# i=-1
# while i>=-n:
#     print(s[i],end='')
#     i=i-1

# s='bhagya'
# l=s.split()
# l1=[]
# i=0
# while i< len(l):
#     l1.append(l[i][::-1])
#     i=i+1
# print(''.join(l1))

# s='bhagya'
# i=len(s)-1
# output=''
# while i>=0:
#     output=output+s[i]
#     i=i-1
# print(output)

# s='Bhagyashree Awatade'    #o/p--Awatade Bhagyashree
# l=s.split()
# l1=[]
# i=len(l)-1
# while i>=0:
#     l1.append(l[i])
#     i=i-1
# # print(' '.join(l1))
#
# s='Bhagyashree Awatade'   #----o/p----edatawA eerhsaygahB
# l=s.split()
# l1=[]
# i=len(l)-1
# while i>=0:
#     l1.append(l[i][::-1])
#     i=i-1
# print(' '.join(l1))
#
#
# s='Bhagyashree'
# i=0
# print("Character present at even place:")
# while i < len(s):
#     print(s[i], end=' ')
#     i=i+2
# print("\nCharacter present at odd place:")
# i=1
# while i < len(s):
#     print(s[i], end=' ')
#     i=i+2

# s='Baysre'
# s1='hgahe'
# output=''
# i,j=0,0
# while i<len(s)  or i<len(s1):
#     if i <len(s):
#         output=output+s[i]
#         i=i+1
#
#     if j <len(s1):
#         output=output+s1[j]
#         j=j+1
# print(output)

# s1='baysre'
# s2='hgahe'
# output=''
# i,j=0,0
# while i<len(s1) or j<len(s2):
#     if i< len(s1):
#         output=output +s1[i]
#         i=i+1
#     if j < len(s2):
#         output=output +s2[j]
#         j=j+1
# print(output)



# s='Kancha'
# n=len(s)-1
# while n>=0:
#     print(s[n],end='')
#     n=n-1

# s='B4A1D3'
# l="".join(sorted(list(filter(lambda x:x.isalpha(),s)))+(sorted(list(filter(lambda y:y.isdigit(),s)))))
# print(l)
#
# s='BraiNwoRkS'
# print("".join(list(filter(lambda i:i.islower(),s))+list(filter(lambda j:j.isupper(),s))))
#
# s='Bhagyashree Vitthal Awatade'
# l=s.split()
# l1=[]
# for i in range(len(l)):
#     if i< (len(l)-1):
#         l1.append(l[i][0])
#     else:
#         l1.append(l[i])
# print(".".join(l1))
#
# s='A4K3B2'
# output=''
# for ch in s:
#     if ch.isalpha():
#         output=output + ch
#         x=ch
#     else:
#         output=output + chr(ord(x)+int(ch))
# print(output)
#
# s='a4b3c2'
# output=''
# for x in s:
#     if x.isalpha():
#         output=output + x
#         previous=x
#     else:
#         output=output +previous * (int(x)-1)
# print(output)

# s='b3h4d2'
# output=''
# for x in s:
#     if x.isalpha():
#         output=output +x
#         previous=x
#     else:
#         output=output + previous* (int(x)-1)
# print(output)
#
#
# s='AAABBBBCCCCDDDEEEEAABBB'
# l1=[]
# for x in s:
#     if x not in l1:
#         l1.append(x)
# print("".join(l1))

# s='Bhagyashree'
# d={}
# for x in s:
#     if x in d.keys():
#         d[x]=d[x] +1
#     else:
#         d[x]=1
# for k,v in d.items():
#     print("{} = {} times".format(k,v))
#
# s='Bhagyashree'
# a=dict()
# for i in s:
#     if i not in a.keys():
#         a[i] = 1
#     else:
#         a[i] = a[i] + 1
# print(a)

#
# s='bhagyashree'
# d={}
# for x in s:
#     if x not in d.keys():
#         d[x]=1
#     else:
#         d[x]=d[x]+1
#
# print(d)
# # for k,v in d.items():
# #     print('{}={} times'.format(k,v))
#
#
# l=[1,2,3,4,5,6,7,8]
# print(list(filter(lambda x:x%2==0,l)))
#
# l=[1,2,3,4,5,6,7,8]
# n=len(l)
# i=0
# for x in l:
#     print('elemets present at positive index {} and at negative index {} is {}'.format(i,i-n,x))
#     i=i+1
#
#
# l=[1,2,3,4]
# n=len(l)
# for i in range(n):
#     print(l[i],'is present at positive index:',i,"and at negative index:",i-n)
#
# l=[1,2,3,4]
# l[2]=10
# l.insert(1,80)
# print(l)
#
# l=[]
# for i in range(101):
#     if i%10==0:
#         l.append(i)
# print(l)

# l=[2*x for x in range(11)]
# print(l)
#
# l=['Bhagyashree','Dnyanu','PuJA','Vaibhav']
# l1=[w[0] for w in l]
# print(l1)


# vowels=['a','e','i','o','u']
# word=input("Enter the string:")
# found=[]
# for ch in word:
#     if ch in vowels:
#         if ch not in found:
#             found.append(ch)
# print(found)


# vowels=['a','e','i','o','u']
# s='Bhagyashree'
# w=set(s)
# print(w.intersection(vowels))

#
# # factorial:
# def fact(num):
#     result=1
#     while num>=1:
#         result =result *num
#         num=num-1
#     return result
# for i in range(1,5):
#     print("The Factorial of ",i,"is:",fact(i))
#
# def factorial(n):
#     if n==0:
#         result=1
#     else:
#         result=n * factorial(n-1)
#     return result
# print("Factorial of 5 is:",factorial(5))
#
#
# def countdown(num):
#     print('start countdown')
#     while (num>0):
#         yield num
#         num=num-1
# values=countdown(5)
# for x in values:
#     print(x,end=' ')
#
# def firstn(num):
#     n=1
#     while n<=num:
#         yield n
#         n=n+1
# values=firstn(5)
# for x in values:
#     print(x,end=' ')
#
#
#
# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for f in fib():
#     if f>100:
#         break
#     print(f,end=' ')

#l=['Bhagya@Awatade','abcd@asdc']
#op=Bhagya
#   Awatade
#   abcd
#   asdc