import os
from termcolor import colored

# Prompt
def prompt():
    print(colored(
        "\t\t\tWelcome player\n\nYou must collect all six items before fighting the boss.\n\nMoves:\t'go {direction}' (travel north, south, east or west)\n\t'get {item}' (add nearby item to inventory)\n\n", color="light_yellow"))

    input("Press any key to continue > ")

# Clear screen
def clear():
    os.system('cls' if os.system == 'nt' else 'clear')


# Rooms
rooms = {
    'Liminal Space': {'North': 'Mirror Maze', 'South': 'Bat Cavern', 'East': 'Bazaar'},
    'Mirror Maze': {'South': 'Liminal Space', 'Item': 'Crystal'},
    'Bat Cavern': {'North': 'Liminal Space', 'East': 'Volcano', 'Item': 'Staff'},
    'Bazaar': {'West': 'Liminal Space', 'North': 'Meat Locker', 'East': 'Dojo', 'Item': 'Altoids'},
    'Meat Locker': {'South': 'Bazaar', 'East': 'Quicksand Pit', 'Item': 'Fig'},
    'Quicksand Pit': {'West': 'Meat Locker', 'Item': 'Robe'},
    'Volcano': {'West': 'Bat Cavern', 'Item': 'Elderberry'},
    'Dojo': {'West': 'Bazaar', 'Boss': 'Shadow Man'}
}

# Track items
vowels = ['a', 'e', 'i', 'o', 'u']

# List to track inventory
inventory = []

# Staring room
current_room = "Liminal Space"

# Result of last move
msg = ""

clear()
prompt()

# Game loop
while True:

    # Clear screen
    clear()

    # Display player info:
    print(f"You are in the {current_room}\nInventory: {inventory}\n{'-' *27}")

    # Display message
    print(msg)

    # Item indicator
    if "Item" in rooms[current_room].keys():

        nearby_item = rooms[current_room]["Item"]

        if nearby_item not in inventory:

            # Pural
            if nearby_item[-1] == 's':
                print(colored(f"You see {nearby_item}", color="light_magenta"))

            # Singular starts with vowels
            elif nearby_item[0] in vowels:
                print(
                    colored(f"You see an {nearby_item}", color="light_magenta"))

            # Singular starts with constant
            else:
                print(
                    colored(f"You see an {nearby_item}", color="light_magenta"))

    # Boss Encounter
    if "Boss" in rooms[current_room].keys():

        # Lose
        if len(inventory) < 6:
            print(
                colored(f"You lost a fight with {rooms[current_room]['Boss']}!", color="red"))

        # Win
        else:
            print(
                colored(f"You beat the {rooms[current_room]['Boss']}!", color="green"))
            break

    # Players moves as input
    user_input = input("Enter your move:\n>")

    # Split moves
    next_move = user_input.split(' ')

    # First word is action
    action = next_move[0].title()

    # Reset item and direction
    item = "Item"
    direction = "null"

    if len(next_move) > 1:
        item = next_move[1:]
        direction = next_move[1].title()
        item = " ".join(item).title()

    # Moving between rooms
    if action == "Go":

        try:
            current_room = rooms[current_room][direction]
            msg = f"You travel {direction}"

        except:
            msg = colored("You can't go that way.", color="light_red")

    elif action == "Get":
        try:
            if item == rooms[current_room]["Item"]:

                if item not in inventory:
                    inventory.append(rooms[current_room]["Item"])
                    msg = colored(f"{item} retrieved!", color="light_green")

                else:
                    msg = colored(
                        f"You already have the {item}!", color="yellow")

            else:
                msg = colored(f"Can't find {item}", color="red")

        except:
            msg = colored(f"Can't find {item}", color="red")

     # Exit program
    elif action == "Exit":
        print(colored("Exited the game!", color="red"))
        break

    # Any other commands invalid
    else:
        msg = "Invalid command"
