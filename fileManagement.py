my=open('profile.txt' ,'w')
my.write('My name is Nuel.\n I am a Nigerian. i study in india .\n i plan to move to canada soonest')
my.close()

you = open('profile.txt' ,'r')
print(you.read())