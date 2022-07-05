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

ENEMY_POKEMONS = ["Volbeat", "Magnemite", "Flapple", "Magby", "Toxicroak", "Exeggcute",
"Tympole", "Porygon", "Typhlosion", "Shieldon", "Ludicolo", "Venomoth",
"Pyroar", "Delibird", "Hatterene", "Wailmer", "Gligar", "Electrike", "Yungoos"]

ENEMY_POKEMON_HEALTH = {"Volbeat": 65, "Magnemite": 25, "Flapple": 70, "Magby": 45, "Toxicroak": 83 , "Exeggcute": 60,
"Tympole": 50 , "Porygon": 65, "Typhlosion": 78, "Shieldon": 30, "Ludicolo": 80, "Venomoth": 70,
"Pyroar": 86, "Delibird": 45, "Hatterene": 57, "Wailmer": 130, "Gligar": 65, "Electrike": 40, "Yungoos": 48}

ENEMY_POKEMON_ATTACK = {"Volbeat": 73, "Magnemite": 35, "Flapple": 110, "Magby": 75, "Toxicroak": 106 , "Exeggcute": 40,
"Tympole": 50 , "Porygon": 60, "Typhlosion": 84, "Shieldon": 42, "Ludicolo": 70, "Venomoth": 65,
"Pyroar": 68, "Delibird": 55, "Hatterene": 90, "Wailmer": 70, "Gligar": 75, "Electrike": 45, "Yungoos": 70}

ENEMY_POKEMON_DEFENSE = {"Volbeat": 75, "Magnemite": 70, "Flapple": 80, "Magby": 37, "Toxicroak": 65 , "Exeggcute": 80,
"Tympole": 40 , "Porygon": 70, "Typhlosion": 78, "Shieldon": 118, "Ludicolo": 70, "Venomoth": 60,
"Pyroar": 72, "Delibird": 45, "Hatterene": 95, "Wailmer": 35, "Gligar": 105, "Electrike": 40, "Yungoos": 30}

ENEMY_POKEMON_SPEED = {"Volbeat": 85, "Magnemite": 45, "Flapple": 70, "Magby": 83, "Toxicroak": 85 , "Exeggcute": 40,
"Tympole": 64 , "Porygon": 85, "Typhlosion": 100, "Shieldon": 30, "Ludicolo": 70, "Venomoth": 90,
"Pyroar": 106, "Delibird": 65, "Hatterene": 29, "Wailmer": 60, "Gligar": 85, "Electrike": 65, "Yungoos": 45}

ENEMY_POKEMON_TYPES = {"Volbeat": ["Bug"], "Magnemite": ["Electric", "Steel"], "Flapple": ["Grass", "Dragon"], "Magby": ["Fire"], "Toxicroak": ["Poison", "Fighing"] , "Exeggcute": ["Grass", "Psychic"],
"Tympole": ["Water"] , "Porygon": ["Normal"], "Typhlosion": ["Fire"], "Shieldon": ["Rock", "Steel"], "Ludicolo": ["Water", "Grass"], "Venomoth": ["Bug", "Poison"],
"Pyroar": ["Fire", "Normal"], "Delibird": ["Ice", "Flying"], "Hatterene": ["Psychic", "Fairy"], "Wailmer": ["Water"], "Gligar": ["Ground", "Flying"], "Electrike": ["Electric"], "Yungoos":["Normal"]}


USER_POKEMONS = ["Thwackey", "Snover", "Salamence", "Caterpie", "Grubbin",
"Simipour", "Pangoro", "Golem", "Nidoran", "Nidorino",
"Lugia", "Quilladin", "Aggron", "Milcery", "Houndoom",
"Tsareena", "Malamar", "Silcoon", "Gallade", "Drizzile"]


random.shuffle(ENEMY_POKEMONS)
random.shuffle(USER_POKEMONS)


ENEMY_POKEMON = []
enemy_pokemon_types = []
def enemy_pokemon_stats():
    enemy_level =  random.randint(40, 60)
    print(enemy_level)
    enemy_pokemon_hp = int(((2 * ENEMY_POKEMON_HEALTH[ENEMY_POKEMONS[0]]) * enemy_level) / 100) + enemy_level + 10
    print(f"{enemy_pokemon_hp}hp")
    enemy_pokemon_attack = int(((2 * ENEMY_POKEMON_ATTACK[ENEMY_POKEMONS[0]]) * enemy_level) / 100) + 5
    print(enemy_pokemon_attack)

    for i in ENEMY_POKEMON_TYPES:
        if i == ENEMY_POKEMONS[0]:
            for type in ENEMY_POKEMON_TYPES[i]:
                enemy_pokemon_types.append(type)
            print(enemy_pokemon_types)
    print(ENEMY_POKEMON_TYPES[ENEMY_POKEMONS[0]])
    for move in moves:
        print(moves[move])
        for i in moves[move]:
            for type in moves[move][i]:
                print(type)
    
            

    ENEMY_POKEMON.extend([ENEMY_POKEMONS[0], enemy_level,ENEMY_POKEMON_TYPES[ENEMY_POKEMONS[0]],
    ENEMY_POKEMON_ATTACK[ENEMY_POKEMONS[0]], ENEMY_POKEMON_DEFENSE[ENEMY_POKEMONS[0]],
    ENEMY_POKEMON_SPEED[ENEMY_POKEMONS[0]], ENEMY_POKEMON_HEALTH[ENEMY_POKEMONS[0]]])
    print(ENEMY_POKEMON)

    


def user_choice():
    print(f"You will be battling against: {ENEMY_POKEMONS[0]}\n")
    # enemy_pokemon_stats()
    print("""----=========================================----
                  POKEMON CHOICES     
----=========================================----""")
    for i in range(5):
        print(f"    {i + 1}. {USER_POKEMONS[i]}")
    repeat = True
    while repeat:
        try:
            print("--------------------------------------------")
            choice = int(input("    Which Pokemon would you like to use: "))
            if choice >= 1 and choice <= 5:
                print(f"You sent out {USER_POKEMONS[choice - 1]}!")
                repeat = False
            else:
                print("Invalid choice")
        except:
            print("Please enter a number") 


user_choice()



