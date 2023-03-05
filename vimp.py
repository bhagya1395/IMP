# for i in range(10):
#     print('Datta',end=" ")
#
# print(10 *' bhagya')





# import pickle
# l=[10,20,30,40]
# file=open('f1.txt',"wb")
# pickle.dump(l,file)
# file.close()

# import pickle
# file=open('f1.txt',"rb")
# l=pickle.load(file)
# print(l)


class A:
    __name="Ravi"
    def __init__(self):
        print(self.__name)
        self.__DisplayInfo()
    def __DisplayInfo(self):
        print("Welcome to TBW")

obj=A()
