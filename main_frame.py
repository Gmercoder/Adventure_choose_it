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

        def leveler(xp, level):
            xp_required=3.7825level4−134.59level3+2572.6level2−10699level+10703
            while xp => xp_required: 
                self.level = self.level += 1
                xp_required=3.7825level4−134.59level3+2572.6level2−10699level+10703

class Player_class:

    def __init__(class_requirements:list, class_abilities:list, skills:list, bonusses:list):
        self.class_requirements = class_requirements
        self.class_abilities = class_abilities
        self.skills = skills
        self.bonusses = bonusses

    def skill_bonus(bonus_1:str, bonus_2:str Character):
        Character.bonus_1 = Character.bonus_1 += 1
        Character.bonus_2 = Character.bonus_2 += 1

    def crit_bonus(Character):
        if "crit_bonus" in Character.abilities:
            if hit_roll => 19:
        
  class Misc_item():
    def __init__(self, name:str, value:int, weight:int) -> None:
        self.name = name
        self.value = value
        self.weight = weight


class Armor:
    def __init__(self, name:str, armor_class:int, value:int, weight:int) -> None:
        self.name = name
        self.armor_class = armor_class
        self.value = value
        self.weight = weight


class Weapon:
    def __init__(self, name:str, damage_dice:Dice, damage_attribute:str, value:int, weight:int) -> None:
        self.name = name
        self.damage_dice = damage_dice
        self.damage_attribute = damage_attribute
        self.value = value
        self.weight = weight

    def damage(self, character)->int:
        return self.damage_dice.roll() + character.__getattribute__(self.damage_attribute) % 4

class Magic_Armor:
    def __init__(self, name:str, armor_class:int, value:int, weight:int, abilities:list, resistance:list) -> None:
        self.name = name
        self.armor_class = armor_class
        self.value = value
        self.weight = weight
        self.abilities = abilities
        self.resistances = resistances

    def damage_resistance(resistances):
        if damage_type = resistances:
            damage_taken = damage_taken/2
        


class Magic_Weapon:
    def __init__(self, name:str, damage_dice:Dice, damage_attribute:str, value:int, weight:int, dt:str) -> None:
        self.name = name
        self.damage_dice = damage_dice
        self.damage_attribute = damage_attribute
        self.value = value
        self.weight = weight
        self.damage_type = dt

    def damage(self, character)->int:
        return self.damage_dice.roll() + character.__getattribute__(self.damage_attribute) % 4

class quest():
