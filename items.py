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
