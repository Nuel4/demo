weight = int(input('weight :'))
unit = input('(l)bs or (k)kg :')
if unit.upper() == 'L':
    converter = weight * 0.45
    print(" your weight is :" , converter)

elif unit.upper() =='K':
    converter = weight / 0.45
    print(f"you are {converter} pounds")

else:
    print("wrong choice you entered")
