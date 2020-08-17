import random
num =random.random()
print(num)
nu = random.uniform(1,10)
print(nu ,num)
mem = random.choices(['man','monkey' ,'marry' ,'mango'])
print(mem)
me =['girl' ,'girlish' ,'gally' ,'goal']
m=random.choice(me)
print(m)

mm =random.choices(me)
print(mem ,m)
co =['nigeria' ,'canada' ,'america','ghana' ,'china']
c = random.choices(co ,k=3)
print(c)
d = random.choices(co ,weights=[50,30,20,1,50] ,k=3)
print(d)

la = range(1,20)
print(la)

laa =list(range(2,10))
print(laa)
random.shuffle(laa)
print(laa)


sa = random.sample(laa ,k=5)
print(sa)