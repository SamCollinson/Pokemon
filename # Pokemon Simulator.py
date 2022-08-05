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
        for i in range(1,5):
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

# ENEMY_POKEMONS = ["Volbeat", "Magnemite", "Flapple", "Magby", "Toxicroak", "Exeggcute",
# "Tympole", "Porygon", "Typhlosion", "Shieldon", "Ludicolo", "Venomoth",
# "Pyroar", "Delibird", "Hatterene", "Wailmer", "Gligar", "Electrike", "Yungoos"]

# ENEMY_POKEMON_HEALTH = {"Volbeat": 65, "Magnemite": 25, "Flapple": 70, "Magby": 45, "Toxicroak": 83 , "Exeggcute": 60,
# "Tympole": 50 , "Porygon": 65, "Typhlosion": 78, "Shieldon": 30, "Ludicolo": 80, "Venomoth": 70,
# "Pyroar": 86, "Delibird": 45, "Hatterene": 57, "Wailmer": 130, "Gligar": 65, "Electrike": 40, "Yungoos": 48}

# ENEMY_POKEMON_ATTACK = {"Volbeat": 73, "Magnemite": 35, "Flapple": 110, "Magby": 75, "Toxicroak": 106 , "Exeggcute": 40,
# "Tympole": 50 , "Porygon": 60, "Typhlosion": 84, "Shieldon": 42, "Ludicolo": 70, "Venomoth": 65,
# "Pyroar": 68, "Delibird": 55, "Hatterene": 90, "Wailmer": 70, "Gligar": 75, "Electrike": 45, "Yungoos": 70}

# ENEMY_POKEMON_DEFENSE = {"Volbeat": 75, "Magnemite": 70, "Flapple": 80, "Magby": 37, "Toxicroak": 65 , "Exeggcute": 80,
# "Tympole": 40 , "Porygon": 70, "Typhlosion": 78, "Shieldon": 118, "Ludicolo": 70, "Venomoth": 60,
# "Pyroar": 72, "Delibird": 45, "Hatterene": 95, "Wailmer": 35, "Gligar": 105, "Electrike": 40, "Yungoos": 30}

# ENEMY_POKEMON_SPEED = {"Volbeat": 85, "Magnemite": 45, "Flapple": 70, "Magby": 83, "Toxicroak": 85 , "Exeggcute": 40,
# "Tympole": 64 , "Porygon": 85, "Typhlosion": 100, "Shieldon": 30, "Ludicolo": 70, "Venomoth": 90,
# "Pyroar": 106, "Delibird": 65, "Hatterene": 29, "Wailmer": 60, "Gligar": 85, "Electrike": 65, "Yungoos": 45}

# ENEMY_POKEMON_TYPES = {"Volbeat": ["Bug"], "Magnemite": ["Electric", "Steel"], "Flapple": ["Grass", "Dragon"], "Magby": ["Fire"], "Toxicroak": ["Poison", "Fighting"] , "Exeggcute": ["Grass", "Psychic"],
# "Tympole": ["Water"] , "Porygon": ["Normal"], "Typhlosion": ["Fire"], "Shieldon": ["Rock", "Steel"], "Ludicolo": ["Water", "Grass"], "Venomoth": ["Bug", "Poison"],
# "Pyroar": ["Fire", "Normal"], "Delibird": ["Ice", "Flying"], "Hatterene": ["Psychic", "Fairy"], "Wailmer": ["Water"], "Gligar": ["Ground", "Flying"], "Electrike": ["Electric"], "Yungoos":["Normal"]}


# USER_POKEMONS = ["Thwackey", "Snover", "Salamence", "Caterpie", "Grubbin",
# "Simipour", "Pangoro", "Golem", "Nidoran", "Nidorino",
# "Lugia", "Quilladin", "Aggron", "Milcery", "Houndoom",
# "Tsareena", "Malamar", "Silcoon", "Gallade", "Drizzile"]

# USER_POKEMON_HEALTH = {"Thwackey": 70, "Snover": 60, "Salamence": 95, "Caterpie": 45, "Grubbin": 47,
# "Simipour": 75, "Pangoro": 95, "Golem": 80, "Nidoran": 55, "Nidorino": 61,
# "Lugia": 106, "Quilladin": 61, "Aggron": 70, "Milcery": 45, "Houndoom": 75,
# "Tsareena": 72, "Malamar": 86, "Silcoon": 50, "Gallade": 68, "Drizzile": 65}

# USER_POKEMON_ATTACK = {"Thwackey": 85, "Snover": 62, "Salamence": 135, "Caterpie": 30, "Grubbin": 62,
# "Simipour": 98, "Pangoro": 124, "Golem": 120, "Nidoran": 47, "Nidorino": 72,
# "Lugia": 90, "Quilladin": 78, "Aggron": 110, "Milcery": 40, "Houndoom": 90,
# "Tsareena": 120, "Malamar": 92, "Silcoon": 35, "Gallade": 125, "Drizzile": 60}

# USER_POKEMON_DEFENSE = {"Thwackey": 70, "Snover": 50, "Salamence": 80, "Caterpie": 35, "Grubbin": 45,
# "Simipour": 63, "Pangoro": 78, "Golem": 130, "Nidoran": 52, "Nidorino": 57,
# "Lugia": 130, "Quilladin": 95, "Aggron": 180, "Milcery": 40, "Houndoom": 50,
# "Tsareena": 98, "Malamar": 88, "Silcoon": 55, "Gallade": 65, "Drizzile": 55}

# USER_POKEMON_SPEED = {"Thwackey": 80, "Snover": 40, "Salamence": 100, "Caterpie": 45, "Grubbin": 46,
# "Simipour": 101, "Pangoro": 58, "Golem": 45, "Nidoran": 41, "Nidorino": 65,
# "Lugia": 110, "Quilladin": 57, "Aggron": 50, "Milcery": 34, "Houndoom": 95,
# "Tsareena": 72, "Malamar": 73, "Silcoon": 15, "Gallade": 80, "Drizzile": 90}

# USER_POKEMON_TYPES = {"Thwackey": ["Grass"], "Snover": ["Grass", "Ice"], "Salamence": ["Dragon", "Flying"], "Caterpie": ["Bug"], "Grubbin": ["Bug"],
# "Simipour": ["Water"], "Pangoro": ["Fighting", "Dark"], "Golem": ["Rock", "Ground"], "Nidoran": ["Poison"], "Nidorino": ["Poison"],
# "Lugia": ["Psychic", "Flying"], "Quilladin": ["Grass"], "Aggron": ["Steel", "Rock"], "Milcery": ["Fairy"], "Houndoom": ["Dark", "Fire"],
# "Tsareena": ["Grass"], "Malamar": ["Dark", "Psychic"], "Silcoon": ["Bug"], "Gallade": ["Pyschic", "Fighting"], "Drizzile": ["Water"]}


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
    print(f"{enemy_pokemon[0]}: {enemy_pokemon[5], enemy_pokemon[6]}, lvl {enemy_level}, {enemy_pokemon_hp}hp , atk {enemy_pokemon_attack}, def {enemy_pokemon_defense}")

def enemy_pokemon_moves():
    for move in moves:
        move_type = moves[move][0]
        if move_type == enemy_pokemon[5]:
            possible_moves.append(moves[move])
        elif move_type == enemy_pokemon[6]:
            possible_moves.append(moves[move])
        else:
            random_num = random.randint(1, 200)
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
    print(f"{user_choice[0][0]}: {user_choice[0][5], user_choice[0][6]}, lvl {user_level}, {user_pokemon_hp}hp , atk {user_pokemon_attack}, def {user_pokemon_defense}")

user_pokemon_stats()


