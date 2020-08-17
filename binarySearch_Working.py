#pos = -1

pos = -1

def binsearch(list ,x):
    lower = 0
    upper = len(list)-1

    while lower <= upper:
        mid = (lower + upper) // 2
        if list[mid] == x:
            globals()['pos'] = mid
            return  True
        else:
            if list[mid] < x:
                lower = mid
            else:
                upper=mid

list =[4,5,8,9,10,21,23,25,45,6,98,14,26,78,59]
x =3
if binsearch(list,x):
    print("found :", x, 'position :', pos)
else:
    print("not fount in the list")