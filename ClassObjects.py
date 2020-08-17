class compute:
    def __init__(self , ram ,cpu):
        self.ram =ram
        self.cpu =cpu

    def configg(self):
        print("congiguration:" ,self.cpu, self.ram)


com =compute("16 gb" ,24)
com1 = compute("8 gb" ,36)
com1.configg()
com.configg()