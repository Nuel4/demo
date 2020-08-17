def Topten():

    yield 50
    yield 51
    yield 52
    yield 53
    yield 54
    # return 5 will return 5 without yeild


s =Topten()
print(s.__next__() ,'sss')
print(next(s))

print("\n .........................")
for i in s:
    print(i)