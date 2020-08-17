class Human:
    
    def __init__(self ,name ,occupation):
        self.name =name
        self.occupation = occupation
        
    def profession(self):
        if self.occupation == "actor":
            
            print(self.name ," is an actor")
            
        elif self.occupation == "footballer":
            print(self.name ,"is a footballer")
            
        elif self.occupation =="programmer":
            print(self.name ," is a software developer")
        
        else:
            print(" You are not recognized here")
            
    def person(self):
        print(self.name ,"says hello")


employee =Human("Emmanuel Nuel" ,"footballer")
employee.profession()
employee.person()

employee2 =Human('Nathaniel Amos' ,'programmer')
employee2.profession()
employee2.person()
        
        