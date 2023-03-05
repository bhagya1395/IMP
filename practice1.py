# def factorial(n):
#     if n==0:
#         result=1
#     else:
#         result=n*factorial(n-1)
#     return result
#
# print("Factorial of 4 is:",factorial(4))



# def fact(num):
#     result=1
#     while num>=1:
#         result=result*num
#         num=num-1
#     return result
# for i in range(1,5):
#     print("The factorial of",i,"is:",fact(i))



# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for f in fib():
#     if f>100:
#         break
#     print(f)

#
#
# s='bhagya'
# n=len(s)
# i=-1
# while i>=-n:
#     print(s[i],end="")
#     i=i-1


#
# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for f in fib():
#     if f>200:
#         break
#     print(f)

# def countdown(num):
#     print("Start Countdown")
#     while(num>0):
#         yield num
#         num=num-1
# values=countdown(10)
# for x in values:
#     print(x)


# def countdown(num):
#     print("Start Countdown")
#     while(num>0):
#         yield num
#         num=num-1
# values=countdown(10)
# for x in values:
#     print(x,end=" ")

# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for f in fib():
#     if f >10:
#         break
#     print(f,end=" ")


# def fact(n):
#     if n==0:
#         result=1
#     else:
#         result=n*fact(n-1)
#     return result
# print(fact(8))

# s="aaaabbbbcccccdkfhgfghgfgh"
# output=''
# for ch in s:
#     if ch not in output:
#         output=output+ch
# print(output)
#
#
# s="aaaabbbbcccccdkfhgfghgfgh"
# output=[]
# for ch in s:
#     if ch not in output:
#         output.append(ch)
# print(output)
#
#
# s="Bhagyashree"
# l=[]
# for ch in s:
#     if ch not in l:
#         l.append(ch)
# for ch in l:
#     print('{} occurs {} times'.format(ch,s.count(ch)))


x='abc'
y='xyz'
z=y[::-1]
p=list(zip(x,z))

#print(x[0]+y[2]+x[1]+y[1]+x[2]+y[0])

s='Bhagyashree Vitthal Awatade'
l=s.split ()
l1=[]
for i in range(len(l)):
    if i < (len(l)-1):
        l1.append(l[i][0])
    else:
        l1.append(l[i])
print(". ".join(l1))


# x=['AB12','AB11','AB21','AB15']
# print(sorted(x))

s= 'Brain$work&'
l=[x for x in s if x.isalnum()][::-1]
l1=[s.index(y) for y in s if y.isalnum()==False]
for i in l1:
    l.insert(i,s[i])
print("".join(l))

# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})

from collections import Counter
sample_data= [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
output= Counter()
for d in sample_data:
    output[d['item']] +=d['amount']
print(output)

d1={1:10 ,2:20}
d2={3:30 ,4:40}
d3={5:50, 6:60}
d4={}
for d in (d1,d2,d3):
    d4.update(d)
print(d4)

d={0:10, 1:20}
d.update({2:30})
print(d)


d={'x':10 ,'y':20, 'z':30}
for k,v in d.items():
    print(k,"->",v)


# n=int(input('enter a number:'))
# d=dict()
# for x in range(1,n+1):
#     d[x]=x**3
# print(d)


s='python language is very easy language'
l=s.split()
l1=[]
for word in l:
    if word not in l1:
        l1.append(word)
for word in l1:
    print('{} occurs {} times'.format(word,s.count(word)))

# string=input("Enter string:")
# word=input("Enter word:")
# a=[]
# count=0
# a=string.split(" ")
# for i in range(0,len(a)):
#       if(word==a[i]):
#             count=count+1
# print("Count of the word is:")
# print(count)


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))

s='bhagyashree'
d={}
for x in s:
    d[x]=d.get(x,0)+1
for k,v in d.items():
    print(k,":",v)

from collections import Counter
s=Counter('bhagyashree')
print(s)



