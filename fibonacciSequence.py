def series(intake):
    num1 =0
    num2 =1

    if intake ==1:
        print(num1)

    else:
        print(num1 ,num2)

    for i in range(2,intake):
        number =num1 + num2
        num1  = num2
        num2  = number
        print(number)

series(10)