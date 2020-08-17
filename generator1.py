def topfive():
    n= 1
    while n <=10:
        sig =n*n
        yield sig
        n +=1

num =topfive()

for x in num:
    print(x)
