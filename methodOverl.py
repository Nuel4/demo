class student:
    def show(self):
        print('welcome to overriding')


class subject(student):
    def show(self):  # method overriding.same method name but the child class method will override parent class method
        print('python is very  sweet to learn')

s =subject()
s.show()
