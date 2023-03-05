l=['bhagya@awatade','abcd @ascd']
# o/p= bhagya
#       awatade
#       abcd
#       ascd

for x in l:
    l1=x.split('@')
    for x in l1:
        print(x)

#
# print("Hello world"[::-1])
#
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