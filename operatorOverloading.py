a =8
b =5
print("a+b =",a +b)
print(int.__add__(a,b))
e ='nuel'
f ='emm'
print(e+f)
print('concatenating :' ,str.__add__(f,e))


class student:
    def __init__(self ,m1 ,m2):
        self.m1 =m1
        self.m2 =m2

    def show(self):
        print(self.m1,self.m2)


s1 =student(175 ,150)
print(s1.m1)

class stud:
    def __init__(self ,m3 ,m4):
        self.m3 =m3
        self.m4 =m4

    def __add__(self, other):
        mm =self.m3 +other.m3
        m =self.m4 +other.m4
        k =mm + m
        return  k
        print("the value k is :" ,k)


    def __gt__(self, other):
        r1 = self.m3 +other.m3
        r2 = self.m4 +other.m4
        if r1 > r2 :
            return r1
        else:
            return r2

    def __sub__(self, other):
        pass



d = stud(80 ,150)
print(d.m4)
dd = stud(70,80)
print(' total value:' , dd +d)


