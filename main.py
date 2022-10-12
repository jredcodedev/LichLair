import copy
import string


# check if room in direction and if room is locked, return status string or room
def try_move_player(direction, rooms, current_room, inventory):
    next_room = rooms[current_room][direction]
    if next_room is not None:  # if there is a room in direction
        if rooms[next_room]['locked']:  # if the room is locked
            if string.capwords(next_room) + ' Key' in inventory:  # if player has correct key
                return next_room
            else:
                return next_room + ' locked'
        else:
            return next_room
    else:
        return 'no path'


# check if item is in room
def try_get_item(item, rooms, current_room):
    if rooms[current_room]['item'] != item:
        return 'not here'
    else:
        return 'item here'


# process player command and return appropriate status string
def process_command(command, all_commands, move_commands, item_commands, rooms, current_room, inventory):
    if command not in all_commands:  # if command invalid
        return 'Invalid command'
    else:
        if command in move_commands:  # try to move player if command is a move command
            return try_move_player(command, rooms, current_room, inventory)
        elif command in item_commands:  # try to pick up item if command is item command
            return try_get_item(command.lstrip('get '), rooms, current_room)
        elif command == 'exit':  # if exit command, return status string
            return command


# print message depending on type: 'intro', 'win', or 'lose'
def print_message(message_type):
    if message_type == 'intro':
        print('Welcome to the Lich\'s Lair!')
        print('Collect all 4 pieces of the Lich\'s Phylactery to ensure his defeat is final.')
        print('-' * 30)
        print('How to play:')
        print('To move, enter a direction: North, South, East, West')
        print('To pick up an item: get \'item name\'')
        print('To leave the game: exit')
    elif message_type == 'win':
        print('After a long fight, you vanquish the Lich.')
        print('As you are celebrating your victory, the Lich begins to rise.')
        print('You quickly smash the Phylactery Pieces and the Lich grows still.')
        print('Congratulations! You win!')
    elif message_type == 'lose':
        print('After a long fight, you vanquish the Lich.')
        print('As you are celebrating your victory, the Lich begins to rise.')
        print('You ready yourself fight again but are too exhausted to continue.')
        print('You lose!')


# display player ui (current room, item in room, inventory)
def display_player_info(rooms, current_room, inventory):
    print('\nYou are in the {}'.format(current_room))  # current room
    print('Inventory :', inventory)  # player inventory
    if rooms[current_room]['item'] is not None:  # display item if there is one
        print('You see a', string.capwords(rooms[current_room]['item']))
    print('-' * 30)
    if current_room != 'Throne Room':  # don't ask for new move if in final room
        print('Enter your move:')


def main():
    current_room = 'Cave Entrance'  # track current room
    inventory = []  # track player inventory
    play_again = True

    # all valid commands
    all_commands = ('north', 'south', 'east', 'west',
                    'get phylactery piece(1)',
                    'get phylactery piece(2)',
                    'get phylactery piece(3)',
                    'get phylactery piece(4)',
                    'get secret room key',
                    'get storage room key',
                    'exit')
    # only movement commands
    move_commands = ('north', 'south', 'east', 'west')
    # only item commands
    item_commands = ('get phylactery piece(1)',
                     'get phylactery piece(2)',
                     'get phylactery piece(3)',
                     'get phylactery piece(4)',
                     'get secret room key',
                     'get storage room key')

    # room connections, items, and lock status
    rooms = {'Cave Entrance': {
        'item': None,
        'locked': False,
        'north': 'Dungeon',
        'south': 'Foyer',
        'east': 'Laboratory',
        'west': 'Interrogation Room'
        },
        'Interrogation Room': {
            'item': 'phylactery piece(1)',
            'locked': False,
            'north': None,
            'south': None,
            'east': 'Cave Entrance',
            'west': None
        },
        'Dungeon': {
            'item': 'phylactery piece(2)',
            'locked': False,
            'north': None,
            'south': 'Cave Entrance',
            'east': 'Secret Room',
            'west': None
        },
        'Storage Room': {
            'item': 'phylactery piece(3)',
            'locked': True,
            'north': None,
            'south': 'Laboratory',
            'east': None,
            'west': None
        },
        'Secret Room': {
            'item': 'phylactery piece(4)',
            'locked': True,
            'north': None,
            'south': None,
            'east': None,
            'west': 'Dungeon'
        },
        'Laboratory': {
            'item': 'secret room key',
            'locked': False,
            'north': 'Storage Room',
            'south': None,
            'east': None,
            'west': 'Cave Entrance'
        },
        'Foyer': {
            'item': 'storage room key',
            'locked': False,
            'north': 'Cave Entrance',
            'south': None,
            'east': 'Throne Room',
            'west': None
        },
        'Throne Room': {
            'item': 'Lich',
            'locked': False,
            'north': None,
            'south': None,
            'east': None,
            'west': 'Foyer'}
    }

    default_rooms = copy.deepcopy(rooms)  # copy of rooms for resetting for play again

    while play_again:  # if play again is true
        print_message('intro')  # intro message

        while True:  # main game loop
            display_player_info(rooms, current_room, inventory)  # show ui

            if current_room == 'Throne Room':  # if player is in boss room
                if len(inventory) == 6:  # if player has all items
                    print_message('win')
                    break
                else:
                    print_message('lose')
                    break

            # store status string or new room
            command_results = process_command(input().lower(),
                                              all_commands,
                                              move_commands,
                                              item_commands,
                                              rooms,
                                              current_room,
                                              inventory)

            if command_results == 'Invalid command':  # if player command is invalid
                print('Invalid command')
            elif command_results == 'no path':  # if there is no room in direction
                print('There is no path in that direction.')
            elif command_results == 'not here':  # if the item is not in the room
                print('That item is not here.')
            elif command_results == 'item here':  # if the item is in the room
                inventory.append(string.capwords(rooms[current_room]['item']))  # add item to inventory
                print('{} added to inventory'.format(string.capwords(rooms[current_room]['item'])))  # inform player
                rooms[current_room]['item'] = None  # remove item from room
            elif command_results == 'Storage Room locked':  # if next room is locked storage room
                print('The storage room is locked, find the key.')
            elif command_results == 'Secret Room locked':  # if next room is locked secret room
                print('The secret room is locked, find the key.')
            elif command_results == 'exit':  # if exit command is given
                play_again = False
                break
            else:  # if no status string, update current room
                current_room = command_results

        print('Thank you for playing!')

        while play_again:  # while player wants to play again
            print('\nPlay again? (y/n)')
            user_choice = input()
            if user_choice == 'y':  # if yes, reset rooms, current room, and inventory and continue
                current_room = 'Cave Entrance'
                rooms = copy.deepcopy(default_rooms)
                inventory.clear()
                break
            elif user_choice == 'n':  # if no, exit game
                play_again = False
                break
            else:  # if input was not 'y' or 'n'
                print('Invalid input')


if __name__ == '__main__':
    main()
