def fact(n):
    if n == 0:
        return 1
    for i in range(n):
        f = n * fact(n-1)
        return f



k = fact(10)
print('k  value:' ,k)
