# Pokemon Simulator
# Date: 14/06/22
# By: Samuel Collinson


import random
import csv

moves = {}
with open("move_data.csv", mode="r") as move_data:
    reader = csv.reader(move_data)
    for row in reader:
        moves[row[0]] = []
        for i in range(0,5):
            moves[row[0]].append(row[i])

enemy_pokemons_stats = {}
user_pokemons_stats = {}
with open("Pokemon_table.csv", mode="r") as pokemon_table:
    pokemon_reader = csv.reader(pokemon_table)
    for pokemon_row in pokemon_reader:
        pokemon_id = int(pokemon_row[0])
        if pokemon_id <= 19:
            enemy_pokemons_stats[pokemon_row[0]] = []
            for num in range(1,8):
                enemy_pokemons_stats[pokemon_row[0]].append(pokemon_row[num])
            for i in range(1, 5):
                enemy_pokemons_stats[pokemon_row[0]][i] = int(enemy_pokemons_stats[pokemon_row[0]][i])
        else:
            user_pokemons_stats[pokemon_row[0]] = []
            for num in range(1,8):
                user_pokemons_stats[pokemon_row[0]].append(pokemon_row[num])
            for i in range(1, 5):
                user_pokemons_stats[pokemon_row[0]][i] = int(user_pokemons_stats[pokemon_row[0]][i])




print("""------------------------------------------------
            !!!!!!DISCLAIMER!!!!!
------------------------------------------------

© 2022 Pokémon. © 1995–2022 Nintendo/Creatures Inc./GAME FREAK inc. Pokémon, Pokémon character names, Nintendo Switch, Nintendo 3DS, Nintendo DS, Wii, Wii U, and WiiWare are trademarks of Nintendo.
The YouTube logo is a trademark of Google Inc. Other trademarks are the property of their respective owners.

Distribution in any form and any channels now known or in the future of derivative works based on the copyrighted property trademarks,
service marks, trade names and other proprietary property (Fan Art) of The Pokémon Company International,
Inc., its affiliates and licensors (Pokémon) constitutes a royalty-free,
non-exclusive, irrevocable, transferable, sub-licensable, worldwide license from the Fan Art's creator to Pokémon to use,
transmit, copy, modify, and display Fan Art (and its derivatives) for any purpose.
No further consideration or compensation of any kind will be given for any Fan Art.
Fan Art creator gives up any claims that the use of the Fan Art violates any of their rights,
including moral rights, privacy rights, proprietary rights publicity rights,
rights to credit for material or ideas or any other right, including the right to approve the way such material is used.
In no uncertain terms, does Pokémon's use of Fan Art constitute a grant to Fan Art's creator to use the Pokémon intellectual property or Fan Art beyond a personal,
noncommercial home use.
------------------------------------------------\n""")

enemy_id, enemy_stats = random.choice(list(enemy_pokemons_stats.items()))
enemy_pokemon = enemy_stats


possible_moves = []
enemy_types = []
def enemy_pokemon_stats():
    enemy_level =  random.randint(40, 60)
    enemy_pokemon_hp = int(((2 * enemy_pokemon[1]) * enemy_level) / 100) + enemy_level + 10
    enemy_pokemon_attack = int(((2 * enemy_pokemon[2]) * enemy_level) / 100) + 5
    enemy_pokemon_defense = int(((2 * enemy_pokemon[3]) * enemy_level) / 100) + 5
    enemy_pokemon_moves()
    print(f"{enemy_pokemon[0]}:")
    print(f"""    Level: {enemy_level}
    Type: {enemy_pokemon[5]}, {enemy_pokemon[6]}
    Health: {enemy_pokemon_hp}""")

def enemy_pokemon_moves():
    for move in moves:
        move_type = moves[move][1]
        if move_type == enemy_pokemon[5]:
            possible_moves.append(moves[move])
        elif move_type == enemy_pokemon[6]:
            possible_moves.append(moves[move])
        else:
            random_num = random.randint(1, 100)
            if random_num == 1:
                possible_moves.append(moves[move])
    random.shuffle(possible_moves)

user_pokemon_choices = []
user_choice = []
def pokemon_choice():
    print(f"You will be battling against: {enemy_pokemon[0]}\n")
    enemy_pokemon_stats()
    print("""----====================================----     
             Pokemon Choices
----====================================----""")
    for i in range(0, 5):
        user_id, user_stats = random.choice(list(user_pokemons_stats.items()))
        user_pokemon_choices.append(user_stats)
        del user_pokemons_stats[user_id]
        print(f"    {i + 1}. {user_pokemon_choices[i][0]}")
    repeat = True
    while repeat:
        try:
            print("--------------------------------------------")
            choice = int(input("Which Pokemon would you like to use: "))
            if choice >= 1 and choice <= 5:
                print(f"You sent out {user_pokemon_choices[choice - 1][0]}!")
                user_choice.append(user_pokemon_choices[choice - 1])
                repeat = False
            else:
                print("Invalid choice")
        except:
            print("Please enter a number") 

def user_pokemon_stats():
    pokemon_choice()
    user_level =  random.randint(40, 60)
    user_pokemon_hp = int(((2 * user_choice[0][1]) * user_level) / 100) + user_level + 10
    user_pokemon_attack = int(((2 * user_choice[0][2]) * user_level) / 100) + 5
    user_pokemon_defense = int(((2 * user_choice[0][3]) * user_level) / 100) + 5
    print(f"{user_choice[0][0]}:")
    print(f"""    Level: {user_level}
    Type: {user_choice[0][5]}, {user_choice[0][6]}
    Health: {user_pokemon_hp}""")
    user_pokemon_moves()

user_possible_moves = []
def user_pokemon_moves():
    for move in moves:
        move_type = moves[move][1]
        if move_type == user_choice[0][5]:
            user_possible_moves.append(moves[move])
        elif move_type == user_choice[0][6]:
            user_possible_moves.append(moves[move])
        else:
            random_num = random.randint(1, 200)
            if random_num == 1:
                user_possible_moves.append(moves[move])
            elif len(user_possible_moves) < 4:
                user_possible_moves.append(moves[move])
    random.shuffle(user_possible_moves)
    print("""----====================================----
                  MOVES
----====================================----""")
    for i in user_possible_moves[0: 4]:
        num_spaces = 25 - len(i[0])
        spaces = num_spaces * " "
        print(f"{i[0]}{spaces}{i[2]}pp")




user_pokemon_stats()

