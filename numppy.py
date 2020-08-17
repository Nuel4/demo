import  numpy as np
a =np.array([(20,3,21,45,67)])
print(a)

b =np.array([(20,3,21,45,67),(3,5,6,7,8),(11,2,4,9,10),(21,23,45,67)])
print(b)

c =np.array([(4.2,4.5,6.7,2.1)] ,int)
print(c)

d =np.array([(20,3,21,45,67)] ,float)
print(d)


e =np.linspace(0,10,5)  #start stop ,part - how many places to divide 10
print("partisioning :" ,e)

f = np.logspace(1,20,5)     # log 0f 1 to 20 and partition it into 5
print('log space :' ,f)
print('%.2f' %f[1])

g = np.zeros(5)
print("zeros :" ,g)

h =np.ones(5)
print("ones :" ,h)

i = np.ones(5,int)
print('only integer values:' ,i)

j =np.arange(1,10 ,2)  # print 1 ,excape 2 places and print next up till 10
print('arange values :' ,j)
