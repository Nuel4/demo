comd =""
started = False
while True:
    comd = input("> ").lower()
    if comd == "start":
        if started:
            print("car already is already on..........")
        else:
            started =True
            print("car  started.......")


    elif comd == "stop":
        if not  started:
            print("car already stopped.")
        else:
            started = False
            print("car stopped !")


    elif comd == "quit":
        print("quit !")
        break

    elif comd =="help":
        print("""
START - start the car
Stop  - stop the car
quit - to quit
        """)

    elif comd =="quit":
        break

    else:
        print("wrong choice  , Not recognized")

