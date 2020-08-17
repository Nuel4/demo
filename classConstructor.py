class emp:
    def __init__(self,office ,position):
        self.office =office
        self.position =position

    def show(self):
        print("inherited attributes")
        #print(self.name,self.id,self.height ,self.py,self.addr)
       # print('personal properties')
        print(self.office,self.position)


k =emp('airtel' ,'HR')
k.show()
print(k.office)
print(k.position)