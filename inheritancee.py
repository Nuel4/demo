class person:
    def __init__(self,name):
        self.name =name
        print('welcome here')




class emp(person):  #can access constructor of person when emp does not have a constructor(_init_)


    def show(self,office ,position):
        self.office =office
        self.position =position



s =emp('mike')
s.show('lagos' ,'sales')

print(s.office)
print(s.position)
print(s.name)
#print(x.name)
#emp.show(,)
#x.show()