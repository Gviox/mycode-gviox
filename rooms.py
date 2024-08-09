rooms = {
    'Bedroom': {
        'description': "You are in a dimly lit room with a single door to the north. There’s a chest that looks like it can be opened with a key.",
        'exits': {'north': 'Hallway'},
        'items': [],
        'locked': False,
        'chest_locked': True,
        'chest_content': 'Mysterious Ball'
        },
    'Hallway': {
        'description': "This room is filled with old bookshelves. There are doors north, south, east, and west.",
        'exits': {'south': 'Bedroom', 'east': 'Living Room', 'west': 'Study', 'north': 'Kitchen'},
        'items': [],
        'locked': False,
        'person': {
            'name': 'Old Man',
            'dialogue': "Answer my question correctly, and I'll give you something valuable.",
            'has_key': 'Key 2',
            'question': "Which Professor invented the Pokedex?",
            'answer': ["Professor Oak", "Oak", "oak"]
        }
    },
    'Kitchen': {
        'description': "You find yourself in a room with a strange, flickering light. There are doors to the south.",
        'exits': {'south':'Hallway'},
        'items': ['Lemonade'],
        'locked': False,
        'person': {
            'name': 'Mysterious Woman',
            'dialogue': "If you can answer my riddle, I'll give you something you need.",
            'has_key': 'Key 1',
            'question': "How many pokemon were first introduced in 1995?",
            'answer':["151", "151 pokemon"]
            }
    },
    'Study': {
        'description': "A quiet study filled with ancient tomes and a single exit to the east.",
        'exits': {'east': 'Hallway'},
        'items': [],
        'locked': False,
        'person': {
            'name': 'Quiz Master',
            'dialogue': "Answer this and I’ll give you the final key.",
            'has_key': 'Key 3',
            'question': "Which Pokémon is known as the Thunderbolt Pokémon?",
            'answer':{ "Pikachu", "pikachu"}
        }
    },
   'Living Room': {
        'description': "You enter a large room with a door that looks like an exit! You can feel electricity in the air. They hallway is to the west.",
        'exits': {'north': 'Exit', 'west' : 'Hallway'},
        'items': [],
        'locked': True,
        'monster': True,
        'required_keys': ['Key 1', 'Key 2', 'Key 3']
    }
}
