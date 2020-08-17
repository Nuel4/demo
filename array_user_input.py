from array import *

num = array('i', [])
i = 0
intake = int(input('enter the number of elements u want:'))
while i < intake:
    x = int(input('enter each value:'))
    num.append(x)
    print(i,num[i])
    i += 1
print(num)



num = array('i', [])
intake = int(input('enter the number of elements u want:'))
for i in range(intake):
    x = int(input('enter each value:'))
    num.append(x * x)
    print(i, num[i])

print(num)