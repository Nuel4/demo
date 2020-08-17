class test:
    name = "lesson 101"

    def __init__(self):
        print("object created.")

    def __del__(self):
        print("object destroyed")


p = test()
print(p.name)