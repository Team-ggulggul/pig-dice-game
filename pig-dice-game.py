from random import randint



def select_level():
    pass

def easy_mode():
    pass

def roll_dice():
    roll_dice = randint(1,6)
    return roll_dice

def e_computer_play():
    pass

def user_play():
    is_play = True
    point_box = 0
    dice_value = 0

    while is_play == True:
        
        print(f"point box: {point_box}")
        rb = input("R or B: ")
        dice_value = roll_dice()

        if rb == 'b':
            # if select bank, get out of while
            is_play = False
        elif rb == 'r':
        # if first dice is one, game end 
            if dice_value == 1:
                print("dice value: 1")
                # user get lose point
                point_box = 0
                is_play = False
            else: 
                print(f"dice value: {dice_value}")
                point_box += dice_value
                continue
    print(f"point box: {point_box}")
    # in the end, return value is point
    return point_box

if __name__ == '__main__':
    print("start")
    select_level()
    user_play()






