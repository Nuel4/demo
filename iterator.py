num =[10,30,25,35,15,20,90]
#for i in num:  for loop
   # print(i)  print num indexwise

n =iter(num)  # built in_function called iter ,pass list into iter
print(n.__next__())  # will give the first value
print(n.__next__())  # gives second index value
print(next(n))

class topten:
    def __init__(self):
        self.number =1 # start from 1

    def  __iter__(self):
        return self  # returns itself

    def __next__(self):
        if self.number<=10: # should be <= 10
            val = self.number
            self.number += 1 # increament number by 1
            return val
        else:
            raise StopIteration # to stop iteration


value = topten()
print(next(value))

for i in value:  #using for loop to print the values of value
    print(i)
