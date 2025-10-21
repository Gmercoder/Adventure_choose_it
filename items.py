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
