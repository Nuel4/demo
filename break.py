av=10

intake =int(input('enter the quantity u want:'))
i =1
while i <=intake:
    print('chocolate: ' ,i)
    i +=1
    if i >av:
        print("out of stock")
        break

