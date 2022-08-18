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
all_enemy_stats = []
start_enemy_health = 0
enemy_level =  random.randint(40, 60)

def enemy_pokemon_stats():
    enemy_pokemon_hp = int(((2 * enemy_pokemon[1]) * enemy_level) / 100) + enemy_level + 10
    enemy_pokemon_attack = int(((2 * enemy_pokemon[2]) * enemy_level) / 100) + 5
    enemy_pokemon_defense = int(((2 * enemy_pokemon[3]) * enemy_level) / 100) + 5
    enemy_pokemon_speed = int(((2 * enemy_pokemon[4]) * enemy_level) / 100) + 5
    all_enemy_stats.extend([enemy_level, enemy_pokemon[5], enemy_pokemon[6] ,enemy_pokemon_hp, enemy_pokemon_attack, enemy_pokemon_defense, enemy_pokemon_speed])
    print(f"{enemy_pokemon[0]}:")
    print(f"""    Level: {enemy_level}
    Type: {enemy_pokemon[5]}, {enemy_pokemon[6]}
    Health: {all_enemy_stats[3]}""")


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
    move_chance = random.randint(1, 4)
    enemy_move = possible_moves[move_chance]
    print(f"{enemy_pokemon[0]} Used {enemy_move[0]}!")

user_pokemon_choices = []
user_choice = []
def pokemon_choice():
    print(f"You will be battling against: {enemy_pokemon[0]}\n")
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
                user_choice.extend(user_pokemon_choices[choice - 1])
                repeat = False
            else:
                print("Invalid choice")
        except:
            print("Please enter a number") 



all_user_stats = []
user_level =  random.randint(40, 60)

def user_pokemon_stats():
    user_pokemon_hp = int(((2 * user_choice[1]) * user_level) / 100) + user_level + 10
    user_pokemon_attack = int(((2 * user_choice[2]) * user_level) / 100) + 5
    user_pokemon_defense = int(((2 * user_choice[3]) * user_level) / 100) + 5
    user_pokemon_speed = int(((2 * user_choice[4]) * user_level) / 100) + 5
    all_user_stats.extend([user_level, user_choice[5], user_choice[6] ,user_pokemon_hp, user_pokemon_attack, user_pokemon_defense, user_pokemon_speed])
    print(f"{user_choice[0]}:")
    print(f"""    Level: {user_level}
    Type: {user_choice[5]}, {user_choice[6]}
    Health: {all_user_stats[3]}
--------------------------------------------""")

user_possible_moves = []
def user_pokemon_moves():
    if len(user_possible_moves) == 0:
        for move in moves:
            move_type = moves[move][1]
            if move_type == user_choice[5]:
                user_possible_moves.append(moves[move])
            elif move_type == user_choice[6]:
                user_possible_moves.append(moves[move])
            else:
                random_num = random.randint(1, 200)
                if random_num == 1:
                    user_possible_moves.append(moves[move])
                elif len(user_possible_moves) < 4:
                    user_possible_moves.append(moves[move])
        random.shuffle(user_possible_moves)
        

users_move_choice = []
def user_move_choice():
    user_pokemon_moves()
    print("\n")
    print("""----====================================----
                  MOVES
----====================================----""")
    num = 1
    for i in user_possible_moves[0: 4]:
        num_spaces = 25 - len(i[0])
        spaces = num_spaces * " "
        print(f"    {num}. {i[0]}{spaces}{i[2]}pp")
        num +=1
    print("--------------------------------------------")
    move_choice = int(input("Which move would you like to use? "))
    users_move_choice.extend(user_possible_moves[move_choice - 1])
    print(f"{user_choice[0]} used {users_move_choice[0]}!")

def user_damage():
        crit_chance = random.randint(0, 255)
        if crit_chance == 1:
            crit = 2
            print("CRITICAL HIT!")
        else:
            crit = 1
        global user_damages
        user_damages = 2 * all_user_stats[0] * crit / 5 + 2 * int(users_move_choice[4]) * all_user_stats[4] / all_user_stats[5] / 50 + 2
        print(f"{user_choice[0]} Did {int(user_damages)} Damage To {enemy_pokemon[0]}!")

def enemy_damage():
    enemy_pokemon_moves()
    crit_chance = random.randint(0, 255)
    if crit_chance == 1:
        crit = 2
        print("CRITICAL HIT!")
    else:
        crit = 1
    global enemy_damages
    enemy_damages = 2 * all_enemy_stats[0] * crit / 5 + 2 * int(possible_moves[0][4]) * all_enemy_stats[4] / all_enemy_stats[5] / 50 + 2
    print(f"{enemy_pokemon[0]} Did {int(enemy_damages)} Damage To {user_choice[0]}!")
    
    
def user_health():
    health = all_user_stats[3]
    if health <= 0:
        print(f"{user_choice[0]} Has Fainted!")
        fainted = "yes"
        return fainted
    else:
        health = int(health - enemy_damages)
        all_user_stats[3] = health
        print(f"{user_choice[0]} Has {all_user_stats[3]}hp left!")

def enemy_health():
    health = all_enemy_stats[3]
    if health <= 0:
        print(f"{enemy_pokemon[0]} Has Fainted!")
        fainted = "yes"
        return fainted
    else:
        health = int(health - user_damages)
        all_enemy_stats[3] = health
        print(f"{enemy_pokemon[0]} Has {all_enemy_stats[3]}hp left!")

def speed():
    if all_enemy_stats[5] < all_user_stats[5]:
        start = "user"
    elif all_enemy_stats[5] > all_user_stats[5]:
        start = "enemy"
    else:
        random_num = random.randint(1, 2)
        if random_num == 1:
            start = "user"
        else:
            start = "enemy"
    print(start)
    return start
    
def pokemon_stats():
    enemy_pokemon_stats()
    user_pokemon_stats()


def battling():
    enemy_pokemon_stats()
    pokemon_choice()
    user_pokemon_stats()
    repeat = True
    while repeat:
        if speed() == "user":
            print(f"{user_choice[0]} attacks first!")
            print("-------------------------------------")
            user_move_choice()
            user_damage()
            enemy_damage()
            print("-------------------------------------")
            if enemy_health() == "yes":
                print("You lost!")
                repeat = False
                         
        else:
            print(f"{enemy_pokemon[0]} attacks first!")
            print("-------------------------------------")
            enemy_damage()
            user_move_choice()
            user_damage()  
            print("-------------------------------------")
            if user_health() == "yes":
                print("You Won!")
                repeat = False          





battling()

