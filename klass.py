class compute:

    def __init__(self, ram, cpu):
        self.ram = ram
        self.cpu = cpu

    def details(self):
        print("congiguration:", self.cpu, self.ram)

    def det(self):
        compute.details()

    def payment(self, x):
        self.x = x
        print('total amount paid is :', x)


kom = compute("12 gb" , "ram 16")
kom.details()
kom.payment(25000)