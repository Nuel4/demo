class pycharm:
    def execute(self):
        print("complie")
        print("runy our program")

class anacoda:
    def execute(self):   # should have same method name in the calling function
        print("spell check")
        print('conversion check')
        print("complie")
        print("runy our program")


class laptop:
    def code(self ,ide):
        ide.execute()  # the class must have same method_name (execute)


#id =pycharm()
id =anacoda()
lap =laptop()
lap.code(id)