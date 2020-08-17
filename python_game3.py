number ,number2,number3 = 7 ,13 ,33
counter,count2,count3 = 6, 4, 3
totalSocore ,totalSocore2,totalSocore3 =30 ,20, 30
stage =1
game1,game2,game3 =1,2,3


def game():
    global counter,count2 ,count3, totalSocore,totalSocore2,totalSocore3 ,stage
    name = input("Enter your name :")
    print(name  , " Please select game type:")
    gametype = int(input("Press 1 for game 1.Press 2 for game 2 .Press 3 for game 3 :"))

    if gametype==game1:
        num1 = int(input("Pick a number between 1-10 :"))
        if num1 > 10:
            print("Number should not be greater than 10")

        else:
            while num1 != number:
                print("Wrong answer:")
                counter -= 1
                totalSocore -= 5
                stage += 1
                print("You have ", counter, "left")
                num1 = int(input("reenter a number:"))

                if counter == 1:
                    if num1 == number:
                        pass
                        # print("congratulations ,you won! at stage: " ,counter)
                        # print("Name :" + name)
                    else:

                        totalSocore = 0
                        print("game ove! You failed all")
                        print(" Name :" + name, '\n', 'Won nothing')
                        print("Total Score :", totalSocore)
                        break

            else:
                print(" You won ,Congartulation!")
                print("Game type :" , game1)
                print(" Name :" + name, '\n', 'won at stage:', stage)
                print("Total Score :", totalSocore)


    elif gametype ==game2:
        num2 = int(input("Pick a number between 1-20 :"))
        if  num2 > 20:
            print("Number should not be greater than 20")

        else:
            while num2 != number2:
                print("Wrong answer:")
                count2 -= 1
                totalSocore2 -= 5
                stage += 1
                print("You have ", count2, "left")
                num2 = int(input("reenter a number:"))

                if count2 == 1:
                    if num2 == number2:
                        pass

                    else:

                        totalSocore2 = 0
                        print("game ove! You failed all")
                        print(" Name :" + name, '\n', 'Won nothing')
                        print("Total Score :", totalSocore2)
                        break

            else:
                print(" You won ,Congartulation!")
                print("Game type :", game2)
                print(" Name :" + name, '\n', 'won at stage:', stage)
                print("Total Score :", totalSocore2)

    elif gametype ==game3:
        num3 = int(input("Pick a number between 1-50 :"))
        if num3 > 50:
            print("Number should not be greater than 50")

        else:
            while num3 != number3:
                print("Wrong answer:")
                count3 -= 1
                totalSocore3 -= 10
                stage += 1
                print("You have ", count3, "left")
                num3 = int(input("reenter a number:"))

                if count3 == 1:
                    if num3 == number3:
                        pass

                    else:

                        totalSocore3 = 0
                        print("game ove! You failed all")
                        print(" Name :" + name, '\n', 'Won nothing')
                        print("Total Score :", totalSocore3)
                        break

            else:
                print(" You won ,Congartulation!")
                print("Game type :", game2)
                print(" Name :" + name, '\n', 'won at stage:', stage)
                print("Total Score :", totalSocore3)

    else:
        print("Wrong game choice ")



game()