exp =[123,45,67,78]
total = 0
for i in exp:
    total += i
    print(total)

print('Total :' ,total)


expense =[100,250,500,600]
total_amount =0

for item in range(len(expense)):
    print("index :" , item +1 , "amount :" ,expense[item])
    total_amount +=expense[item]
    print("each addition :" ,total_amount)

print('Total Amount :' ,total_amount)