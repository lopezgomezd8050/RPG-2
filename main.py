import os
import random
import time
import math

#things to do
#make the xp and enemy progression fair

#done
#fix the no armor bug#fixed
#enemy total health is glitchy #ehh it works kinda #its a feature
#add shop for the trader#added but not much to do
#fix the armor stats


class Armor:

  def __init__(self, tier, slot, health, damage, name, value):
    self.tier = tier
    self.slot = slot
    self.health = health
    self.damage = damage
    self.name = name
    self.value = value


class Consumables:

  def __init__(self, tier, slot, stat, increase, name, type, value):
    self.tier = tier
    self.slot = slot
    self.stat = stat
    self.increase = increase
    self.name = name
    self.type = type
    self.value = value


class Person:

  def __init__(self, Health, CurrHealth, Attack, Mage, Range, Level, Effects,
               Equip, Class, Exp, Cutter):
    self.Health = Health
    self.CurrHealth = Health
    self.Attack = Attack
    self.Mage = Mage
    self.Range = Range
    self.Level = Level
    self.Effects = Effects
    self.Equip = Equip
    self.Class = Class
    self.Exp = Exp
    self.Cutter = Cutter


epichelmet = Armor(1, 'helmet', 99999, 99999, 'epichelmet', 99999999)

#Armors n stuff

t1h = Armor(1, 'helmet', 1, 1, 'tier 1 helm', 9)
t1c = Armor(1, 'chestplate', 1, 1, 'tier 1 chestplate', 9)
t1p = Armor(1, 'platelegs', 1, 1, 'tier 1 platelegs', 9)
t1a = Armor(1, 'amulet', 1, 1, 'tier 1 amulet', 9)
t1s = Armor(1, 'sword', 1, 1, 'tier 1 sword', 9)
t1b = Armor(1, 'bow', 1, 1, 'tier 1 bow', 9)
t1w = Armor(1, 'wand', 1, 1, 'tier 1 wand', 9)

t2h = Armor(2, 'helmet', 1, 1, 'tier 2 helm', 9)
t2c = Armor(2, 'chestplate', 1, 1, 'tier 2 chestplate', 9)
t2p = Armor(2, 'platelegs', 1, 1, 'tier 2 platelegs', 9)
t2a = Armor(2, 'amulet', 1, 1, 'tier 2 amulet', 9)
t2s = Armor(2, 'sword', 1, 1, 'tier 2 sword', 9)
t2b = Armor(2, 'bow', 1, 1, 'tier 2 bow', 9)
t2w = Armor(2, 'wand', 1, 1, 'tier 2 wand', 9)

t3h = Armor(3, 'helmet', 1, 1, 'tier 3 helm', 9)
t3c = Armor(3, 'chestplate', 1, 1, 'tier 3 chestplate', 9)
t3p = Armor(3, 'platelegs', 1, 1, 'tier 3 platelegs', 9)
t3a = Armor(3, 'amulet', 1, 1, 'tier 3 amulet', 9)
t3s = Armor(3, 'sword', 1, 1, 'tier 3 sword', 9)
t3b = Armor(3, 'bow', 1, 1, 'tier 3 bow', 9)
t3w = Armor(3, 'wand', 1, 1, 'tier 3 wand', 9)

t4h = Armor(4, 'helmet', 1, 1, 'tier 4 helm', 9)
t4c = Armor(4, 'chestplate', 1, 1, 'tier 4 chestplate', 9)
t4p = Armor(4, 'platelegs', 1, 1, 'tier 4 platelegs', 9)
t4a = Armor(4, 'amulet', 1, 1, 'tier 4 amulet', 9)
t4s = Armor(4, 'sword', 1, 1, 'tier 4 sword', 9)
t4b = Armor(4, 'bow', 1, 1, 'tier 4 bow', 9)
t4w = Armor(4, 'wand', 1, 1, 'tier 4 wand', 9)

t5h = Armor(5, 'helmet', 1, 1, 'tier 5 helm', 9)
t5c = Armor(5, 'chestplate', 1, 1, 'tier 5 chestplate', 9)
t5p = Armor(5, 'platelegs', 1, 1, 'tier 5 platelegs', 9)
t5a = Armor(5, 'amulet', 1, 1, 'tier 5 amulet', 9)
t5s = Armor(5, 'sword', 1, 1, 'tier 5 sword', 9)
t5b = Armor(5, 'bow', 1, 1, 'tier 5 bow', 9)
t5w = Armor(5, 'wand', 1, 1, 'tier 5 wand', 9)

nh = Armor(0, 'helmet', 0, 0, 'No Helmet', 0)
nc = Armor(0, 'chestplate', 0, 0, 'No Chestplate', 0)
np = Armor(0, 'platelegs', 0, 0, 'No Platelegs', 0)
na = Armor(0, 'amulet', 0, 0, 'No Amulet', 0)
nw = Armor(0, 'sword', 0, 0, 'No Weapon', 0)

hp1 = Consumables(1, 'consumable', 'Health', 20, 'Health Potion 1', 'health',
                  9)
hp2 = Consumables(2, 'consumable', 'Health', 50, 'Health Potion 2', 'heatlh',
                  9)
hp3 = Consumables(3, 'consumable', 'Health', 100, 'Health Potion 3', 'health',
                  9)
hp4 = Consumables(4, 'consumable', 'Health', 250, 'Health Potion 4', 'health',
                  9)
hp5 = Consumables(5, 'consumable', 'Health', 600, 'Health Potion 5', 'health',
                  9)

m1 = Consumables(1, 'consumable', 'Mage', 10, 'Magic Potion 1', 'magic', 9)
w1 = Consumables(1, 'consumable', 'Attack', 10, 'Attack Potion 1', 'range', 9)
a1 = Consumables(1, 'consumable', 'Range', 10, 'Attack Potion 1', 'attack', 9)
o1 = Consumables(1, 'consumable', 'Mage', 10, 'Overload Potion 1', 'all', 9)

m2 = Consumables(2, 'consumable', 'Mage', 20, 'Magic Potion 2', 'magic', 9)
w2 = Consumables(2, 'consumable', 'Attack', 20, 'Attack Potion 2', 'range', 9)
a2 = Consumables(2, 'consumable', 'Range', 20, 'Attack Potion 2', 'attack', 9)
o2 = Consumables(2, 'consumable', 'Mage', 20, 'Overload Potion 2', 'all', 9)

m3 = Consumables(3, 'consumable', 'Mage', 50, 'Magic Potion 3', 'magic', 9)
w3 = Consumables(3, 'consumable', 'Attack', 50, 'Attack Potion 3', 'range', 9)
a3 = Consumables(3, 'consumable', 'Range', 50, 'Attack Potion 3', 'attack', 9)
o3 = Consumables(3, 'consumable', 'Mage', 50, 'Overload Potion 3', 'all', 9)

m4 = Consumables(4, 'consumable', 'Mage', 100, 'Magic Potion 4', 'magic', 9)
w4 = Consumables(4, 'consumable', 'Attack', 100, 'Attack Potion 4', 'range', 9)
a4 = Consumables(4, 'consumable', 'Range', 100, 'Attack Potion 4', 'attack', 9)
o4 = Consumables(4, 'consumable', 'Mage', 100, 'Overload Potion 4', 'all', 9)

m5 = Consumables(5, 'consumable', 'Mage', 300, 'Magic Potion 5', 'magic', 9)
w5 = Consumables(5, 'consumable', 'Attack', 300, 'Attack Potion 5', 'range', 9)
a5 = Consumables(5, 'consumable', 'Range', 300, 'Attack Potion 5', 'attack', 9)
o5 = Consumables(5, 'consumable', 'Mage', 300, 'Overload Potion 5', 'all', 9)
noArmored = [nh, nc, np, na, nw]

armorTable = [
  t1h, t1c, t1p, t1a, t1s, t1b, t1w, t2h, t2c, t2p, t2a, t2s, t2b, t2w, t3h,
  t3c, t3p, t3a, t3s, t3b, t3w, t4h, t4c, t4p, t4a, t4s, t4b, t4w, t5h, t5c,
  t5p, t5a, t5s, t5b, t5w
]

consumableTable = [
  hp1, hp2, hp3, hp4, hp5, m1, m2, m3, m4, m5, w1, w2, w3, w4, w5, a1, a2, a3,
  a4, a5, o1, o2, o3, o4, o5
]

user = Person(0, 0, 0, 0, 0, 1, [], [nh, nc, np, na, nw], '', 0, 100)
enemy = Person(0, 0, 0, 0, 0, 1, [], [], '', 0, 100)

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

inv = []


#inv = [epichelmet, t4a, hp3, o4, a2,t1h]
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
    ans = input(question + "\n(" + exp1 + ")" + "(" + exp2 + ")" + "(" + exp3 +
                ")" + ": ").lower()
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
  print("Effects: " + str(*user.Effects))
  print("Coins: " + str(money))
  print("Level: " + str(user.Level))
  print("Exp: " + str(user.Exp) + "\nTo next level: " + str(user.Cutter) +
        '\n')


def armorSwapper(slot):
  global pureHeath
  global pureDamage
  ansEquip = ''
  x = 0
  y = 0
  validNumberList = []
  validArmorList = []
  ansEquipToInv = []
  w = 0
  for item in inv:
    if item.value == 0:
      inv.pop(w)
    w = w + 1
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
      ansEquip = int(input('what number item would you like to equip?: '))

      z = 0
      pureHealth = user.Health
      if user.Class == 'w':
        pureDamage = user.Attack
      elif user.Class == 'a':
        pureDamage = user.Range
      elif user.Class == 'm':
        pureDamage = user.Mage

      for i in user.Equip:
        if i.slot == slot:
          inv.append(i)
          user.Health = user.Health - i.health
          if user.Class == 'w':
            user.Attack = user.Attack - i.damage
          elif user.Class == 'a':
            user.Range = user.Range - i.damage
          elif user.Class == 'm':
            user.Mage = user.Mage - i.damage
          user.Equip[z] = (validArmorList[int(ansEquip)])
          v = validArmorList[int(ansEquip)]
          user.Health = user.Health + v.health
          if user.Class == 'w':
            user.Attack = user.Attack + v.damage
          elif user.Class == 'a':
            user.Range = user.Range + v.damage
          elif user.Class == 'm':
            user.Mage = user.Mage + v.damage
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
  validLoot = []
  for item in armorTable:
    if item.tier == tier:
      validLoot.append(item)
  for item in consumableTable:
    if item.tier == tier:
      validLoot.append(item)
      validLoot.append(item)
      validLoot.append(item)
      validLoot.append(item)
      validLoot.append(item)
  return random.choice(validLoot)


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
    print('You found:')
    for i in range(int(odds)):
      rolls = random.randint(0, 1)
      if rolls == 1:
        lootTable()
        a = lootTable()
        print(a.name)

  elif source == 'battleStrong':
    odds = 6
    odds = odds * luck
    print('You found:')
    for i in range(int(odds)):
      rolls = random.randint(0, 1)
      if rolls == 1:
        lootTable()
        a = lootTable()
        print(a.name)

  elif source == 'battleBoss':
    odds = 10
    odds = odds * luck
    print('You found:')
    for i in range(int(odds)):
      rolls = random.randint(0, 1)
      if rolls == 1:
        a = lootTable()
        print(a.name)

  elif source == "battleFinal":
    odds = 25
    odds = odds * luck
    print('You found:')
    for i in range(int(odds)):
      rolls = random.randint(0, 1)
      if rolls == 1:
        a = lootTable()
        print(a.name)

  elif source == 'chest':
    odds = 5
    odds = odds * luck
    print('You found:')
    for i in range(int(odds)):
      rolls = random.randint(0, 1)
      if rolls == 1:
        a = lootTable()
        print(a.name)

  elif source == 'trapChest':
    odds = 7
    odds = odds * luck
    print('You found:')
    for i in range(int(odds)):
      rolls = random.randint(0, 1)
      if rolls == 1:
        a = lootTable()
        print(a.name)


def ArmorToPerson(person):
  #this will add more health every time it is run, maybe this should be put in the armor equip stuff but every time it runs it adds more and more health
  #so every time you like get into a battle you get more and more hp
  attackStyle = 0
  if person.Class == 'w':
    attackStyle = person.Attack
  elif person.Class == 'a':
    attackStyle = person.Range
  elif person.Class == 'm':
    attackStyle = person.Mage
  for i in person.Equip:
    person.Health = person.Health + i.health
    attackStyle = attackStyle + i.damage
  if person.Class == 'w':
    person.Attack = attackStyle
  elif person.Class == 'a':
    person.Range = attackStyle
  elif person.Class == 'm':
    person.Mage = attackStyle


def removeArmor(person):
  attackStyle = 0
  if person.Class == 'w':
    attackStyle = person.Attack
  elif person.Class == 'a':
    attackStyle = person.Range
  elif person.Class == 'm':
    attackStyle = person.Mage
  for i in person.Equip:
    person.Health = person.Health - i.health
    attackStyle = attackStyle - i.damage
  if person.Class == 'w':
    person.Attack = attackStyle
  elif person.Class == 'a':
    person.Range = attackStyle
  elif person.Class == 'm':
    person.Mage = attackStyle


def expToLevel(person):
  while person.Exp >= person.Cutter:
    person.Exp = person.Exp - person.Cutter
    person.Level = person.Level + 1
    person.Cutter = (int(person.Cutter * 1.1))
    levelScale(person)


def levelScale(person):
  person.Health = person.Health + 5
  person.Attack = person.Attack + 5
  person.Range = person.Range + 5
  person.Mage = person.Mage + 5
  #print('you got a level')


def battleCalc(hit, name):
  attackStyle = 0
  enemyAttack = 0
  userDamageMult = 0.20
  enemyDamageMult = 0.20
  if user.Class == 'w':
    attackStyle = user.Attack
  elif user.Class == 'a':
    attackStyle = user.Range
  elif user.Class == 'm':
    attackStyle = user.Mage

  if enemy.Class == 'w':
    enemyAttack = enemy.Attack
  elif enemy.Class == 'a':
    enemyAttack = enemy.Range
  elif enemy.Class == 'm':
    enemyAttack = enemy.Mage


#Warrior strong against Archers
#Rangers strong against Magicians
#Magicians strong against Warriors
  if user.Class == 'w':
    if enemy.Class == 'w':
      userDamageMult = 0.20
    elif enemy.Class == 'a':
      userDamageMult = 0.30
    elif enemy.Class == 'm':
      userDamageMult = 0.15
  elif user.Class == 'a':
    if enemy.Class == 'w':
      userDamageMult = 0.15
    elif enemy.Class == 'a':
      userDamageMult = 0.20
    elif enemy.Class == 'm':
      userDamageMult = 0.30
  elif user.Class == 'm':
    if enemy.Class == 'w':
      userDamageMult = 0.30
    elif enemy.Class == 'a':
      userDamageMult = 0.15
    elif enemy.Class == 'm':
      userDamageMult = 0.20

  if enemy.Class == 'w':
    if user.Class == 'w':
      enemyDamageMult = 0.20
    elif user.Class == 'a':
      enemyDamageMult = 0.30
    elif user.Class == 'm':
      enemyDamageMult = 0.15
  elif enemy.Class == 'a':
    if user.Class == 'w':
      enemyDamageMult = 0.15
    elif user.Class == 'a':
      enemyDamageMult = 0.20
    elif user.Class == 'm':
      enemyDamageMult = 0.30
  elif enemy.Class == 'm':
    if user.Class == 'w':
      enemyDamageMult = 0.30
    elif user.Class == 'a':
      enemyDamageMult = 0.15
    elif user.Class == 'm':
      enemyDamageMult = 0.20

  if hit == 'yes':
    enemy.CurrHealth = int(enemy.CurrHealth - (attackStyle * userDamageMult))

    print('You damaged ' + name + ' for ' +
          str(int((attackStyle * userDamageMult))) + ' Health')
  else:
    if hit == 'flee':
      print('You tried to flee but failed!')
    else:
      print('')
  user.CurrHealth = int(user.CurrHealth - (enemyAttack * enemyDamageMult))
  print(name + ' damaged you for ' + str(int(enemyAttack * enemyDamageMult)) +
        ' Health')


def consumableCalc(type):
  if type.type == 'health':
    healthHealed = 0
    healthInc = type.increase
    healthPrevious = user.CurrHealth
    user.CurrHealth = int(user.CurrHealth * healthInc)
    if user.CurrHealth > user.Health:
      healthHealed = user.Health - healthPrevious
      user.CurrHealth = user.Health
    else:
      healthHealed = int(user.CurrHealth * healthInc - user.CurrHealth)
    print('\nYou healed for ' + str(healthHealed) + ' Health.')
  elif type.type == 'magic':
    user.Mage = user.Mage + type.increase
    print('Your magic stat increased by ' + str(type.increase) + '.')
  elif type.type == 'range':
    user.Range = user.Range + type.increase
    print('Your ranged stat increased by ' + str(type.increase) + '.')
  elif type.type == 'attack':
    user.Attack = user.Attack + type.increase
    print('Your attack stat increased by ' + str(type.increase) + '.')
  elif type.type == 'all':
    user.Range = user.Range + type.increase
    user.Mage = user.Mage + type.increase
    user.Attack = user.Attack + type.increase
    print('All your combat stats increased by ' + str(type.increase) + '.')


  #total health, mage, range, attack, mixes
def battle(special):
  global money
  expToLevel(user)
  classPool = ['w', 'a', 'm']
  fleeCheck = 0
  if user.CurrHealth > user.Health:
    user.CurrHealth = user.Health
  enterclr()
  enemyNamePool = [
    'Qa', 'Qe', 'Qi', 'Qo', 'Qu', 'Wa', 'We', 'Wi', 'Wo', 'Wu', 'Ra', 'Re',
    'Ri', 'Ro', 'Ru', 'Ta', 'Te', 'Ti', 'To', 'Tu', 'Ya', 'Ye', 'Yi', 'Yo',
    'Yu', 'Pa', 'Pe', 'Pi', 'Po', 'Pu', 'Sa', 'Se', 'Si', 'So', 'Su', 'Da',
    'De', 'Di', 'Do', 'Du', 'Fa', 'Fe', 'Fi', 'Fo', 'Fu', 'Ga', 'Ge', 'Gi',
    'Go', 'Gu', 'Ha', 'He', 'Hi', 'Ho', 'Hu', 'Ja', 'Je', 'Ji', 'Jo', 'Ju',
    'Ka', 'Ke', 'Ki', 'Ko', 'Ku', 'La', 'Le', 'Li', 'Lo', 'Lu', 'Za', 'Ze',
    'Zi', 'Zo', 'Zu', 'Xa', 'Xe', 'Xi', 'Xo', 'Xu', 'Ca', 'Ce', 'Ci', 'Co',
    'Cu', 'Va', 'Ve', 'Vi', 'Vo', 'Vu', 'Ba', 'Be', 'Bi', 'Bo', 'Bu', 'Na',
    'Ne', 'Ni', 'No', 'Nu', 'Ma', 'Me', 'Mi', 'Mo', 'Mu'
  ]
  enemyFullName = random.choice(enemyNamePool) + '\'' + random.choice(
    enemyNamePool).lower()
  enemyClassStyle = ''
  ans = 'ans'
  if special == '':
    enemy.Health = user.Health + (random.randint(-50, -25))
    enemy.CurrHealth = enemy.Health
    enemy.Exp = user.Exp * random.randint(1, 2)  #if this is a float it crashes
    enemy.Class = random.choice(classPool)
    if enemy.Class == 'w':  #This doesnt compensate for armor based bonuses
      enemy.Attack = random.randint(25, 30)  #
      enemy.Range = random.randint(10, 15)
      enemy.Mage = random.randint(10, 15)
      enemyClassStyle = ' the Warrior '
    elif enemy.Class == 'a':
      enemy.Attack = random.randint(10, 15)
      enemy.Range = random.randint(25, 30)  #
      enemy.Mage = random.randint(10, 15)
      enemyClassStyle = ' the Archer '
    elif enemy.Class == 'm':
      enemy.Attack = random.randint(10, 15)
      enemy.Range = random.randint(10, 15)
      enemy.Mage = random.randint(25, 30)  #
      enemyClassStyle = ' the Magician '
    enemy.Effects = []
    enemy.Equip = [nh, nc, np, na, nw]
    expToLevel(enemy)
    ArmorToPerson(enemy)
    print(enemyFullName + enemyClassStyle + 'drew near!')
  elif special == 'trader':
    #fair and balanced
    enemy.Health = 9999999999
    enemy.CurrHealth = enemy.Health
    enemy.Exp = 99999999999999999999999
    enemy.Class = 'a'
    enemy.Equip = [t5h, t5c, t5p, t5a, t5w]
    enemyFullName = 'The Wandering Trader'
    expToLevel(enemy)
    ArmorToPerson(enemy)
    print('The trader had enough')
  elif special == 'boss1':
    print('boss 1')
  elif special == 'boss2':
    print('boss 2')
  elif special == 'boss3':
    print('boss 3')
  elif special == 'boss4':
    print('boss 4')
  elif special == 'final boss':
    print('final boss')
  while enemy.CurrHealth > 0 and user.CurrHealth > 0:

    print('\nCurrent Standings:\n\nYour Health: ' + str(user.CurrHealth) +
          '/' + str(user.Health) + '\n' + enemyFullName + '\'s Health: ' +
          str(enemy.CurrHealth) + '/' + str(enemy.Health) +
          '\n')  #for some reason enemy health is messy so ehh
    ans = question(
      '\nWould you like to:\n\nAttack ' + enemyFullName +
      '\nCheck Your Inventory \nFlee\n', 'a', 'i', 'f')

    if ans == 'a':
      if user.Class == 'w':
        print('You struck ' + enemyFullName)
        battleCalc('yes', enemyFullName)
        if user.CurrHealth <= 0:
          break
      elif user.Class == 'a':
        print('You shot ' + enemyFullName)
        battleCalc('yes', enemyFullName)
        if user.CurrHealth <= 0:
          break
      elif user.Class == 'm':
        print('You casted a spell on ' + enemyFullName)
        battleCalc('yes', enemyFullName)
        if user.CurrHealth <= 0:
          break
      ans = 'ans'
    elif ans == 'i':
      x = 0
      y = 0
      validNumberList = []
      validItemList = []
      ansItemToInv = []
      invAns = 'abc'
      numAns = ''
      print('\n')
      for item in inv:
        if item.slot == 'consumable':
          print(item.name + " (" + (str(x)) + ')\n')
          validNumberList.append(x)
          validItemList.append(item)
          ansItemToInv.append(list((x, y)))
          x = x + 1
        y = y + 1
      while invAns not in ("e", "c"):
        invAns = input(
          'Would you like to eat items to heal or close inventory? (e)(c):'
        ).lower()
        if invAns == 'e' and x == 0:
          print('\n No consumable items in your inventory.')
          invAns = ''
          break
      if invAns == 'e':
        while numAns not in (validNumberList):
          try:
            numAns = int(input('what number item would you like to consume: '))
          except:
            print('')
        finalItem = ansItemToInv[int(numAns)]
        consumableCalc(validItemList[int(numAns)])
        finalItem.pop(0)
        inv.pop(finalItem[0])
      battleCalc('inv', enemyFullName)
      if invAns == 'c':
        print('Closing Inventory')
    elif ans == 'f':
      x = random.randint(0, 1)
      if x == 1:
        print('You Fled Sucessfully!')
        fleeCheck = 1
        break
      else:
        battleCalc('flee', enemyFullName)
        ans = 'ans'
    enterclr()
  if user.Health > 0:
    print('Battle End')
    if fleeCheck == 0:
      loot('battle')
      expGained = 25 + (user.Exp * 0.3) + (user.Level * 25)
      user.Exp = user.Exp + expGained
      moneyGained = random.randint(25, 50)
      money = money + moneyGained
      print(str(moneyGained) + ' Coins')
      print(str(int(expGained)) + ' Exp')
    else:
      print('You fled so you gained no Money, Exp or Loot.')
  else:
    print('')
  expToLevel(user)


def chest():
  enterclr()
  print('You found a Treasure Chest while exploring the ' + currentLocation +
        '.')
  loot("chest")


def trapChest():
  enterclr()
  print('You found a Treasure Chest while exploring the ' + currentLocation +
        '.')
  print('An enemy drew near trying to defend the chest!')
  battle('')
  loot("trapChest")


def shopInt(tier):
  print('\nWhat would you like to buy?')
  validLoot = []
  formatThingy = []
  formatItem = []
  formatName = []
  formatValue = []
  formatNumber = []
  shoppingComplete = []
  global money
  for item in armorTable:
    if item.tier == tier:
      validLoot.append(item)
  for item in consumableTable:
    if item.tier == tier:
      validLoot.append(item)
  x = 5
  y = 0
  for i in range(x):
    z = random.choice(validLoot)
    print(z.name + ' (' + str(z.value) + ')' + '(' + str(y) + ')')
    formatThingy.append([z, z.name, z.value, y])
    formatItem.append(z)
    formatName.append(z.name)
    formatValue.append(z.value)
    formatNumber.append(y)
    shopChoice = '9'
    y = y + 1
  while shopChoice not in formatNumber:
    try:
      shopChoice = int(input('What number item would you like to buy?: '))
      if formatValue[shopChoice] > money:
        print('too poor lol')
        shopChoice = '9'
        break
      shoppingComplete = formatItem[shopChoice]
      formatItem.pop(shopChoice)
      money = money - formatValue[shopChoice]
      inv.append(shoppingComplete)
    except:
      continue


def shop():
  enterclr()
  ans = ''
  print('You stumbled across a wandering trader')
  ans = question(
    "what would you like to buy, not buy, or attack the shop owner?", 'b', 'n',
    'a')
  if ans == 'b':
    if currentLocation == "plains":
      shopInt(1)
    elif currentLocation == "forest":
      shopInt(2)
    elif currentLocation == "desert":
      shopInt(3)
    elif currentLocation == "tundra":
      shopInt(4)
    elif currentLocation == "mountain":
      shopInt(5)
    elif currentLocation == "mountaintop":
      shopInt(5)
  elif ans == 'n':
    print('\nYou kindly decline their offer.\n')
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
  eventRegulator = 8  #normally 8
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


def tutorial():
  print('Welcome to rpg')
  user.Class = question(
    'Do you want to be a Warrior, an Archer, or a Magician?', 'w', 'a', 'm')
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

    user.Range = random.randint(110, 120)
    print("Range: " + str(user.Range) + '\n')
  elif user.Class == 'm':
    print('\nYou picked the Magician class!')

    user.Health = random.randint(100, 120)
    print("\nHealth: " + str(user.Health))
    user.CurrHealth = user.Health
    user.Attack = random.randint(40, 50)
    print("Attack: " + str(user.Attack))

    user.Mage = random.randint(110, 120)
    print("Mage: " + str(user.Mage))

    user.Range = random.randint(40, 50)
    print("Range: " + str(user.Range) + '\n')

  enterclr()
  print('''
Warrior strong against Archers
Rangers strong against Magicians
Magicians strong against Warriors
    ''')
  enterclr()


def dayCycle():
  global day
  tutorial()
  while user.CurrHealth > 0:
    print("It is day " + str(day) + " in your journey.")
    print("You are currently in the " + currentLocation + ".")
    ans = "ans"

    while ans not in ("s", "i", "e", "d", "a"):
      ans = input(
        "\nWould you like to:\n\nCheck your Stats\nCheck your Inventory\nEquip Armor\nExplore the "
        + currentLocation.capitalize() + "\nDont Explore the " +
        currentLocation.capitalize() + "\n\n(s)(i)(a)(e)(d): ").lower()
      if ans == "s":
        userStats()
        ans = "ans"
      if ans == "i":
        print("\n")
        w = 0
        for item in inv:
          if item.value == 0:
            inv.pop(w)
          w = w + 1
        for item in inv:
          print(item.name)
        ans = "ans"
      if ans == 'e':
        print("\nYou venture off to explore the " + currentLocation + ".\n")
        randomEvent(2)
      if ans == 'd':
        healthHealed = 0
        healthMult = 1.2
        healthPrevious = user.CurrHealth

        user.CurrHealth = int(user.CurrHealth * healthMult + 10)
        if user.CurrHealth > user.Health:
          healthHealed = user.Health - healthPrevious
          user.CurrHealth = user.Health
        else:
          healthHealed = int(user.CurrHealth * healthMult - user.CurrHealth)
        print("\nYou decide not to explore the " + currentLocation +
              " and took rest.\nYou healed for " + str(healthHealed) +
              ' Health.')
        randomEvent(1)
      if ans == 'a':
        equipMenu()
        ans = "ans"
    day = day + 1
    enterclr()
  clr()
  print("You died!")
  print("You lasted " + str(day) + " days.")


dayCycle()
