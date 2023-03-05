# file=open("emp.txt",'w')
# file.write("i am employee\n")
# file.write(" i am a data engineer\n")
# file.write("this is team brainwork")
# file.close()

file1=open("emp.txt",'r')
result=file1.readlines()
print(result)
file1.close()


# import os
# filename=input("Enter the filename:")
# if os.path.isfile(filename):
#     f=open(filename)
#     f.close()
# else:
#     print("file not exist")
#
# with open("xyz.txt","w") as f:
#     f.write("Hello")
#     f.close()
#
# with open("xyz.txt","w") as f:
#     f.write("Hello\n")
#     f.write("Good Morning\n")
#     f.write("How r u\n")
#     f.write("What r u doing")


# with open("xyz.txt","r") as f:
#     data=f.readlines()
#     print(data)

# file=open("xyz1.txt","w")
# list=['Saurabh\n','Aniruddha\n','Prathamesh\n','Bhagya\n','Pratiksha\n','Ankur']
# file.writelines(list)
# file.close()

# file=open('xyz1.txt',"r")
# data=file.readlines()
# for line in data:
#     print(line,end="")
#
# f=open('xyz1.txt',"r")
# print(f.tell())
# f.read(4)
# print(f.tell())
# f.read(5)
# print(f.tell())
# f.seek(6)
# print(f.tell())
# f.seek(3)
# print(f.tell())
# f.close()
#
#
# f=open('xyz1.txt',"r")
# number_of_words=0
# number_of_chars=0
# number_of_lines=0
# for line in f:
#     number_of_lines+=1
#     line=line.strip('\n')
#     number_of_chars+=len(line)
#     list1=line.split()
#     number_of_words+=len(list1)
# f.close()
# print("number of lines:",number_of_lines)
# print("number of words:",number_of_words)
# print("number of chars:",number_of_chars)

# f1=open("xyz1.txt","r")
# f2=open("xyz2.txt","w")
# data=f1.readlines()
# for line in data:
#     f2.write(line)
# f1.close()
# f2.close()


import random
rand_nums=[]
for i in range(10):
    rand_nums.append(random.randrange(1200,2000))
print(rand_nums)

l=[{'a':0,'b':0},{'c':0},{'d':0}]
for x in l:
    print(x)

