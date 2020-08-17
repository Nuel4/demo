from array import *
k =array('I',[3,54,32,12,45,67,89,27])
newarry = array(k.typecode,(a for a in k))

for j in newarry:
    print(j)


m =array('I',[3,54,32,12,45,67,89,27])
newa = array(m.typecode,(a*2 for a in m))

for j in newa:
    print(j)
print(newa)


n =array('I',[3,5,32,21,4,67,8,27])
newarry = array(n.typecode,(a for a in n))

count =0
while count < len(newarry):
    print(newarry[count])
    count += 1

print(newarry)