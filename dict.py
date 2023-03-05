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

d={}
for x in range(1,16):
    d[x]=x*x
print(d)

d1={'a':100, 'b':200}
d2={'x':300, 'y':200}
d1.update(d2)
print(d1)

d={1:10, 2:20}
print(sum(d.values()))

d={1:10, 2:20, 3:30, 4:40}
result=1
for key in d:
    result=result*d[key]
print(result)

d={1:10, 2:20, 3:30, 4:40}
del d[1]
print(d)

k = [1,2,3,4]
v=[10,20,30,40]
d=dict(zip(k,v))
print(d)

d={3:30, 9:50, 4:40,  1:30}
for key in sorted(d):
    print( "%s: %s" % (key, d[key]))

d={'x':1000, 'y':345, 'z':836}
min=min(d.keys(), key=(lambda k:d[k]))
print("Minimum Value: ",d[min])
max=max(d.keys(), key=(lambda k:d[k]))
print("Maximum Value: ",d[max])


class dictObj(object):
    def __init__(self):
        self.x = 'red'
        self.y = 'Yellow'
        self.z = 'Green'

test=dictObj()
print(test.__dict__)


student_data = {'id1':
   {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id2':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id3':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id4':
   {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
}
result={}
for k,v in student_data.items():
    if v not in result.values():
        result[k]=v
print(result)


my_dict = {1:20}
if not bool(my_dict):
    print("Dictionary is empty")
else:
    print(my_dict)


from collections import Counter
d1={'a':100, 'b':200, 'c':300}
d2={'a':300, 'b':200, 'c':400,'d':200}
d=Counter(d1) + Counter(d2)
print(d)

d= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
unique_value=set(val for dic in d for val in dic.values())
print("Unique Values:",unique_value)


d={'1':['a','b'], '2':['c','d']}
import itertools
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))

from heapq import nlargest
my_dict = {'a':500, 'b':3423, 'c':580, 'd':400,'e':900}
three_largest = nlargest(3,my_dict,key=my_dict.get)
print(three_largest)

from collections import Counter
sample_data= [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
output= Counter()
for d in sample_data:
    output[d['item']] += d['amount']
print(output)

from collections import defaultdict, Counter
str= 'w3school'
d={}
for letter in str:
    d[letter]= d.get(letter,0) + 1
print(d)

d={'c1':[1,2,3], 'c2':[5,6,7], 'c3':[9,10,11]}
for row in zip(*([key] + (value) for key,value in sorted(d.items()))):
    print(*row)


student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
print(sum(d['id'] for d in student))
print(sum(d['success'] for d in student))

list=[1,2,3,4]
new_dict =current = {}
for name in list:
    current[name]= {}
    current = current[name]
print(new_dict)


num={'n1':[2,3,1], 'n2':[5,1,2], 'n3':[3,2,4]}
sorted_dict={x: sorted(y) for x,y in num.items()}
print(sorted_dict)

student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
dict={x.translate({32:None}): y for x,y in student_list.items() }
print(dict)

from heapq import nlargest
from operator import itemgetter
items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
for name,value in nlargest(3,items.items(),key=itemgetter(1)):
    print(name,value)

dict={1:10, 2:20, 3:30, 4:49}
print("key value count")
for count, (key,value)in enumerate(dict.items(),1):
    print(key,' ',value,' ',count)

students = {'Aex':{'class':'V','roll_id':2},'Puja':{'class':'V','roll_id':3}}
for a in students:
    for b in students[a]:
        print(b,':',students[a][b])

student={'name':'Alex','class':'V','roll_id':'2'}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'Alex'})
print(student.keys() >= {'roll_id', 'name'})
