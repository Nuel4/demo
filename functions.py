
def calculate(exp):
    total = 0
    for item in exp:
        total  = total  + item
        print(total)

    return total
expense1 =[50,20,40,90]
expense2 =[60,10,45,67]
expense3 = [89,90,56,23,56,95]

ep1=calculate(expense1)
ep2 =calculate(expense2)
ep3 = calculate(expense3)
print("total expenses 1 :" ,ep1)
print("total expenses 2:" ,ep2)
print("total expenses 3:" ,ep3)