with open('C:\\Users\emman\Desktop\ book.txt' ,'r') as f:
     p=f.read()
     print(p)

import  json

boo = json.loads(p)
print(boo)
print(type(boo))
print(type(p))
print(boo['Mark'])
print(boo['Mark']['phone'])

for person in boo:
    print(boo[person])