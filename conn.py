# str="Bhagyashree"
# counter=0
# for ch in str:
#     counter =counter +1
# print(counter)


# str1="Bhagyashree"
# vowels=['a','e','i','o','u']
# counter=0
# for ch in str1:
#     if ch in vowels:
#         counter +=1
# print(counter)
#
# s="Viaan"
# print(list(enumerate(s)))
#
#
# str="bhagya"
# str1=""
# count=len(str)
# while count >0:
#     str1= str1 +str[count-1]
#     count=count-1
# print(str1)
#
# str="nihit"
# str1=""
# for ch in str:
#     str1= ch+str1
# print(str1)


import time
epoch=time.time()
print(time.ctime(epoch))

import time
print(time.ctime())

l=[10,20,45,78,98,56,4,5,78,100,23,4,5,34]
max=l[0]
for ele in l:
    if ele > max:
        max=ele
print(max)

l=[10,20,45,78,98,56,4,5,78,100,23,4,5,34]
min=l[0]
for ele in l:
    if ele <min:
        min=ele
print(min)

print((10,20,30)+(100,))

s={10,20,30,(10,20)}
print(type(s))

num=int(input('enter the number:'))
result=1
for i in range(num,0,-1):
    result=result* i
print(result)

# candid1=int(input('Enter 1st candidate name:'))
# candid2=int(input('Enter 2nd candidate name:'))
# cand1_votes=0
# cand2_votes=0
# voters_id=[101,102,103,104,105,106]
# no_of_voters=len(voters_id)
# print("number of voters:",no_of_voters)
# voted=[]
# while True:
#     if voters_id==[]:
#         print("voting is over")





