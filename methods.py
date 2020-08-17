class Student:
    school = 'Nuel University'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2= m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3) /3

    def get_m1(self):
        return self.m1

    def set_m1(self,value):
        self.m1 = value
    @classmethod
    def info(cls):
        #print(cls.school)
        return cls.school



s1 =Student(20,13,56)
s2 =Student(110,222,123)
s3 =Student(50,70,80)
s3.set_m1(20000)
print(s3.get_m1())
print(s1.m1)
print(s1.avg())
print(Student.info())
print(s1.info())