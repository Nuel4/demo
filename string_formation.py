user = "emmanuel"
action = 'run'
print('{a} {b}' .format(b=user ,a=action))

num = 1235
print('the code is {:1f}'.format(num))
print('{:.0f}'.format(num))

print("welcome here home .\n please make yourself comfortable")

n= 5799.9045860
print('{:.3f}'.format(n))

name = 'mike'
age = 20
pay = 15000
ph = 888776
print("first print:",' name:{} age :{} pay: {} phone :{}'.format(name,age,pay,ph))
print("second print\n-------\n"' name:{}\n age :{} \npay: {}\n phone :{}'.format(name,age,pay,ph))
print("Third print\n-------\n"' age:{a}\n phone:{b} \npay: {c}\n name:{d}'.format(d=name,a=age,c=pay,b=ph))