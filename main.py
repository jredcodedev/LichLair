import string

current_room = 'Cave Entrance'
inventory = []
play_again = True
all_commands = ('north', 'south', 'east', 'west',
                'get phylactery piece(1)',
                'get phylactery piece(2)',
                'get phylactery piece(3)',
                'get phylactery piece(4)',
                'get secret room key',
                'get storage room key',
                'exit')
move_commands = ('north', 'south', 'east', 'west')
item_commands = ('get phylactery piece(1)',
                 'get phylactery piece(2)',
                 'get phylactery piece(3)',
                 'get phylactery piece(4)',
                 'get secret room key',
                 'get storage room key')
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


def try_move_player(direction):
    next_room = rooms[current_room][direction]
    if next_room is not None:
        if rooms[next_room]['locked']:
            if string.capwords(next_room) + ' Key' in inventory:
                return next_room
            else:
                return 'locked room'
        else:
            return next_room
    else:
        return 'no path'


def try_get_item(item):
    if rooms[current_room]['item'] != item:
        return 'not here'
    else:
        return 'item here'


def process_command(command):
    if command not in all_commands:
        return 'Invalid command'
    else:
        if command in move_commands:
            return try_move_player(command)
        elif command in item_commands:
            return try_get_item(command.lstrip('get '))
        elif command == 'exit':
            return command


def print_intro():
    print('Welcome to the Lich\'s Lair!')
    print('Collect all 4 pieces of the Lich\'s Phylactery to ensure his defeat is final.')
    print('-' * 30)
    print('How to play:')
    print('To move, enter a direction: North, South, East, West')
    print('To pick up an item: get \'item name\'')
    print('To leave the game: exit')


def print_win_message():
    print('After a long fight, you vanquish the Lich.')
    print('As you are celebrating your victory, the Lich begins to rise.')
    print('You quickly smash the Phylactery Pieces and the Lich grows still.')
    print('Congratulations! You win!')


def print_lose_message():
    print('After a long fight, you vanquish the Lich.')
    print('As you are celebrating your victory, the Lich begins to rise.')
    print('You ready yourself fight again but are too exhausted to continue.')
    print('You lose!')


def display_player_info():
    print('\nYou are in the {}'.format(current_room))
    print('Inventory :', inventory)
    if rooms[current_room]['item'] is not None:
        print('You see a', string.capwords(rooms[current_room]['item']))
    print('-' * 30)
    if current_room != 'Throne Room':
        print('Enter your move:')


if __name__ == '__main__':
    while play_again:
        print_intro()

        while True:
            display_player_info()

            if current_room == 'Throne Room':
                if len(inventory) == 6:
                    print_win_message()
                    break
                else:
                    print_lose_message()
                    break

            command_results = process_command(input().lower())

            if command_results == 'Invalid command':
                print('Invalid command')
            elif command_results == 'no path':
                print('There is no path in that direction.')
            elif command_results == 'not here':
                print('That item is not here.')
            elif command_results == 'item here':
                inventory.append(string.capwords(rooms[current_room]['item']))
                print('{} added to inventory'.format(string.capwords(rooms[current_room]['item'])))
                rooms[current_room]['item'] = None
            elif command_results == 'locked room':
                print('That room is locked, find the key.')
            elif command_results == 'exit':
                play_again = False
                break
            else:
                current_room = command_results

        print('Thank you for playing!')

        while play_again:
            print('\nPlay again? (y/n)')
            user_choice = input()
            if user_choice == 'y':
                current_room = 'Cave Entrance'
                break
            elif user_choice == 'n':
                play_again = False
                break
            else:
                print('Invalid input')
