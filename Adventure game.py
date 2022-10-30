import time            # import time to sleep some times
import random          # import random  to select random objects
# Define function to print messages


def print_pause(message_to_print):
    print(message_to_print + '\n ')
    time.sleep(2)



def valid_input(prompt, option1, option2):
    while True:
        change = input(prompt).lower()
        if option1 in change:
            break
        elif option2 in change:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return change

#The list of the objects used in the game
places = ['forest', 'desert', 'house']
weapons = ['sword', 'knife', 'gun', 'rock']
forest_monster = ['bear', 'rabbit', 'lion', 'wolf', 'monkey']
desert_monster = ['alien', 'giant monster', 'snake', 'dog']
house_monster = ['cat', 'dog', 'rat']
game_result = ['win', 'lose']

# intro for the game


def intro():
    print_pause('Welcome to the game of adventure fun game')
    print_pause('takes you to another world of fun and thrill')
    print_pause('We will help you during the game choices,' +
                ' but you have to think well ' +
                'before each selection so you can win ')
# user can put his name to start the game


intro()
name = input('Please Enter your Name to start the game \n')
time.sleep(2)
print_pause('Welcome to the game ' + name + ' !! ')
print_pause('Please Choose which place you want to play \n')
# to select place
for place in places:
    print_pause(place)
choice = ''
while choice not in places:
    choice = input('Give me your choice \n ' +
                   'for forest write F or forest or 1 \n' +
                   'for desert write desert or D or 2 \n' +
                   'for house  write house or H or 3 \n')
    if choice .lower() == 'Forest' or choice == 'F' or choice == '1':
        choice = 'forest'
    elif choice.lower() == 'Desert' or choice == 'D' or choice == '2':
        choice = 'desert'
    elif choice .lower() == 'House' or choice == 'H' or choice == '3':
        choice = 'house'
    else:
        choice = ''
time.sleep(2)
# to give the user random weapon


print_pause('you have a  random weapon')
weapon_choosed = (random.choice(weapons))
print_pause(weapon_choosed)
# to know if the user want to change the weapon


def change():
    change_request = valid_input('do you like to change weapon ?\n',
                                 'yes', 'no')
    if 'yes' in change_request:
        print_pause(random.choice(weapons))
    elif 'no' in change_request:
        print_pause('okay!!')
    print_pause('you now in ' + choice + ' and ' + ' you have weapon ' +
                weapon_choosed)
    print_pause('now you see in fornt of you ')
    if choice == 'forest':
        print_pause(random.choice(forest_monster))
    if choice == 'desert':
        print_pause(random.choice(desert_monster))
    if choice == 'house':
        print_pause(random.choice(house_monster))


change()


def play():
    choose = valid_input('You have the the choice to run or attack \n',
                         'attack', 'run')
    if 'attack' in choose:
        print_pause('You win')
    elif 'run' in choose:
        print_pause('You fall in a hole You lost !! ')


play()
print('Game Over ')
