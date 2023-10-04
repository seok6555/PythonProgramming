import random

dice = [0, 0, 0, 0, 0, 0]

def roll_the_dice(count):
    rolled_dice = [0, 0, 0, 0, 0, 0]

    for i in range(count):
        randomNumber = random.randrange(0, 6)
        rolled_dice[randomNumber] += 1

    return rolled_dice

roll_count_input = int(input("주사위의 총 횟수는? "))

while(True):
    if not(roll_count_input > 0):
        roll_count_input = int(input("주사위의 총 횟수는? "))
        continue
    else:
        dice = roll_the_dice(roll_count_input)

        for index in range(len(dice)):
            print(index + 1, "의 눈의 횟수는", dice[index], "회, 비율은", dice[index] / roll_count_input)
        break