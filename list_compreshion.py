#list comprehension

s ='something'

print([letter for letter in s])
b = 'everything'
my = [lett for lett in b]
print(my)
a =' everything in life is for us to use for our own good'
print('.....list comprehension......')
bb=[word[0] for word in a.split()]
print(bb)

print('.....spliting a range of word.....')
print(a.split())

print('........spliting letter .....')
for word in a:
    print(word)

print('........spliting word .....')
for word in a.split():
    print(word)

print('........spliting word based a letter.....')
wording = 'Secreet Agents Are Supper Good At Staying Hidden'
for word in wording.split():
    first = word.lower()[0]
    if first == 's':
        print(word)



print('.......square .........')
sqt = [x**2 for x in range(0 ,11)]
print(sqt)

print('............even numbers.............')
even = [y for y in range(0,21) if y%2 == 0]
print(even)


