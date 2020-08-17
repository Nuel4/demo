import numpy as np
a = np.array([(4,3,12,34),(23,5,11,56)])
print('a values:' ,a)

aa =a.shape  # shape is used to know how mny rows and columns
print('shape of a :' ,aa)

ab =a.size  #total number of elements
print("size of a :" ,ab)

print(a[0])

ac =a.flatten() # to combine all elements in one array -list
print("flattening : " ,ac)

b =np.array([(4,6,8,12,2),(1,3,5,7,9),(3,6,9,12,15)]) # 3 dimentional array
print("3 dimentional array " ,b)

cc =b.reshape(5,3)  #converting it to 3 dimentional aray
print('reshaping  3D to 5D:' ,cc)

e =np.array([(3,2,1,5,7,4),(9,8,5,3,2,1)])
print('values: ',e)

f =e.reshape(3,4)  # 3 rows and 4 columns - 3 dimentional arra
print('reshaping 2D  to 3D',f)

ff =e.reshape(6,2)  # 6 dimentional array
print('from 3D to 6D:' ,ff)

g =ff.reshape(2,2,3)  # 2 dimentional arrays having 3 elements in each
print(g)
