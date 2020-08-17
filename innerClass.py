class Employee:

    def __init__(self,name,rollno):

        self.name = name
        self.rollno = rollno

    def show(self):

        print(self.name ,self.rollno)

s1 = Employee("Mike" ,1001)
s2 = Employee('Nuel' ,1005)
s1.show()
s2.show()