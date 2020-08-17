pi =3.14

def area():
    a=lambda ar :ar *ar
    a=a(6) *pi

    return a


k=area()
print(k)

def arealambda():
    arr=float(input("enter the radius of a circle:"))
    res =lambda arr : arr * arr
    area = res(arr) * pi
    print("Area of a circle is :" ,area)
    
arealambda()