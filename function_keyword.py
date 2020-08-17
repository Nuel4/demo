def func(name, **others):
    print(name)
    for i,j in others.items():

        print(i ,j)


func("mike" ,address="lagos" ,age =32,phone=9876555,status='married')