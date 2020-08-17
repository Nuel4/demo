def something():
    yield  'man'
    yield  'woman'
    yield  'children'
    yield 'grand child'



k =something()
print(k.__next__())
print(k.__next__())

print("\n........................\n")
print(next(k))
print(next(k))