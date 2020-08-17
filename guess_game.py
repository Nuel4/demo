number = 20

guess_number = 0
guess_limit = 3

while guess_number < guess_limit :
    guess = int(input("guess:"))
    guess_number += 1

    if guess == number:
        print(f"congratulations! {guess} is correct")
        break

else:
    print("you failed ")