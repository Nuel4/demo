from array import *

f = array('i', [])
intake = int(input('enter the lenght:'))

for q in range(intake):
    h = int(input('enter the values :'))
    f.append(h)

print(f)

cnt = 0
nn = int(input('enter a number to be searched :'))
for qq in f:
    if qq == nn:
        print('found', cnt)
        break

    else:
        f.append(nn)
        print('number not found but added:')
        break

print(f)