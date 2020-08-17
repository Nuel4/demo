class person:
    def __init__(self,name,id,height): # should only have one init constructor
        self.name = name
        self.id =id
        self.height =height


    def pay(self,py,addr):

        self.py = py
        self.addr=addr




class emp(person):

    def __init__(self,office ,position):  # only the child class constructor will be executed without super constructor
        self.office =office
        self.position =position

    def show(self):
        print("inherited attributes")
        print(self.name,self.id,self.height ,self.py,self.addr)
        print('personal properties')
        print(self.office,self.position)


s =person("MUSA" ,2005 ,5.7)

print(s.name)
print(s.id)
print(s.height)
s.pay(5000,'lagos')
print("second function")
print(s.py)
print(s.addr)

x =emp('MTN' ,'Manager')
print(x.office ,x.position)

x.pay(4000,'enugu')
print(x.py,x.addr ,end=" ")
#emp.show(,)
#x.show()