f = open('yourfile','w')
f.write('this is for beginners.\n Anybody can learn it. it is  easy to learn.\n ypu are welcome on board.\n feel free to ask questions if u get confused')


with open("yourfile",'r') as p:
    n =p.read()
    print(n)
    p.close()


f = open('myfile.txt','w')
f.write('this is for beginners.\n Anybody can learn it. it is  easy to learn.\n ypu are welcome on board.\n feel free to ask questions if u get confused')


d = open('myfile.txt')
print(d.read())