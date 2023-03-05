from time import time,ctime,localtime
epoch=time()
print(epoch)

et=ctime(epoch)
print(et)

a=localtime()
print(a.tm_year)

#
# from datetime import datetime
# dt=datetime(2022, 4,24,14,40)

s="shubham12"
l=list(filter(lambda s:s.isdigit(),s))
print("".join(l))

l=["bhagya@awatade",'awatade@bhagya']
l1=list(filter(lambda l:l.isalpha(),l))
print(l1)


l=[10,20,32,43,35,45,65,4,56,53,67]
l1=[x for x in l if x < max(l)]
print(max(l1))

arr=[6,2,3,4,5,7,8]
temp=0
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if(arr[i] > arr[j]):
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
print()

p=[1,2,3,4,56,6,7]
d=[x for x in p if x%2]
print(d)

p=[1,2,3,4,56,6,7]
d=[x for x in p if x%3]
print(d)