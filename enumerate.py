
for ind,let  in enumerate('zyxwu'):
    print('At position {} the letter is : {}'.format(ind, let))

print('....using list in enumerate..............')
print(list(enumerate('abcde')))
print(".....................")
for ind,let  in enumerate(['z','y','x','w','u']):
    print('At position {} the letter is : {}'.format(ind, let))

# using zip function
print('.....ZIP FUNCTION.................')
list1 = [1,2,3,4,5]
list2 = ['Nuel' ,'Emma' ,'Natha','Id' ,'Amaka']
for item in zip(list1 ,list2):
    print(item)
print(''''list in zip''')
print(list(zip(list2 ,list1)))

# in operator
print('........IN operator...........')
print('x' in 'abcd')
print('.............')
print('x' in ['a','b','c','d'])
print('.............')
print(3 in [1,2,3,4])

print('.......using shuffle fuction from random......')
from random import  shuffle ,randint
mylist =[1,2,3,4,5]
shuffle(mylist)
print(mylist)
print('..........randint..........')
print(randint(10,20))
import random
print('random number')
print(random.randint(0,10))
