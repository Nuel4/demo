ps = - 1  # counting position


def binary(lst, x):         # list of variable and the item to be searched
    low = 0                     # lower bound
    upp = len(lst) - 1              # length of the list (-1) counting from 0

    while low <= upp:                  # lower bound should be less than the upper bound since the position is starting from 0
        mid = (low + upp) // 2                # add lower bound position which 0 + the lenghtof the list and divid by 2

        if lst[mid] == x:                   # if mid position is == x (the item being searched)
            globals()['ps'] = mid                 # pos = the position
            return True                             # return confirm
        else:                                       # if lst[miid] is not equal or same item being looked for
            if lst[mid] < x:                         # midpint value is less than the item
                low = mid                              # lower bound should be equal to mid
            else:
                upp = mid                                 # x,the item is greater than mid point, upper bound should be equal to mid


lst = [10, 25, 58, 12, 56, 14, 29]
x = 1
if binary(lst, x):
    print(x, ' is available at :', ps)

else:
    print('item not found')