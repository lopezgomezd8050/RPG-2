import os
import random
import time
import math


class Armor:

    def __init__(self, tier, slot, health, damage,name):
        self.tier = tier
        self.slot = slot
        self.health = health
        self.damage = damage
        self.name = name


class Person:

    def __init__(self, Health, Attack, Mage, Range, Level, Effects,Equip,
                 Stats):
        self.Health = Health
        self.Attack = Attack
        self.Mage = Mage
        self.Range = Range
        self.Level = Level
        self.Effects = Effects
        self.Equip = Equip
        self.Stats = Stats

epichelmet=Armor(1,'helmet',1,1,'epichelmet')
user = Person(0, 0, 0, 0, 1, [], [], [])
enemy = Person(0, 0, 0, 0, 1, [], [], [])

location = [
    'plains', 'forest', 'desert', 'tundra', 'mountain', 'mountaintop', 'market'
]
currentLocation = location[0]
day = 1
money = 0
luck = 1
event = 0
eventRegulator = 0
randomEvents = ["battle"] * 6 + ["chest"] * 1 + ["trapchest"] * 1 + [
    "shop"
] * 1 + [
    "final boss"
] * 0  #make this a variable that changes to 1 after reaching moutnaintop
#also make a random event that like lets you move onto the next area by fighting a boss
exp = 0
inv=[epichelmet]

#make enemies a class too
class Enemy:

    def __init__(self, strength, type):
        self.strength = strength
        self.type = type


# remove these later
enemyMagic = ['Undead Mage', 'Lesser Thrall']
enemyWarrior = ['Zombie', 'Vampire']
enemyArcher = ['Skeleton', 'Sharpshooter']
enemyPool = enemyMagic + enemyWarrior + enemyArcher
# ^^^


def enter():
    input("Press enter to continue.")


def clr():
    os.system('cls' if os.name == 'nt' else 'clear')


def enterclr():
    input("Press enter to continue to next screen.")
    os.system('cls' if os.name == 'nt' else 'clear')


def question(question, exp1, exp2, exp3):
    ans = "ans"
    while ans not in (exp1, exp2, exp3):
        ans = input(question + "\n(" + exp1 + ")" + "(" + exp2 + ")" + "(" +
                    exp3 + ")" + ": ").lower()
    return ans


def yesNo(question):
    ans = "ans"
    while ans not in ("y", "n"):
        ans = input(question + " (y)(n): ").lower()
    return ans


def userStats():
    print("\nHealth: " + str(user.Health))
    print("Attack: " + str(user.Attack))
    print("Mage: " + str(user.Mage))
    print("Range: " + str(user.Range))
    print("Effects: " + str(user.Effects))
    print("Money: " + str(money))
    print("Level: " + str(user.Level))
    print("Exp to next level: " + str(exp) + '\n')

def armorSwapper(slot):
  ansEquip='ans'
  validNumberList=[]
  for item in inv:
    if item.slot==slot:
      print(item.name+" ("+(str(len(inv)))+')\n')
      validNumberList.append(len(inv))
      #print(validNumberList)
  while ansEquip not in validNumberList:
    ansEquip=int(input('what number item would you like to equip?: '))
        
def equipMenu():
    ans = 'ans'
    #print('Current Equipment:\n' + userEquip[0])  #work on this tmrw
    while ans not in ('h', 'c', 'p', 'a', 'w','n'):
        ans = input(
            'Would you like to equip a Helmet, Chestplate, Platelegs, Amulet, Weapon, or None?\n(h)(c)(p)(a)(w)(n):'
        ).lower()
    print('\n')
    
    if ans == 'h':
      armorSwapper('helmet')
    elif ans == 'c':
     armorSwapper('chestplate')
    elif ans == 'p':
      armorSwapper('platelegs')
    elif ans == 'a':
      armorSwapper('amulet')
    elif ans == 'w':
      armorSwapper('weapon')
    elif ans == 'n':
      print('Returning')


#VV bad code will change later™
def lootTable():
    lootGotten = "abc"
    if currentLocation == "plains":
        lootGotten = random.choice(t1Armor)  #and 2
    elif currentLocation == "forest":
        lootGotten = random.choice(t2Armor)  #and 3
    elif currentLocation == "desert":
        lootGotten = random.choice(t3Armor)  #and 4
    elif currentLocation == "tundra":
        lootGotten = random.choice(t4Armor)  #and 5
    elif currentLocation == "mountain":
        lootGotten = random.choice(t5Armor)  #mostly 5
    elif currentLocation == "mountaintop":
        lootGotten = random.choice(
            t5Armor)  #just 5 or we could add god armor or smth
    user.Inv.append(lootGotten)
    return lootGotten


#nerf this hard its too op
#but balancing updates are like the last thing needed lol
def loot(source):
    global eventRegulator
    if source == 'battle':
        odds = 3
        odds = odds * luck
        for i in range(int(odds)):
            rolls = random.randint(0, 1)
            if rolls == 1:
                lootTable()

    elif source == 'battleStrong':
        odds = 6
        odds = odds * luck
        for i in range(int(odds)):
            rolls = random.randint(0, 1)
            if rolls == 1:
                lootTable()

    elif source == 'battleBoss':
        odds = 10
        odds = odds * luck
        for i in range(int(odds)):
            rolls = random.randint(0, 1)
            if rolls == 1:
                lootTable()

    elif source == "battleFinal":
        odds = 25
        odds = odds * luck
        for i in range(int(odds)):
            rolls = random.randint(0, 1)
            if rolls == 1:
                lootTable()

    elif source == 'chest':
        odds = 5
        odds = odds * luck
        for i in range(int(odds)):
            rolls = random.randint(0, 1)
            if rolls == 1:
                print(lootTable())

    elif source == 'trapChest':
        odds = 7
        odds = odds * luck
        for i in range(int(odds)):
            rolls = random.randint(0, 1)
            if rolls == 1:
                print(lootTable())


def battle():
    enterclr()
    print("A(n) " + enemyPool[random.randint(0, 5)] + " drew near!")


def chest():
    enterclr()
    print('You found a Treasure Chest while exploring the ' + currentLocation +
          '.')
    loot("chest")
    print('You got: ' + 'placeholder kekw')


def trapChest():
    enterclr()
    print('You found a Treasure Chest while exploring the ' + currentLocation +
          '.')
    print('An enemy popped out trying to defend the chest!')
    battle()
    loot("trapChest")


def shop():
    enterclr()
    print('You stumbled across a wandering trader')
    #add the ability to attack the shop owner later but still add it
    #make it like a mini bossfight
    ans = question(
        "what would you like to buy, not buy, or attack the shop owner?", 'b',
        'n', 'a')


def finalBoss():
    print("ur gonna die pepega")


def noEvent():
    enterclr()
    print("No event occurred.")


def randomEvent(odds):
    global event
    global eventRegulator
    odds = odds * luck
    rolls = 0
    eventRegulator = 8
    #^^^^^^ change this to randomly change based on luck or days or smth
    for i in range(int(odds)):
        rolls = random.randint(0, 1)
        if rolls == 1:
            event = randomEvents[random.randint(0, eventRegulator)]
            if event == "battle":
                battle()
                event = 0
            if event == "chest":
                chest()
                event = 0
            if event == "trapchest":
                trapChest()
                event = 0
            if event == "shop":
                shop()
                event = 0
            if event == "final boss":
                finalBoss()
                event = 0
        elif rolls == 0:
            noEvent()

        #this code currently forces 2 events, leading to the event being repeated twice if there isnt a roll for it
        #fixed


def tutorial():
    user.Health
    user.Attack
    user.Mage
    user.Range
    print('Welcome to rpg')
    userClass = question(
        'Do you want to be a Warrior, an Archer, or a Magician?', 'w', 'a',
        'm')
    if userClass == 'w':
        print('\nYou picked the Warrior class!')

        user.Health = random.randint(100, 120)
        print("\nHealth: " + str(user.Health))

        user.Attack = random.randint(110, 120)
        print("Attack: " + str(user.Attack))

        user.Mage = random.randint(40, 50)
        print("Mage: " + str(user.Mage))

        user.Range = random.randint(40, 50)
        print("Range: " + str(user.Range) + '\n')
    elif userClass == 'a':
        print('\nYou picked the Archer class!')

        user.Health = random.randint(100, 120)
        print("\nHealth: " + str(user.Health))

        user.Attack = random.randint(40, 50)
        print("Attack: " + str(user.Attack))

        user.Mage = random.randint(40, 50)
        print("Mage: " + str(user.Mage))

        user.Range = random.randint(100, 120)
        print("Range: " + str(user.Range) + '\n')
    elif userClass == 'm':
        print('\nYou picked the Magician class!')

        user.Health = random.randint(100, 120)
        print("\nHealth: " + str(user.Health))

        user.Attack = random.randint(40, 50)
        print("Attack: " + str(user.Attack))

        user.Mage = random.randint(100, 120)
        print("Mage: " + str(user.Mage))

        user.Range = random.randint(40, 50)
        print("Range: " + str(user.Range) + '\n')

    enterclr()
    print("put tutorial here")
    enterclr()


def dayCycle():
    global day
    tutorial()
    #while like health is above 0 or smth
    while user.Health > 0:
        print("It is day " + str(day) + " in your journey.")
        print("You are currently in the " + currentLocation + ".")
        ans = "ans"

        while ans not in ("s", "i", "e", "d", "a"):
            ans = input(
                "\nWould you like to:\n\nCheck your Stats\nCheck your Inventory\nEquip Armor\nExplore the "
                + currentLocation.capitalize() + "\nDont Explore the " +
                currentLocation.capitalize() +
                "\n\n(s)(i)(a)(e)(d): ").lower()
            if ans == "s":
                userStats()
                ans = "ans"
            if ans == "i":
                print("\n")
                print(inv)
                ans = "ans"
            if ans == 'e':
                print("\nYou venture off to explore the " + currentLocation +
                      ".\n")
                randomEvent(2)
            if ans == 'd':
                print("\nYou decide not to explore the " + currentLocation +
                      ".\n")
                randomEvent(1)
            if ans == 'a':
                equipMenu()
                ans = "ans"
        day = day + 1
        enterclr()
    clr()
    print("You died!")
    print("You lasted " + day + "days.")


dayCycle()
