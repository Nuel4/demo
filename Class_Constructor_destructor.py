class n:
    def __init__(self):
        print('welcome home')

    def __del__(self):
        print("safe journey")

p =n()

class nn:
    def sam(self,fname,lname):
        self.fname =fname
        self.lname = lname

        def __del__(self):
            print("safe journey, object destroyed")

k = nn()
k.sam("Emma" ,"Nuel")
print("first name : " ,k.fname)
print("surname: " ,k.lname)