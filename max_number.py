

def find_max(numbers):
    maximum = numbers[0]
    for item in numbers:
        if item > maximum :
            maximum = item
    return maximum


number = [10,5,30,25,6,12]
num = find_max(number)
print(num)
