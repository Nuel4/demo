import  random
class Dice:
    def roll_dice(self):
        first =random.randint(1,6)
        second = random.randint(1,10)
        return first ,second


dice_number = Dice()
number=dice_number.roll_dice()
print(number)
print(dice_number.roll_dice())