with open('profile.txt','r')  as myfile :
    lines = myfile.read()
    print(lines)

with open('profile.txt' ,mode='a') as yourfile:
    li = yourfile.write('My phone number is 8867589262 and my email address is nuel4xelence@gmail.com\n contact me if you need to me.')
    yourfile.close()