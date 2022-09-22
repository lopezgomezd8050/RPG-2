import os
import random
import time
import math


class Armor:

    def __init__(self, tier, slot, health, damage, name):
        self.tier = tier
        self.slot = slot
        self.health = health
        self.damage = damage
        self.name = name


class Person:

    def __init__(self, Health, CurrHealth, Attack, Mage, Range, Level, Effects,
                 Equip,Class):
        self.Health = Health
        self.CurrHealth = Health
        self.Attack = Attack
        self.Mage = Mage
        self.Range = Range
        self.Level = Level
        self.Effects = Effects
        self.Equip = Equip
        self.Class = Class


epichelmet = Armor(1, 'helmet', 99999, 99999, 'epichelmet')

#Armors n stuff

t1h = Armor(1, 'helmet', 1, 1, 'tier 1 helm')
t1c = Armor(1, 'chestplate', 1, 1, 'tier 1 chestplate')
t1p = Armor(1, 'platelegs', 1, 1, 'tier 1 platelegs')
t1a = Armor(1, 'amulet', 1, 1, 'tier 1 amulet')
t1s = Armor(1, 'sword', 1, 1, 'tier 1 sword')
t1b = Armor(1, 'bow', 1, 1, 'tier 1 bow')
t1w = Armor(1, 'wand', 1, 1, 'tier 1 wand')

t2h = Armor(2, 'helmet', 1, 1, 'tier 2 helm')
t2c = Armor(2, 'chestplate', 1, 1, 'tier 2 chestplate')
t2p = Armor(2, 'platelegs', 1, 1, 'tier 2 platelegs')
t2a = Armor(2, 'amulet', 1, 1, 'tier 2 amulet')
t2s = Armor(2, 'sword', 1, 1, 'tier 2 sword')
t2b = Armor(2, 'bow', 1, 1, 'tier 2 bow')
t2w = Armor(2, 'wand', 1, 1, 'tier 2 wand')

t3h = Armor(3, 'helmet', 1, 1, 'tier 3 helm')
t3c = Armor(3, 'chestplate', 1, 1, 'tier 3 chestplate')
t3p = Armor(3, 'platelegs', 1, 1, 'tier 3 platelegs')
t3a = Armor(3, 'amulet', 1, 1, 'tier 3 amulet')
t3s = Armor(3, 'sword', 1, 1, 'tier 3 sword')
t3b = Armor(3, 'bow', 1, 1, 'tier 3 bow')
t3w = Armor(3, 'wand', 1, 1, 'tier 3 wand')

t4h = Armor(4, 'helmet', 1, 1, 'tier 4 helm')
t4c = Armor(4, 'chestplate', 1, 1, 'tier 4 chestplate')
t4p = Armor(4, 'platelegs', 1, 1, 'tier 4 platelegs')
t4a = Armor(4, 'amulet', 1, 1, 'tier 4 amulet')
t4s = Armor(4, 'sword', 1, 1, 'tier 4 sword')
t4b = Armor(4, 'bow', 1, 1, 'tier 4 bow')
t4w = Armor(4, 'wand', 1, 1, 'tier 4 wand')

t5h = Armor(5, 'helmet', 1, 1, 'tier 5 helm')
t5c = Armor(5, 'chestplate', 1, 1, 'tier 5 chestplate')
t5p = Armor(5, 'platelegs', 1, 1, 'tier 5 platelegs')
t5a = Armor(5, 'amulet', 1, 1, 'tier 5 amulet')
t5s = Armor(5, 'sword', 1, 1, 'tier 5 sword')
t5b = Armor(5, 'bow', 1, 1, 'tier 5 bow')
t5w = Armor(5, 'wand', 1, 1, 'tier 5 wand')

nh = Armor(0, 'helmet', 0, 0, 'No Helmet')
nc = Armor(0, 'chestplate', 0, 0, 'No Chestplate')
np = Armor(0, 'platelegs', 0, 0, 'No Platelegs')
na = Armor(0, 'amulet', 0, 0, 'No Amulet')
nw = Armor(0, 'sword', 0, 0, 'No Weapon')

noArmored = [nh, nc, np, na, nw]

armorTable = [
    t1h, t1c, t1p, t1a, t1s, t1b, t1w, t2h, t2c, t2p, t2a, t2s, t2b, t2w, t3h,
    t3c, t3p, t3a, t3s, t3b, t3w, t4h, t4c, t4p, t4a, t4s, t4b, t4w, t5h, t5c,
    t5p, t5a, t5s, t5b, t5w
]

user = Person(0, 0, 0, 0, 0, 1, [], [nh, nc, np, na, nw],'')
enemy = Person(0, 0, 0, 0, 0, 1, [], [],'')

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
inv = [epichelmet, t4a]

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
    print("\nHealth: " + str(user.CurrHealth))
    print("Attack: " + str(user.Attack))
    print("Mage: " + str(user.Mage))
    print("Range: " + str(user.Range))
    print("Effects: " + str(user.Effects))
    print("Money: " + str(money))
    print("Level: " + str(user.Level))
    print("Exp to next level: " + str(exp) + '\n')


#no armor still exists in inventory but we can fix that later bc i am lazy and i worked on this for long enough
def armorSwapper(slot):
    ansEquip = ''
    x = 0
    y = 0
    validNumberList = []
    validArmorList = []
    ansEquipToInv = []
    for item in inv:
        if item.slot == slot:
            print(item.name + " (" + (str(x)) + ')\n')
            validNumberList.append(x)
            validArmorList.append(item)
            ansEquipToInv.append(list((x, y)))
            x = x + 1
        y = y + 1
    while ansEquip not in (validNumberList):
        if validNumberList == []:
            print('No items of ' + slot + ' in your inventory.')
            break
        try:
            ansEquip = int(
                input('what number item would you like to equip?: '))

            z = 0
            for i in user.Equip:
                if i.slot == slot:
                    inv.append(i)
                    user.Equip[z] = (validArmorList[int(ansEquip)])
                z = z + 1
            finalEquip = ansEquipToInv[int(ansEquip)]
            finalEquip.pop(0)
            inv.pop(finalEquip[0])
        except:
            print('')
            continue
        else:
            break


def equipMenu():
    global userClass
    ans = 'ans'
    print('\nCurrent Equipment:\n')
    for armor in user.Equip:
        print(armor.name)
    print('\n')
    while ans not in ('h', 'c', 'p', 'a', 'w', 'n'):
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
        if user.Class == 'w':
            armorSwapper('sword')
        elif user.Class == 'a':
            armorSwapper('bow')
        elif user.Class == 'm':
            armorSwapper('wand')
    elif ans == 'n':
        print('Returning')


def lootSorter(tier):
    x = 1
    validLoot = []
    for item in armorTable:
        if item.tier == tier:
            validLoot.append(item)
            x = x + 1
    return random.choice(validLoot)


#VV bad code will change later™
def lootTable():
    lootGotten = ""
    if currentLocation == "plains":
        lootGotten = lootSorter(1)
    elif currentLocation == "forest":
        lootGotten = lootSorter(2)
    elif currentLocation == "desert":
        lootGotten = lootSorter(3)
    elif currentLocation == "tundra":
        lootGotten = lootSorter(4)
    elif currentLocation == "mountain":
        lootGotten = lootSorter(5)
    elif currentLocation == "mountaintop":
        lootGotten = lootSorter(5)

    inv.append(lootGotten)
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
                a = lootTable()
                print(a.name)

    elif source == 'trapChest':
        odds = 7
        odds = odds * luck
        for i in range(int(odds)):
            rolls = random.randint(0, 1)
            if rolls == 1:
                a = lootTable()
                print(a.name)


def expToLevel():
  global exp
  cutter=100
  level=1
  while exp>=cutter:
   exp=exp-cutter
   level=level+1
   cutter=(int(cutter*1.1))

#this works ^^^^^^^
    
def levelScale():
  for i in range(user.Level):
    user.Health=user.Health+5
    user.Attack=user.Attack+5
    user.Range=user.Range+5
    user.Mage=user.Mage+5
  for i in range(user.Level):
    user.Health=user.Health+5
    user.Attack=user.Attack+5
    user.Range=user.Range+5
    user.Mage=user.Mage+5

# import math
# expcalc=99999
# cutter=100
# level=1
# while expcalc>=cutter:
#   expcalc=expcalc-cutter
#   level=level+1
#   cutter=(int(cutter*1.1))

# print('Level: '+str(level))
# print('Cutter: '+str(cutter))
# print('ExpCalc: '+str(expcalc))

#test code i made

    
def battle(special):
    classPool=['w','a','m']
    enterclr()
    if special == '':
      enemy.Health=user.Health+(random.randint(-50,-25)) 
      enemy.CurrHealth=enemy.Health
      enemy.Level=user.Level+(random.randint(0,1))
      enemy.Class=random.choice(classPool)
      if enemy.Class=='w':
        enemy.Attack=0
      elif enemy.Class=='a':
        enemy.Range=0
      elif enemy.Class=='m':
        enemy.Mage=0
      enemy.Effects=[]
      enemy.Equip=[nh,nc,np,na,nw]
      
    elif special == 'trader':
      print('ur dying pepega')



#expToLevel levelScale and battle are working kinda
      #like they work but not how i want them to
      #fix that tmrw

def chest():
    enterclr()
    print('You found a Treasure Chest while exploring the ' + currentLocation +
          '.')
    print('You got: ')
    loot("chest")


def trapChest():
    enterclr()
    print('You found a Treasure Chest while exploring the ' + currentLocation +
          '.')
    print('An enemy popped out trying to defend the chest!')
    battle('')
    loot("trapChest")


def shop():
    enterclr()
    print('You stumbled across a wandering trader')
    #add the ability to attack the shop owner later but still add it
    #make it like a mini bossfight
    ans = question(
        "what would you like to buy, not buy, or attack the shop owner?", 'b',
        'n', 'a')
    if ans == 'b':
      print('you enter the shop (yk if there was one) (will add later)')
    elif ans == 'n':
      print('You kindly decline their offer.')
    elif ans == 'a':
      battle('trader')

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
                battle('')
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

#Warrior strong against Archers
#Rangers strong against Magicians
#Magicians strong against Warriors
def tutorial():
    print('Welcome to rpg')
    user.Class = question(
        'Do you want to be a Warrior, an Archer, or a Magician?', 'w', 'a',
        'm')
    if user.Class == 'w':
        print('\nYou picked the Warrior class!')

        user.Health = random.randint(100, 120)
        user.CurrHealth = user.Health
        print("\nHealth: " + str(user.Health))

        user.Attack = random.randint(110, 120)
        print("Attack: " + str(user.Attack))

        user.Mage = random.randint(40, 50)
        print("Mage: " + str(user.Mage))

        user.Range = random.randint(40, 50)
        print("Range: " + str(user.Range) + '\n')
    elif user.Class == 'a':
        print('\nYou picked the Archer class!')

        user.Health = random.randint(100, 120)
        print("\nHealth: " + str(user.Health))
        user.CurrHealth = user.Health
        user.Attack = random.randint(40, 50)
        print("Attack: " + str(user.Attack))

        user.Mage = random.randint(40, 50)
        print("Mage: " + str(user.Mage))

        user.Range = random.randint(100, 120)
        print("Range: " + str(user.Range) + '\n')
    elif user.Class == 'm':
        print('\nYou picked the Magician class!')

        user.Health = random.randint(100, 120)
        print("\nHealth: " + str(user.Health))
        user.CurrHealth = user.Health
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
                for item in inv:
                    print(item.name)
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
