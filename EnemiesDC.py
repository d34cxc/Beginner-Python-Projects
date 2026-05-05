#Importing random for a random chance at encountering one of the enemies within the list
import random

# List for enemies
enemies = ["Goblin", "Rat", "Skeleton", "Ghost", "HobGob"]

#Enemy health
enemies = {
    "Goblin": {"hp": 20, "dmg": 5},
    "Rat": {"hp": 15, "dmg": 3}, 
    "Skeleton": {"hp": 20, "dmg": 7},
    "Ghost": {"hp": 25, "dmg": 8},
    "HobGob": {"hp": 50, "dmg": 12}
}

enemy_name = random.choice(list(enemies.keys()))
enemy = enemies[enemy_name]

print("You encountered a " + enemy_name)
print("HP: " + str(enemy["hp"]))
print("Damage: " + str(enemy["dmg"]))
