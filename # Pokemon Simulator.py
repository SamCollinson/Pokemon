# Pokemon Simulator
# Date: 14/06/22
# By: Samuel Collinson


from doctest import run_docstring_examples
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
    again = True
    while again:
        print("\n")
        print("""----====================================----
                    MOVES
----====================================----""")
        num = 1
        for i in user_possible_moves[0: 4]:
            num_spaces = 25 - len(i[0])
            spaces = num_spaces * " "
            print(f"    {num}. {i[0]}")
            num +=1
        print("--------------------------------------------")
        try:
            global move_choice
            move_choice = int(input("Which move would you like to use? "))
            if move_choice >= 1 and move_choice <= 4:
                users_move_choice.extend(user_possible_moves[move_choice - 1])
                print("--------------------------------------------")
                print("\n")
                print(f"{user_choice[0]} used {user_possible_moves[move_choice - 1][0]}!")
                again = False
            else:
                print("Please enter a number from the choices")
        except:
            print("Please enter a number from the choices")

def user_fainted():
    if all_user_stats[3] <= 0:
        print(f"{user_choice[0]} Has Fainted!")
        fainted = "yes"
        return fainted        

def enemy_fainted():
    if all_enemy_stats[3] <= 0:
        print(f"{enemy_pokemon[0]} Has Fainted!")
        fainted = "yes"
        return fainted

def user_starts():
    if speed() == "user":
        repeat = True
        while repeat:
            print("\n")
            if user_fainted() == "yes":
                repeat == False
                exit()
            elif enemy_fainted() == "yes":
                repeat == False
                exit()
            print("--------------------------------------------")
            print("\n")
            print(f"{user_choice[0]} Attacks First!")
            if all_user_stats[3] > 0 and all_enemy_stats[3] > 0:
                user_move_choice()
                crit_chance = random.randint(0, 100)
                if crit_chance == 1:
                    crit = 2
                    print("CRITICAL HIT!")
                else:
                    crit = 1
                users_damage = 2 * all_user_stats[0] * crit / 5 + 2 * int(user_possible_moves[move_choice - 1][3]) * all_user_stats[4] / all_user_stats[5] / 50 + 2
                print(f"{user_choice[0]} Did {int(users_damage)} Damage To {enemy_pokemon[0]}!")
                enemys_health = all_enemy_stats[3]
                enemys_health = int(enemys_health - users_damage)
                all_enemy_stats[3] = enemys_health
                if user_fainted() == "yes":
                    repeat == False
                    exit()
                elif enemy_fainted() == "yes":
                    repeat == False
                    exit()
                # print(f"{enemy_pokemon[0]} Has {all_enemy_stats[3]}hp left!")
                print("\n")
                enemy_pokemon_moves()
                crit_chance = random.randint(0, 100)
                if crit_chance == 1:
                    crit = 2
                    print("CRITICAL HIT!")
                else:
                    crit = 1
                enemys_damage = 2 * all_enemy_stats[0] * crit / 5 + 2 * int(possible_moves[0][3]) * all_enemy_stats[4] / all_enemy_stats[5] / 50 + 2
                print(f"{enemy_pokemon[0]} Did {int(enemys_damage)} Damage To {user_choice[0]}!")
                users_health = all_user_stats[3]
                users_health = int(users_health - enemys_damage)
                all_user_stats[3] = users_health
                if user_fainted() == "yes":
                    repeat == False
                    exit()
                elif enemy_fainted() == "yes":
                    repeat == False
                    exit()
                # print(f"{user_choice[0]} Has {all_user_stats[3]}hp left!")
                print("\n")
                print("--------------------------------------------")
                pokemon_stats()
                user_interface()

def enemy_starts():
    if speed() == "enemy":
        repeat = True
        while repeat:
            if user_fainted() == "yes":
                repeat == False
                exit()
            elif enemy_fainted() == "yes":
                repeat == False
                exit()
            print("--------------------------------------------")
            print("\n")
            print(f"{enemy_pokemon[0]} Attacks First!")
            print("\n")
            print("--------------------------------------------")
            if all_user_stats[3] > 0 and all_enemy_stats[3] > 0:
                enemy_pokemon_moves()
                crit_chance = random.randint(0, 100)
                if crit_chance == 1:
                    crit = 2
                    print("CRITICAL HIT!")
                else:
                    crit = 1
                enemys_damage = 2 * all_enemy_stats[0] * crit / 5 + 2 * int(possible_moves[0][3]) * all_enemy_stats[4] / all_enemy_stats[5] / 50 + 2
                print(f"{enemy_pokemon[0]} Did {int(enemys_damage)} Damage To {user_choice[0]}!")
                users_health = all_user_stats[3]
                users_health = int(users_health - enemys_damage)
                all_user_stats[3] = users_health
                if user_fainted() == "yes":
                    repeat == False
                    exit()
                elif enemy_fainted() == "yes":
                    repeat == False
                    exit()
                # print(f"{user_choice[0]} Has {all_user_stats[3]}hp left!")
                user_move_choice()
                crit_chance = random.randint(0, 100)
                if crit_chance == 1:
                    crit = 2
                    print("CRITICAL HIT!")
                else:
                    crit = 1
                users_damage = 2 * all_user_stats[0] * crit / 5 + 2 * int(user_possible_moves[move_choice - 1][3]) * all_user_stats[4] / all_user_stats[5] / 50 + 2
                print(f"{user_choice[0]} Did {int(users_damage)} Damage To {enemy_pokemon[0]}!")
                enemys_health = all_enemy_stats[3]
                enemys_health = int(enemys_health - users_damage)
                all_enemy_stats[3] = enemys_health
                if user_fainted() == "yes":
                    repeat == False
                    exit()
                elif enemy_fainted() == "yes":
                    repeat == False
                    exit()
                # print(f"{enemy_pokemon[0]} Has {all_enemy_stats[3]}hp left!")
                print("\n")
                print("----------------------------------------------")
                pokemon_stats()
                user_interface()
                

def speed():
    if all_enemy_stats[6] < all_user_stats[6]:
        start = "user"
    elif all_enemy_stats[6] > all_user_stats[6]:
        start = "enemy"
    else:
        random_num = random.randint(1, 2)
        if random_num == 1:
            start = "user"
        else:
            start = "enemy"
    return start
    
def pokemon_stats():
    enemy_pokemon_stats()
    user_pokemon_stats()

run_once = 0
potion_sizes = []
def healing():
    global run_once
    while run_once == 0:
        num_potions = random.randint(0,2)
        if num_potions == 0:
            print("You have 0 potions!")
            run_once = run_once + 1
            user_interface()
        else:
            for i in range(num_potions):
                size = random.randint(1, 3)
                potion_sizes.append(size)
            run_once = run_once + 1
    again = True
    while again:
        if len(potion_sizes) > 0:
            num_small = potion_sizes.count(1)
            num_medium = potion_sizes.count(2)
            num_large = potion_sizes.count(3)
            print("\n")
            print(f"""Small Potion: {num_small}    Medium Potion: {num_medium}    Large Potion: {num_large}""")
            print("\n")
            which_size = input("Which size potion would you like to use? ").lower()
            for num in potion_sizes:
                if num == 0:
                    print("You have 0 potions to use")
                    user_interface()
                if which_size == "small":
                    if num == 1:
                        print(f"You have {num_small} small potions. This will heal 10hp")
                        use = input("Would you like to use one? ").lower()
                        if use == "yes":
                            all_user_stats[3] = all_user_stats[3] + 10
                            print("You Healed 10hp!")
                            print(f"{user_choice[0]} now has {all_user_stats[3]}hp!")
                            potion_sizes.remove(num)
                            user_interface()
                        elif use == "no":
                            user_interface()
                        else:
                            print("Please enter yes or no")
                elif which_size == "medium":
                    if num == 2:
                        if num_large < 1:
                            print("There are no potions for that size!")
                        print(f"You have {num_medium} medium potions. This will heal 20hp")
                        use = input("Would you like to use one? ").lower()
                        if use == "yes":
                            all_user_stats[3] = all_user_stats[3] + 20
                            print("You Healed 20hp!")
                            print(f"{user_choice[0]} now has {all_user_stats[3]}hp!")
                            potion_sizes.remove(num)
                            user_interface()
                        elif use == "no":
                            user_interface()
                        else:
                            print("Please enter yes or no")
                elif which_size == "large":
                    if num == 3:
                        if num_large < 1:
                            print("There are no potions for that size!")
                        print(f"You have {num_large} large potions. This will heal 30hp")
                        use = input("Would you like to use one? ").lower()
                        if use == "yes":
                            all_user_stats[3] = all_user_stats[3] + 30
                            print("You Healed 30hp!")
                            print(f"{user_choice[0]} now has {all_user_stats[3]}hp!")
                            potion_sizes.remove(num)
                            user_interface()
                        elif use == "no":
                            user_interface()
                        else:
                            print("Please enter yes or no")
            if num_small < 1:
                print("There are no potions for that size!")
            elif num_medium < 1:
                print("There are no potions for that size!")
            elif num_large < 1:
                print("There are no potions for that size!")
        else:
            print("You do not have any more potions!")
            user_interface() 

def battling():
    if len(user_pokemon_choices) == 0:
        enemy_pokemon_stats()
        pokemon_choice()
        user_pokemon_stats()
    if speed() == "user":
        user_starts()
    elif speed() == "enemy":
        enemy_starts()


def user_interface():
    repeat = True
    while repeat:
        print("""----====================================----
             POKEMON SIMULATOR
----====================================----
1. Battle    
2. Heal
--------------------------------------------""")
        choice = input("Which would you like to do? ")
        if choice == "2":
            if len(user_pokemon_choices) == 0:
                print("You cannot heal, as no pokemon has been chosen yet")
                user_interface()   
            else:
                healing()
            repeat = False
        elif choice == "1":
            battling()
            repeat = False
        else:
            print("Please enter a number from the choices")
user_interface()