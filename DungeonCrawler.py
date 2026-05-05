import random

#Ask for the players name
player_name = input("Tell me, what is your name? ")

#Player Dictionary
player = {
    "name": player_name,
    "hp": 25,
    "dmg": 4,
}

# List for enemies
enemies = ["Goblin", "Rat", "Skeleton", "Ghost", "HobGob"]

#Enemy health, hp and dmg
enemies = {
    "Goblin": {"hp": 20, "dmg": 5},
    "Rat": {"hp": 15, "dmg": 3}, 
    "Skeleton": {"hp": 20, "dmg": 7},
    "Ghost": {"hp": 25, "dmg": 8},
    "HobGob": {"hp": 50, "dmg": 12}
}

print("-------------------------------")
print("Below are your player stats:")
print("Name: " + player_name)
print("HP: " + str(player["hp"]))
print("Damage: " + str(player["dmg"]))
print("-------------------------------")

#Start of Dungeon Crawler
while True: 
    print("Will you enter the Dungeon?")
    print("\n1.Yes\n2.No")    
    choice = input("Select your choice 1 or 2: ")
    
    if choice == '1':
        print("You will now enter the Dungeon!")
        
        enemy_name = random.choice(list(enemies.keys()))
        enemy = enemies[enemy_name]


        print("-------------------------------")
        print("You've encountered a " + enemy_name)
        print("HP: " + str(enemy["hp"]))
        print("Damage: " + str(enemy["dmg"]))
        print(" ")
        print("Name: " + player_name)
        print("HP: " + str(player["hp"]))
        print("Damage: " + str(player["dmg"]))
        print("-------------------------------")

        while True:
            print("Would you like to 1.Fight or 2.Flee?")
            print("\n1.Fight\n2.Flee")
            choice == input("What is your decision?: ")
    
            if choice == '1':
                print("You fight the " + enemy_name)
                print(player_name + " deals 4 damage to " + enemy_name)
                player_dmg = str(player["dmg"])
                update_ehp = str(enemy["hp"])
                dmg_dealt = int(update_ehp) - int(player_dmg)
                print(enemy_name + " now has " + str(dmg_dealt) + " HP left!")
            else:
                print("Your cowardice is amusing.")
            break
        break
