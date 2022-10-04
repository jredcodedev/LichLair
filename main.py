current_room = 'Cave Entrance'
inventory = []
play_again = True
commands = ('North', 'South', 'East', 'West',
            'get Phylactery Piece(1)',
            'get Phylactery Piece(2)',
            'get Phylactery Piece(3)',
            'get Phylactery Piece(4)',
            'get Secret Room Key',
            'get Storage Room Key')
rooms = {'Cave Entrance':
             {'item': None,
              'locked': False,
              'north': 'Dungeon',
              'south': 'Foyer',
              'east': 'Laboratory',
              'west': 'Interrogation Room'
              },
         'Interrogation Room':
             {'item': 'Phylactery Piece(1)',
              'locked': False,
              'north': None,
              'south': None,
              'east': 'Cave Entrance',
              'west': None
              },
         'Dungeon':
             {'item': 'Phylactery Piece(2)',
              'locked': False,
              'north': None,
              'south': 'Cave Entrance',
              'east': 'Secret Room',
              'west': None
              },
         'Storage Room':
             {'item': 'Phylactery Piece(3)',
              'locked': True,
              'north': None,
              'south': 'Laboratory',
              'east': None,
              'west': None
              },
         'Secret Room':
             {'item': 'Phylactery Piece(4)',
              'locked': True,
              'north': None,
              'south': None,
              'east': None,
              'west': 'Dungeon'
              },
         'Laboratory':
             {'item': 'Secret Room Key',
              'locked': False,
              'north': 'Storage Room',
              'south': None,
              'east': None,
              'west': 'Cave Entrance'
              },
         'Foyer':
             {'item': 'Storage Room Key',
              'locked': False,
              'north': 'Cave Entrance',
              'south': None,
              'east': 'Throne Room',
              'west': None
              },
         'Throne Room':
             {'item': 'Lich',
              'locked': False,
              'north': None,
              'south': None,
              'east': None,
              'west': 'Foyer'}
         }


def display_info():
    print('\nYou are in the {}'.format(current_room))
    print('Inventory :', inventory)
    if rooms[current_room]['item'] is not None:
        print('You see a', rooms[current_room]['item'])
    print('-' * 30)
    if current_room != 'Throne Room':
        print('Enter your move:')


def move_player(direction):
    if rooms[current_room][direction] is not None:
        next_room = rooms[current_room][direction]
        if rooms[next_room]['locked']:
            if rooms[current_room][direction] + ' Key' in inventory:
                return rooms[current_room][direction]
            else:
                return 'locked room'
        else:
            return rooms[current_room][direction]
    else:
        return 'no path'


def try_get_item(item):
    if rooms[current_room]['item'] != item:
        return 'not here'
    else:
        return 'item here'


def process_command(command):
    if command not in commands:
        return 'Invalid command'
    else:
        if command == 'North':
            return move_player('north')
        elif command == 'South':
            return move_player('south')
        elif command == 'East':
            return move_player('east')
        elif command == 'West':
            return move_player('west')
        elif command == 'get Phylactery Piece(1)':
            return try_get_item('Phylactery Piece(1)')
        elif command == 'get Phylactery Piece(2)':
            return try_get_item('Phylactery Piece(2)')
        elif command == 'get Phylactery Piece(3)':
            return try_get_item('Phylactery Piece(3)')
        elif command == 'get Phylactery Piece(4)':
            return try_get_item('Phylactery Piece(4)')
        elif command == 'get Storage Room Key':
            return try_get_item('Storage Room Key')
        elif command == 'get Secret Room Key':
            return try_get_item('Secret Room Key')


if __name__ == '__main__':
    while play_again:
        print('Welcome to the Lich\'s Lair!')
        print('Collect all 4 pieces of the Lich\'s Phylactery to ensure his defeat is final.')
        print('Move commands: North, South, East, West')
        print('Pick up item: get \'item name\'')

        while True:
            display_info()
            if current_room == 'Throne Room':
                if len(inventory) == 6:
                    print('After a long fight, you vanquish the Lich.')
                    print('As you are celebrating your victory, the Lich begins to rise.')
                    print('You quickly smash the Phylactery Pieces and the Lich grows still.')
                    print('Congratulations! You win!')
                    break
                else:
                    print('After a long fight, you vanquish the Lich.')
                    print('As you are celebrating your victory, the Lich begins to rise.')
                    print('You ready yourself fight again but are too exhausted to continue.')
                    print('You lose!')
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
            else:
                current_room = command_results

        print('Thank you for playing!')

        while True:
            print('\nPlay again? (y/n)')
            user_choice = input()
            if user_choice == 'y':
                play_again = True
                current_room = 'Cave Entrance'
                break
            elif user_choice == 'n':
                play_again = False
                break
            else:
                print('Invalid input')
