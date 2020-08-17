from numpy import *
arr = array([2,21,34,12,25])
ar =array([10,3,45,6,11])
a =arr +ar
print(a)

c =arr * ar
print(c)

aa = array([2,21,34,12,25])
print("cos :" ,cos(aa))

aa = array([2,21,34,12,25])
print("tan:" ,tan(aa))

aa = array([2,21,34,12,25])
print("sin:" ,sin(aa))

aa = array([2,21,34,12,25])
print("sqrt:" ,sqrt(aa))

print("memory location:" ,id(aa))

ab =aa.view()
print("view: ",ab)