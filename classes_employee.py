class emp:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def pat(self):
        print("name :", self.name, "age :", self.age)
        #print('salary :', self.amt)

    def update(self):
        self.name = 'nuel'

da = emp("mike" ,16)
da.pat()
da.update()