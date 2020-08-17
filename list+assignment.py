numbers = [6,7,8,2,1,5,6,2,1]

unique = []
for item in numbers:
    if item not in unique:
        unique.append(item)

print(unique)
