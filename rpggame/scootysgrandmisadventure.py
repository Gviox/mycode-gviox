#!/usr/bin/python3

# importing from a different file
from rooms import rooms

inventory = []
currentRoom = 'Bedroom'

def showInstructions():
    print('''
    RPG Game
    =======
    Commands:
    go [direction]
    get [item]
    ''')

def showStatus():
    global currentRoom
    print('======================')
    print('You are currently located in the ' + currentRoom)
    print(rooms[currentRoom]['description'])
    print('======================')


# New method for interacting with a person
def interact_with_person(room, player_inventory):
    if 'person' in room:
        person = room['person']
        print(f"{person['name']} says: {person['dialogue']}")
        user_answer = input(f"They ask: {person['question']} ").strip().lower()
        if user_answer in [str(answer).lower() for answer in person['answer']]:
            print("Correct! You have earned the key.")
            if person['has_key'] and person['has_key'] not in player_inventory:
                player_inventory.append(person['has_key'])
                print(f"You have received {person['has_key']}!")
                person['has_key'] = None
        else:
            print("Incorrect. The person shakes their head and refuses to give you the key.")
    else:
        print("There is no one here to interact with.")

# Method for opening chest
def open_chest(player_inventory):
    if 'Key 3' in player_inventory and rooms['Bedroom']['chest_locked']:
        rooms['Bedroom']['chest_locked'] = False
        print("You unlock the chest in the Bedroom. Inside, you find a mysterious red and white ball!")
        player_inventory.append('Mysterious Ball')
    else:
        print("The chest is locked. You need Key 3 to open it.")

# Method for facing monster
def face_monster(player_inventory):
    if 'Mysterious Ball' in player_inventory:
        print("You throw the mysterious ball at the monster. It gets captured inside!")
        rooms['Living Room']['monster'] = False
        rooms['Living Room']['locked'] = False
        return "The path is clear! You can now escape!"
    else:
        return "The monster shocks you! You need something special to capture it."

#Method to check for escape, if player has all keys, they can escape, if not, they get shocked by monster
def check_for_escape(player_inventory):
    required_keys = rooms['Living Room']['required_keys']
    if all(key in player_inventory for key in required_keys):
        if rooms['Living Room']['monster']:
            return face_monster(player_inventory)
        else:
            return "The door unlocks with a satisfying click. You can now escape!  The monster you captured breaks out of the ball! It jumps on your shoulder and rubs its cheek against yours! You've befriended a Pikachu!"
    else:
        return "The door is still locked. You need more keys to escape."
showInstructions()

while True:
    showStatus()

    move = input('>').lower().split(" ", 1)

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]['exits']:
            currentRoom = rooms[currentRoom]['exits'][move[1]]
            showStatus() #show the new room's description after moving
        else:
            print('You can\'t go that way!')

    if move[0] == 'get':
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory.append(move[1])
            print(move[1] + ' got!')
            del rooms[currentRoom]['item']
        else:
            print('Can\'t get ' + move[1] + '!')

    # Show room description if the room changes
    if currentRoom == 'Bedroom' and rooms['Bedroom']['chest_locked']:
        unlock = input("Do you want to unlock the chest? (yes/no) ").lower()
        if unlock == 'yes':
            open_chest(inventory)

    # Interact with a person in the room after showing the description
    if 'person' in rooms[currentRoom]:
        talk = input("Do you want to talk to the person here? (yes/no) ").lower()
        if talk == 'yes':
            interact_with_person(rooms[currentRoom], inventory)

     # Specific conditions for Living Room
    if currentRoom == 'Living Room':
        escape = input("Do you want to try escaping? (yes/no) ").lower()
        if escape == 'yes':
            escape_message = check_for_escape(inventory)
            print(escape_message)
            if "you can now escape!" in escape_message.lower():
                 break
                                                                                                                                                                                                                                                                       
