def sort(num):                          # define the function and pass the list name
    for i in range(len(num)-1 ,0 ,-1):   # traversing through the num  in descending order
        for j in range(i):                # second iteration
            if num[j] > num[j+1]:           # checking iff the first item is greater than the second index
                temp = num[j]                # swapping if greater
                num[j] = num[j+1]
                num[j+1] = temp

num =[415,61,72,23,45,120 ,100,4,8,11]        # list of number to sort
sort(num)                         # calling the function
print(num)