# Pokemon Simulator
# Date: 14/06/22
# By: Samuel Collinson

import random

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

enemy_pokemon = ["Volbeat", "Magnemite", "Flapple", "Magby", "Toxicroak", "Exeggcute",
"Tympole", "Porygon", "Typhlosion", "Shieldon", "Ludicolo", "Venomoth",
"Pyroar", "Delibird", "Hatterene", "Wailmer", "Gligar", "Electrike", "Yungoos"]

enemy_pokemon_health= {"Volbeat": 65, "Magnemite": 25, "Flapple": 70, "Magby": 45, "Toxicroak": 83 , "Exeggcute": 60,
"Tympole": 50 , "Porygon": 65, "Typhlosion": 78, "Shieldon": 30, "Ludicolo": 80, "Venomoth": 70,
"Pyroar": 86, "Delibird": 45, "Hatterene": 57, "Wailmer": 130, "Gligar": 65, "Electrike": 40, "Yungoos": 48}

enemy_pokemon_attack= {"Volbeat": 73, "Magnemite": 35, "Flapple": 110, "Magby": 75, "Toxicroak": 106 , "Exeggcute": 40,
"Tympole": 50 , "Porygon": 60, "Typhlosion": 84, "Shieldon": 42, "Ludicolo": 70, "Venomoth": 65,
"Pyroar": 68, "Delibird": 55, "Hatterene": 90, "Wailmer": 70, "Gligar": 75, "Electrike": 45, "Yungoos": 70}

enemy_pokemon_defense= {"Volbeat": 75, "Magnemite": 70, "Flapple": 80, "Magby": 37, "Toxicroak": 65 , "Exeggcute": 80,
"Tympole": 40 , "Porygon": 70, "Typhlosion": 78, "Shieldon": 118, "Ludicolo": 70, "Venomoth": 60,
"Pyroar": 72, "Delibird": 45, "Hatterene": 95, "Wailmer": 35, "Gligar": 105, "Electrike": 40, "Yungoos": 30}

enemy_pokemon_speed= {"Volbeat": 85, "Magnemite": 45, "Flapple": 70, "Magby": 83, "Toxicroak": 85 , "Exeggcute": 40,
"Tympole": 64 , "Porygon": 85, "Typhlosion": 100, "Shieldon": 30, "Ludicolo": 70, "Venomoth": 90,
"Pyroar": 106, "Delibird": 65, "Hatterene": 29, "Wailmer": 60, "Gligar": 85, "Electrike": 65, "Yungoos": 45}

enemy_pokemon_types = {"Volbeat": ["bug"], "Magnemite": ["electric", "steel"], "Flapple": ["grass", "dragon"], "Magby": ["fire"], "Toxicroak": ["poison", "fighing"] , "Exeggcute": ["grass", "psychic"],
"Tympole": ["water"] , "Porygon": ["normal"], "Typhlosion": ["fire"], "Shieldon": ["rock", "steel"], "Ludicolo": ["water", "grass"], "Venomoth": ["bug", "poison"],
"Pyroar": ["fire", "normal"], "Delibird": ["ice", "flying"], "Hatterene": ["psychic", "fairy"], "Wailmer": ["water"], "Gligar": ["ground", "flying"], "Electrike": ["electric"], "Yungoos":["normal"]}


user_pokemon = ["Thwackey", "Snover", "Salamence", "Caterpie", "Grubbin",
"Simipour", "Pangoro", "Golem", "Nidoran", "Nidorino",
"Lugia", "Quilladin", "Aggron", "Milcery", "Houndoom",
"Tsareena", "Malamar", "Silcoon", "Gallade", "Drizzile"]


random.shuffle(enemy_pokemon)
random.shuffle(user_pokemon)

def enemy_pokemon_stats():
    print(enemy_pokemon[0])
    for pokemon in enemy_pokemon_attack:
        if pokemon == enemy_pokemon[0]:
            for atk_stat in pokemon:
                print(atk_stat)

    


def user_choice():
    print(f"You will be battling against: {enemy_pokemon[0]}")
    for i in range(3):
        print(f"{i + 1}. {user_pokemon[i]}")
    repeat = True
    while repeat:
        try:
            choice = int(input("Which Pokemon would you like to use: "))
            if choice >= 1 and choice <= 3:
                print(f"You sent out {user_pokemon[choice - 1]}!")
                repeat = False
            else:
                print("Invalid choice")
        except:
            print("Please enter a number") 

# user_choice()
enemy_pokemon_stats()


