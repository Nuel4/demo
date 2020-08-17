import array
a =array.array('i',[2,4,6,8,10,24,-6,9,-2])  # small i stands for signed integer. it can take negative values
print(a)


b =array.array('f' ,[4,7,8,2,4,5])
print(b)

c =array.array('I' ,[9,6,8,9,10,39,3])  # upper I does not take negative value
print(c)

d =array.array('u' ,['t','y','r','p','s']) # unicode takes only single character
print(d)

e =array.array('i' ,[9,6,8,23,5,10])
print(' memory address: and number of elements' ,e.buffer_info()) # address of the array and the size of the array

print(e.typecode) # to know the type of arry it is

e.append(45) # to append a value
print("new value of e :" ,e)

e.extend([4,6,11,56])
print('adding multiple values: ' ,e)

e.reverse()
print('reversing e values: ' ,e)
print('first value on the list:' ,e[0])

for k in range(len(e)):
    print(e[k])
