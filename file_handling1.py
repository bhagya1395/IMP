# f=open('abcd.txt','w')
# f.write('Bhagyashree\n')
# f.write('Puja\n')                                 #only for string
# f.write('Priyanka\n')
# f.write('good evening\n')
# list=['sunny\n','bunny\n','vinny\n','chinny']    #list of multiple lines
# f.writelines(list)
# print('Data written to the file successfully')
# f.close()

# f=open('abcd.txt','r')
# data=f.read()    #to read total data from the file
# print(data)
# f.close()
#
# f=open('abcd.txt','r')
# data=f.read(15)    #to read only 15 characters
# print(data)
# f.close()
#
# f=open('abcd.txt','r')
# data=f.readline()    #to read only one line
# print(data)
# f.close()

# f=open('abcd.txt','r')
# data=f.readlines()    #to read all lines into a list
# for lines in data:
#     print(lines)
# f.close()

# with open("abcd.txt",'w') as f:
#     f.write('Durga\n')
#     f.write('Software\n')
#     f.write('Solutions\n')
#     print("Is file closed",f.closed)
# print("Is file closed",f.closed)
#
# #tell()--we can use tell() method to return current position of the cursor(file pointer) from beginning of the line.
#
# f=open('abcd.txt','r')
# print(f.tell())
# print(f.read(2))
# print(f.tell())
# print(f.readlines())
# print(f.tell())

#seek()--We can use seek() method to move cursor(file pointer) to specified location.

#f.seek(offset,fromwhere)
#offset represents the number of positions

#The allowed values for second attribute(from where)are
# 0--> from beginning of file(default value)

# data='All students are STUPIDS'
# f=open('abcd.txt','w')
# f.write(data)
# with open('abcd.txt','r+')as f:
#     text=f.read()
#     print(text)
#     print('The current position of the cursor',f.tell())
#     f.seek(17)
#     print('The current position of the cursor', f.tell())
#     f.write('GEMS!!!')
#     f.seek(0)
#     text=f.read()
#     print('Data after Modification')
#     print(text)

#How to check a particular file exits or not?
#We can use os library to get information about files in our computer
#os module has path sub module,which contains isFile() function to check whether a particular file exists or not?
#os.path.isfile(fname)
#
# import os,sys
# fname=input("Enter File Name:")
# if os.path.isfile(fname):
#     print("file exists:",fname)
#     #f=open(fname,'r')
# else:
#     print("File does not exist:",fname)
#     sys.exit(0)
# f = open(fname, 'r')
# print("content of file is:")
# data=f.read()
# print(data)
#
# #sys.exit()-->To exit system without executing rest of the program.
# #argument represents status code. 0 means normal termination & it is default value.
#
# import os,sys
# fname=input("Enter File Name:")
# if os.path.isfile(fname):
#     print("file exist:",fname)
#     f = open(fname, 'r')
# else:
#     print('File does not exist',fname)
#     sys.exit(0)
# # f=open(fname,'r')
# lcount=wcount=ccount=0
# for line in f:
#     lcount=lcount +1
#     ccount=ccount + len(line)
#     words=line.split()
#     wcount=wcount+len(words)
# print("The number of lines:",lcount)
# print("The number of words:",wcount)
# print("The number of Characters:",ccount)

#HANDLING BINARY DATA:
#Program to read image file and write to a new image file?
# f=open("D:\image3.jpg","rb")
# f1=open("newpic.jpg","wb")
# bytes=f.read()
# f1.write(bytes)
# print("New image is available with name:newpic.jpg")

#HANDLING CSV DATA:

#CSV---->comma separated values---->python provides csv module to handle csv files.

#Writing data  to csv file:

import pickle
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno;
        self.ename=ename;
        self.esal=esal;
        self.eaddr=eaddr;
    def display(self):
        print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)
with open("emp.dat","wb")as f:
    e=Employee(100,"Durga",1000,"Hyd")
    pickle.dump(e,f)
    print("Pickling of Employee Object completed....")
with open("emp.dat","rb")as f:
    obj=pickle.load(f)
    print("Printing Employee Information after unpickling")
    obj.display()




