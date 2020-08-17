num1 =int(input("enter a number :"))
num2 = int(input("enter another  number :"))

try:
    num =num1 /num2
    print(num)
except:
    num =0
    print("zero is not possible :" ,num)