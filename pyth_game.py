number = 7
counter = 3
totalSocore =30
stage =1

def game():
    global counter,totalSocore ,stage
    name = input("enter your name:")
    num1 =int(input("enter a number:"))
    while num1 !=number:
        print("Wrong answer:")
        counter -= 1
        totalSocore -=10
        stage +=1
        print(counter)
        num1 =int(input("reenter a number:"))

        if counter==1:
            if num1 ==number:
                pass
                #print("congratulations ,you won! at stage: " ,counter)
                #print("Name :" + name)
            else:
                totalSocore=0
                print("game ove! You failed all")
                print(" Name :" + name, '\n', 'Won nothing')
                print("Total Score :", totalSocore)
                break



    else:
        print(" You won ,Congartulation!")
        print(" Name :" + name ,'\n' ,'won at stage:', stage)
        print("Total Score :", totalSocore)



game()