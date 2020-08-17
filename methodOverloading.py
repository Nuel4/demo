class student:
    def __init__(self,m1,m2):
        self.m1 =m1   # assigning values from the user
        self.m2 = m2

    def sum(self,a=None,b=None ,c=None): #default value is none if  no value is passed
        s=0

        if a!=None and b!=None and c!=None : # if none of arguemnt is null
            s = a+b+c       #add all the values here
           # return s      #return s
        elif a!=None and b!=None: # executes this block if 2 arguments are passed
            s=a+b
            #return s
        else:
            s=a
           # print(s) #if only one argument is passed,execute this block
        return s


d =student(40 ,60)
print(d.m1)
print(d.sum(50,90 ))

