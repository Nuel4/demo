matrix = [
    [3,5,7,8],
    [6,4,7,9],
    [10,4,6,2]
]

matrix[2][1] = 20
print(matrix[0])
print(matrix[2][3])
print(matrix[2])
print(matrix[2][1])
print(matrix[1])

print("............new begining.............")
for row in matrix:
    print(row)

print("............new begining.............")
for ite in matrix:
    for it in ite:
        print(it)