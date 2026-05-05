import random

#Ask for the players name
player_name = input("Tell me, what is your name? ")

#Player Dictionary
player = {
    "name": player_name,
    "hp": 25,
}

#Enemy health, hp and dmg
enemies = {
    "Goblin": {"hp": 20},
    "Rat": {"hp": 15}, 
    "Skeleton": {"hp": 20},
    "Ghost": {"hp": 25},
    "HobGob": {"hp": 50}
}

print("-------------------------------")
print("Below are your player stats:")
print("Name: " + player_name)
print("HP: " + str(player["hp"]))
print("-------------------------------")

print("Will you enter the Dungeon?")
choice = input("Select your choice (1) Yes or (2) No ")
#Start of Dungeon Crawler
while True: 
    
    if choice == '1':
        
        enemy_name = random.choice(list(enemies.keys()))
        enemy = enemies[enemy_name]

        print("-------------------------------")
        print("You've encountered a " + enemy_name)
        print("HP: " + str(enemy["hp"]))
        print(" ")
        print("Name: " + player_name)
        print("HP: " + str(player["hp"]))
        print("-------------------------------")

        player_hp = int(str(player["hp"]))
        enemy_hp = int(str(enemy["hp"]))

        while player_hp > 0 and enemy_hp > 0:
            print(f"\nYour HP: {player_hp} | Enemy HP: {enemy_hp}")
            action = input("Choose action: (1) Attack (2) Heal: ")

            if action == "1":
                damage = random.randint(1, 10)
                enemy_hp -= damage
                print(f"You dealt {damage} damage!")
            elif action == "2":
                heal = random.randint(5, 10)
                player_hp += heal
                print(f"You healed for {heal} HP!")
        
            # Check if enemy died before it can counter-attack
            if enemy_hp <= 0:
                print("The enemy was defeated!")
                print("-------------------------------")
                break
                
             # Enemy's turn
            enemy_dmg = random.randint(1, 10)
            player_hp -= enemy_dmg
            print(f"The enemy hit you for {enemy_dmg} damage!")
            
        if enemy_hp <= 0:
            go_deeper = input("Will you traverse deeper into the dungeon? (1) Yes (2) No: ")
            if go_deeper == "1":
                print(player_name + " you are a brave soul!")
                if go_deeper == "1":
                    choice = "1"
                    continue
                else:
                    break
 
        if player_hp <= 0:
            print("You have been defeated...")
            try_again = input("Would you like to try again?: (1) Yes (2) No: ")
            if try_again == "1":
                player["hp"] = 25
                choice = "1"
                continue
            else:
                break
        print("-------------------------------")
        break
