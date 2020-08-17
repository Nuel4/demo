number = [5 , 2, 5 ,2,2]

for x in number:

    print("* " * x)

print("..........the end .................")
for x_count in number:
    output = ""
    for y_count in range(x_count):
        output += " x"

    print(output)