command = ""
started = False
while True:
    command = input("> :").lower()
    if command =="start":
        if started:
            print("car is already on.....")
        else:
            started = True
            print("car started ........... ")

    elif command == "stop":
        if not started:
            print(" car is already stopped ......")
        else:
            started = False
            print("car stopped !!!")

    elif command =="help":
        print("""
START - start the car
STOP - stop the car
Quit -  Quit        
        """)
    elif command =="quit":
        print("bye")
        break

    else:
        print("not recognized. wrong choice")

