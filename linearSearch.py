ps = -1


def look(lst, x):
    n = 0
    for i in range(len(lst)):

        if lst[i] == x:
            globals()['ps'] = n
            return True
        n =n+1

    return False


lst = [100, 111, 122, 133, 144, 155, 166]
x = 155
if look(lst, x):
    print('item found :', x, 'at index :', ps)

else:
    print('not available')