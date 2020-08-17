tup = ('ka' ,'ki' ,'rt' ,'up')
print(tup[-4 :-1])
print(tup[-1:-3],'checking')


print(type(tup))
x = ("apple", "banana", "cherry")
y = list(x)
print('y:' ,y)
y[1] = "kiwi"
#y[3]=10
x = tuple(y)

print(x)


thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")


thistuple = ("apple", "banana", "cherry")
print(len(thistuple))



tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)