import numpy as np
h =np.array([(3,5,6,7),(1,3,7,9)])
print(h)
m = np.matrix(h)
print('matrix value:' ,h)

n =np.matrix('2,4,6,1;8,4,2,1') # defining values in matrix function 2D with 4 elements
print('matrix val :' ,n)

o =np.matrix('24,12 ;8,4;10,5;9,3')  # defining values in matrix function 4D with 2 elements
print('matrix 4d :' ,o)

d =np.array(([(3,2,1,5),(2,4,6,8),(4,2,6,8),(10,20,30,40)]))
dd =np.diagonal(d) # diagonal values
print('d values: ',d)
print('only diagonal values:' ,dd)

k=np.min(d)
print('min vale: ',k)
kk =np.max(d)
print('max value :', kk)

x =np.matrix('4,1,5;2,5,1;6,7,2')
y =np.matrix('2,4,5;9,12,2;5,2,6')
print('x =' ,x)
print('y = ' ,y)
z = x* y
print('x *y :' ,z)
#print('................vstack -vetical ........................')


#print('vstack:' , np.vstack(d))

#print('................hstack -vetical ........................')
#print('hstack:' , d.np.vstack)