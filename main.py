current_room = 'Cave Entrance'
inventory = []
play_again = True
all_commands = ('North', 'South', 'East', 'West',
                'get Phylactery Piece(1)',
                'get Phylactery Piece(2)',
                'get Phylactery Piece(3)',
                'get Phylactery Piece(4)',
                'get Secret Room Key',
                'get Storage Room Key',
                'Exit')
move_commands = ('North', 'South', 'East', 'West')
item_commands = ('get Phylactery Piece(1)',
                 'get Phylactery Piece(2)',
                 'get Phylactery Piece(3)',
                 'get Phylactery Piece(4)',
                 'get Secret Room Key',
                 'get Storage Room Key')
rooms = {'Cave Entrance': {
    'item': None,
    'locked': False,
    'North': 'Dungeon',
    'South': 'Foyer',
    'East': 'Laboratory',
    'West': 'Interrogation Room'
},
    'Interrogation Room': {
        'item': 'Phylactery Piece(1)',
        'locked': False,
        'North': None,
        'South': None,
        'East': 'Cave Entrance',
        'West': None
    },
    'Dungeon': {
        'item': 'Phylactery Piece(2)',
        'locked': False,
        'North': None,
        'South': 'Cave Entrance',
        'East': 'Secret Room',
        'West': None
    },
    'Storage Room': {
        'item': 'Phylactery Piece(3)',
        'locked': True,
        'North': None,
        'South': 'Laboratory',
        'East': None,
        'West': None
    },
    'Secret Room': {
        'item': 'Phylactery Piece(4)',
        'locked': True,
        'North': None,
        'South': None,
        'East': None,
        'West': 'Dungeon'
    },
    'Laboratory': {
        'item': 'Secret Room Key',
        'locked': False,
        'North': 'Storage Room',
        'South': None,
        'East': None,
        'West': 'Cave Entrance'
    },
    'Foyer': {
        'item': 'Storage Room Key',
        'locked': False,
        'North': 'Cave Entrance',
        'South': None,
        'East': 'Throne Room',
        'West': None
    },
    'Throne Room': {
        'item': 'Lich',
        'locked': False,
        'North': None,
        'South': None,
        'East': None,
        'West': 'Foyer'}
}


def try_move_player(direction):
    next_room = rooms[current_room][direction]
    if next_room is not None:
        if rooms[next_room]['locked']:
            if next_room + ' Key' in inventory:
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
        elif command == 'Exit':
            return command


def print_intro():
    print('Welcome to the Lich\'s Lair!')
    print('Collect all 4 pieces of the Lich\'s Phylactery to ensure his defeat is final.')
    print('-' * 30)
    print('How to play:')
    print('To move, enter a direction: North, South, East, West')
    print('To pick up an item: get \'item name\'')
    print('To leave the game: Exit')


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
        print('You see a', rooms[current_room]['item'])
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

            command_results = process_command(input())

            if command_results == 'Invalid command':
                print('Invalid command')
            elif command_results == 'no path':
                print('There is no path in that direction.')
            elif command_results == 'not here':
                print('That item is not here.')
            elif command_results == 'item here':
                inventory.append(rooms[current_room]['item'])
                print('{} added to inventory'.format(rooms[current_room]['item']))
                rooms[current_room]['item'] = None
            elif command_results == 'locked room':
                print('That room is locked, find the key.')
            elif command_results == 'Exit':
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
