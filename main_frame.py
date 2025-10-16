import random as rand
import time as ti


class Character:
    """Character class

    Represents all characters in the game.

    >>> moe = Character(health=10, armor=2, weapons=[], num_attack=1, playable=True)
    """
    def __init__(self, strength:int, dexterity:int, health:int, armor:Armor, weapons:list[Weapon], num_attack:int, playable: bool, con:int, 
                 intel:int, wis:int, res:int, san:int, mon:int, xp:int, lvl:int, clas:str, weaknesses:list, inventory:list) -> None:
        self.strength = strength
        self.dexterity = dexterity
        self.health = health
        self.armor = armor
        self.weapons = weapons
        self.num_attack = num_attack
        self.playable = playable

        self.constitiution = con
        self.intellegence = intel
        self.wisdom = wis
        self.resistance = res

        self.sanity = san
        self.money = mon
        self.experience = xp
        self.level = lvl
      
        self.class = clas

        self.weaknesses = weaknesses
        self.inventory = inventory


class Player_class():
  class barbarian():
    str skills
    str classabilities
  
  class Ranger():
    str skills
    str classabilities
  
  class Fighter():
    str skills
    str classabilities
    
  class Wizard():
    str skills
    str classabilities
  
  class Cleric():
    str skills
    str classabilities
  
  class Paladin():
    str skills
    str classabilities
  
  class Monk():
    str skills
    str classabilities
  
  class Rogue():
    str skills
    str classabilities
  
  class Bard():
    str skills
    str classabilities
  
  class Druid():
    str skills
    str classabilities
  
  class Warlock():
    str skills
    str classabilities

class quest():
