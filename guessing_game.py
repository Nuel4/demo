number =9
guess_count =0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("guess:"))
    guess_count += 1
     #if guess_count ==3:   correct but else statement is a better way to write it
       # print("you failed")
      #  break

    if guess ==number:
        print(f"you won! {guess} is correct")
        break
else:
    print("you failed")