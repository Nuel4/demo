a= 20
b =0

try:
    ans = a/b
    print(ans)
    print('resource opened')
except Exception as e:
    print("wrong input. zero can not divide a number:",e)
else:
    print('correct answer:')

finally:
    print('resource closed')