def search(lis, n):
    i = 0
    while i < len(lis):
        if lis[i] == n:
            return True
        i = i + 1

    return False


lis = [4, 5, 1, 6, 10, 8]
n = 50

if search(lis, n):
    print('found :' , n)
else:
    print("Not found")