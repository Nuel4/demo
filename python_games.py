number = 7
counter = 3

def game():
    global counter
    name = input("enter your name:")
    num1 =int(input("enter a number:"))
    while num1 !=number:
        print("Wrong answer:")
        counter -= 1
        print(counter)
        num1 =int(input("reenter a number:"))

        if counter==1:
            if num1 ==number:
                pass
                #print("congratulations ,you won! at stage: " ,counter)
                #print("Name :" + name)
            else:
                print("game ove! You failed all")
                break



    else:
        print(" You won")
        print(" Name :" + name ,'won at stage:', counter)

    print(name)

game()