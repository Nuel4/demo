import  random

for i in range(5):
    print(random.randint(10,20))    # to chose random numbers from 10 20


members  = ['Mary' ,'kosi','Moses' ,'mike' ,'Nuel' ,'Emma']
le = random.choice(members)
print(le)

class dice:
    def roll(self):
        first = random.randint(1,6)
        sec = random.randint(1,6)
        return first ,sec


dc = dice()
print(dc.roll())