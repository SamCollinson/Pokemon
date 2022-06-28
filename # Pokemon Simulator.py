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
"Pyroar", "Delibird", "Hatterene", "Wailme", "Gligar", "Electrike", "Yungoos"]


user_pokemon = ["Thwackey", "Snover", "Salamence", "Caterpie", "Grubbin",
"Simipour", "Pangoro", "Golem", "Nidoran", "Nidorino",
"Lugia", "Quilladin", "Aggron", "Milcery", "Houndoom",
"Tsareena", "Malamar", "Silcoon", "Gallade", "Drizzile"]

random.shuffle(enemy_pokemon)
print("Original list\n", user_pokemon)
random.shuffle(user_pokemon)
print("\nRandomized list\n", user_pokemon)
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

user_choice()