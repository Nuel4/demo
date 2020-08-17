import  random

for i in range(3):
    print(random.random())
    number=random.randint(10 ,20)
    print(f"random value is : {number}")

members =['Nuel' ,'Mash' ,'Mary' ,'John', 'Mark']
leader =random.choice(members)  # random.choice to pick a member -string value
print(leader)