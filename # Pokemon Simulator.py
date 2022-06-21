# Pokemon Simulator
# Date: 14/06/22
# By: Samuel Collinson

import random


enemy_pokemon = ["Volbeat", "Pidegy", "Flapple", "Magby", "Toxicroak", "Exeggcute",
"Tympole", "Porygon", "Typhlosion", "Shieldon", "Ludicolo", "Venomoth",
"Pyroar", "Delibird", "Hatterene", "Wailme", "Gligar", "Electrike"]


user_pokemon = ["Thwackey", "Snover", "Salamence", "Caterpie", "Grubbin",
"Simipour", "Pangoro", "Golem", "Nidoran", "Nidorino",
"Lugia", "Quilladin", "Aggron", "Milcery", "Houndoom",
"Tsareena", "Malamar", "Silcoon", "Gallade", "Drizzile"]

print("Original list \n")
print(enemy_pokemon)
random.shuffle(enemy_pokemon)
print("Randomized new list \n")
print(enemy_pokemon)

random.shuffle(user_pokemon)
num = 0
for i in range(3):
    num = num + 1
    print(f"{num}. {user_pokemon[i]}")
print(f"You will be battling against: {enemy_pokemon[0]}")