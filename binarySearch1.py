pos = -1
def binsearch(list ,n):
    lower = 0
    upper = len(list)-1
    while lower <= upper:
        midpoint = (lower + upper) // 2

        if list[midpoint] == n:
            globals()['pos'] = midpoint
            return True
        else:
            if list[midpoint] < n:
                lower = midpoint
            else:
                upper = midpoint



list =[4,5,8,9,10,21,23,25,45,6,98,14,26,78,59]
n=6
if binsearch(list,n):
    print("found :",n ,'position :',pos)
else:
    print("not fount in the list")