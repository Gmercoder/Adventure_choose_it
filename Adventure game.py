import random as rand
import time as ti

monster_list = ["chimera", "skeleton", "zombie", "dragon", "hydra", "slime", "ghost", "ghoul", "basilisk", "cyclops", "gorgon", "griffin", "minotaur", "sphinx", "banshee", "bonless", "wraith", "lich", "mummy", "necromanser", "vampire", "wyvern", "Oblex", "beholder", "manticore", "cockatrice", "werewolf", "giant", "goblin", "orc", "troll", "ogre"]
vendor_list = ["Josh", "Robert", "William", "Jones", "Dan", "Mathew"]
anthrohuman_vendors = ["Caelynn", "Liriath", "Aelarion", "Krushk", "Grommash"]
quest_list = ["Defeat a horde of Slimes", "Kill a dragon", "Help Thornfell fight off three Wyverns", "Find a basilisk near Whisperwood", "Escort the princess of Gohmashi to Thornfell", "Find a lost Griffin", "Help a sorceror with a necromanser problem", "Banish a banshee from the edge of the WrithingForests", "Help hide an innocent werewolf", "Fight a manticore"]
classes_list = ["Barbarian", "Fighter", "Monk", "Rogue", "Bard", "Cleric", "Druid", "Wizard", "Warlock", "Paladin", "Ranger"]
species_list = ["Human", "Dragonborne", "Dwarf", "Elf (Dark, Wood, High)", "Halfling", "Half-elf"]
def monsters():
    mononster = rand.choice(monster_list)
    return mononster.lower
def human_vendors():
    regular = rand.choice(vendor_list)
    return regular.lower
def anthro_vendors():
    demi = rand.choice(anthrohuman_vendors)
    return demi.lower
def bounties():
    quests = rand.choice(quest_list)
    return quests.lower
item_0 = quest_list[0]
item_1 = quest_list[1]
item_2 = quest_list[2]
item_3 = quest_list[3] 
item_4 = quest_list[4]
item_5 = quest_list[5]
item_6 = quest_list[6]
item_7 = quest_list[7]
item_8 = quest_list[8]
item_9 = quest_list[9]

def powers():
    classes = rand.choice(classes_list)
    return classes.lower
class_0 = classes_list[0]
class_1 = classes_list[1]
class_2 = classes_list[2]
class_3 = classes_list[3]
class_4 = classes_list[4]
class_5 = classes_list[5]
class_6 = classes_list[6]
class_7 = classes_list[7]
class_8 = classes_list[8]
class_9 = classes_list[9]
class_10 = classes_list[10]

def species():
    race = rand.choice(species_list)
    return race.lower
race_0 = species_list[0]
race_1 = species_list[1]
race_2 = species_list[2]
race_3 = species_list[3]
race_4 = species_list[4]
race_5 = species_list[5]



def play_game(mononster, regular, demi, quests, classes):
    print("Make sure to captialize the beginning letter of you answers.")
    ti.sleep(3)
    play = input("Welcome to my game would you like to play? (Y/N)")
    if play == "Y":
        print("Welcome the world of fantasy beings, I will give you a run down of what's happening.")
        ti.sleep(4)
        user = input("What do you want your name to be, (It can be anything)")
        ti.sleep(2)
        ask_now = input("Do you want to know the classes you can choose from and what they are or are you good? (Y/N)")
        if ask_now != "N":
            while True:
                ti.sleep(2)
                whhich = input(f"What class do you want to know more about? {class_0}, {class_1}, {class_2}, {class_3}, {class_4}, {class_5}, {class_6}, {class_7}, {class_8}, {class_9}, {class_10}")
                if whhich == "Barbarian":
                    print("A fierce warrior who channels primal fury, the Barbarian enters a state of rage to shrug off attacks and deal devastating blows. The source of a Barbarian's rage can be anything from inner animal spirits to ancient, wild magic.")
                elif whhich == "Fighter":
                    print("The master of martial combat, the Fighter is a versatile warrior defined by their mastery of weapons and armor. They can specialize in any number of combat styles and tactics.")
                elif whhich == "Monk":
                    print("A master of martial arts, the Monk channels an inner energy called Focus to perform incredible feats of speed and power. They fight unarmored and are known for their unarmed strikes.")
                elif whhich == "Rogue":
                    print("A master of stealth and subtlety, the Rogue uses cunning and surprise to exploit enemy weaknesses. They are highly versatile, excelling at everything from combat and subterfuge to exploration and social manipulation.")
                elif whhich == "Bard":
                    print("The spellcaster whose magic comes from the words of creation, the Bard is an expert in arts, music, and the power of inspiration. This class is a versatile support character that can buff allies, debuff enemies, and contribute to combat.")
                elif whhich == "Cleric":
                    print("A divine spellcaster who draws power from a deity or another divine source. Clerics are defined by their Divine Order, which determines their focus on martial combat or spellcasting.")
                elif whhich == "Druid":
                    print("A spellcaster who harnesses the power of nature and can take on the forms of animals.")
                elif whhich == "Wizard":
                    print("The magic-user, the Wizard has spent years studying the arcane arts to prepare and cast a variety of spells. They learn new spells by adding them to their unique spellbook.")
                elif whhich == "Warlock":
                    print("A wielder of magic granted by a supernatural patron, the Warlock uses pact-based magic to fight enemies.")
                elif whhich == "Paladin":
                    print("A holy warrior bound by a sacred oath, the Paladin is a heavily armored combatant who can channel divine power to smite foes and protect allies.")
                elif whhich == "Ranger":
                    print("A warrior with a deep connection to nature, the Ranger is a versatile martial class focused on survival and combat.")
                else:
                    print("Not a valid answer!")
                ti.sleep(3)
                repep = input("Would you like to know another class? (Y/N)")
                if repep != "Y":
                    break
        
        classs = input(f"What is your class? {class_0}, {class_1}, {class_2}, {class_3}, {class_4}, {class_5}, {class_6}, {class_7}, {class_8}, {class_9}, {class_10}.")
        print("You are a" , classs)
        ti.sleep(4)
        ranc = input("Do you want to know the races in the land of Ismira? (Y/N)")
        if ranc != "N":
            while True:
                ti.sleep(3)
                whoch_one = input(f"What race would you like to know more about? {race_0}, {race_1}, {race_2,}, {race_3},(only have to put Elf for more info about elves) {race_4}, {race_5}(Make sure to put Half-Elf)")
                if whoch_one == "Human":
                    print("The most adaptable and versatile of all species. Though they have no special attributes, they can fit any character class and archetype.")
                elif whoch_one == "Dragonborne":
                    print("Humanoids who have both the appearance and breath weapon of dragons.")
                elif whoch_one == "Dwarf":
                    print("A short, hardy, and bearded people known for their skill in mining and smithing. They are resistant to poison and have Darkvision.")
                elif whoch_one == "Elf":
                    print("An elegant, long-lived, and magical people with a connection to nature. They are immune to magical sleep.\n(Dark Elf): Elves with dark skin from the Underdark.\n High Elf: Masters of both weapon and arcane magic.\n Wood Elf: Quick on their feet and have superior stealth.")
                elif whoch_one == "Halfling":
                    print("Halfling: Diminutive folk known for their luck and nimbleness. They are brave and good at avoiding notice.")
                elif whoch_one == "Half-Elf":
                    print("Individuals who have human and elf parentage. They receive the benefits of both lineages, including Darkvision and versatility.")
                else:
                    print("Not a valid answer!")
                ti.sleep(3)
                repeat = input("Do you want to see another? (Y/N)")
                if repeat != "Y":
                    break
        
        raaace = input(f"What is your species? {race_0}, {race_1}, {race_2}, {race_3}, {race_4}, {race_5}?")
        print("You are a," ,raaace)
        ti.sleep(2)
        story = input("Would you like to read the story about the world you're in (Y/N)")
        if story == "Y":
            print("The story starts of with the creation, many monsters and humans alike were borne from many different ways, though nobody knows how it came to be there are only guesses.\nThere are many villages around the land known as Ismeria.\nSome places in Ismeria is Aethelgard. Whisperwoods. Thornfell. And much more.\n its up to you" ,user, "to go where you want to.")
            ti.sleep(8)
            choice_first = input("Where do you want to go? (Thornfell, Aethelgard?)")
            if choice_first  == "Aethelgard":
                ti.sleep(4)
                vendors_1 = input("You travel all the way to the bustling city of Aethelgard.\n there are many vendors would you like to go to one? (Y/N)")
                ti.sleep(4)
                if vendors_1 == "Y":
                    print(f"You go to a vendor their name is {regular()}")
                    ti.sleep(3)
                    coins = input("They're selling a sword, map and quill, the sword is fifteen coins, the map and quills is twenty coins, you have 250 coins, what do you want to buy? (Sword/ Map and Quill)")
                    ti.sleep(4)
                    if coins == "Sword":
                        result_1 = 250-15
                        print("You now have" , result_1, "coins")
                        ti.sleep(3)
                        now_what = input("Do you also want to buy the map and quill or go to the guild? (Map and Quill/Guild)")
                        if now_what == "Map and Quill":
                            result_3 = 235-20
                            print("You now have" ,result_3, "coins and you go to the guild afterwards.")
                            ti.sleep(3)
                            chooseee = input(f"There are three quests you see once you get to the guild, {item_0}, {item_7}, {item_4} (1,2,3)")
                            if chooseee == "1":
                                print("You go to the guild master and he lets you take on the quest. (Defeat a horde of Slimes) \n good luck kid, you're going to need it.Slimes are a tricky bunch. Hope you're ready for them.")
                                go = input("Do you want to head over to where the slimes are in the plains nearby or no? (Y/N)")
                                if go == "Y":
                                    print("You leave the gates of Aethelgard, going East you see a slime and slash it, nothing out of the ordinary... until you see dozens upon dozens of slimes!")
                                elif go == "N":
                                    what_doyou_mean = input("What do you want to do before? (Vendor/ Walk around/ NVM)")
                                    if what_doyou_mean == "Vendor":
                                        print("You see many vendors but only go to the ones specifically for your class.")
                                        if classs == "Barbarian":
                                            print("You walk up to a vendor selling an axe; 25 coins, a spear; 30 coins, and a dagger; 15 coins")
                                            bar = input("What do you want to buy? (Axe/Spear/Dagger) (You can only choose 1)")
                                            if bar == "Axe":
                                                result_4 = result_3-25
                                                print("You now have" , result_4)
                                            elif bar == "Spear":
                                                result_5 = result_3-30
                                                print("You now have" , result_5)
                                            elif bar == "Dagger":
                                                result_6 = result_3-15
                                                print("You now have" , result_6)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {bar}")
                                        elif classs == "Fighter":
                                            print("You go up to a vendor that is selling a dagger; 15 coins, a set of light armor; 45 coins, and a spear; 30 coins")
                                            fig = input("What do you want to buy? (Dagger/Light Armor/Spear) (You can only choose 1)")
                                            if fig == "Dagger":
                                                result_7 = result_3-15
                                                print("You now have" , result_7)
                                            elif fig == "Light Armor":
                                                result_8 = result_3-45
                                                print("You now have" , result_8)
                                            elif fig == "Spear":
                                                result_9 = result_3-30
                                                print("You now have" , result_9)
                                            else:
                                                print("Invalid answer!")
                                            print(f"You now have a {fig}")
                                        elif classs == "Monk":
                                            print("You go up to a vendor that is selling a set of clothes (tunic, and a cowl); 25 coins. Thats all.")
                                            mon = input("Do you want to buy the set of clothes? (Y/N)")
                                            if mon == "Y":
                                                result_10 = result_3-25
                                                print("You now have" , result_10, "and put on the clothes!")
                                            elif mon == "N":
                                                print("You dont get it all good!")
                                            else:
                                                print("Not a valid answer")
                                        elif classs == "Rogue":
                                            print("You go up to a vendor that is selling, a hood; 10 coins, a dagger; 15 coins, and a shawl; 20 coins")
                                            ro = input("What would you like to buy? (Hood/Dagger/Shawl) (Only able to get one)")
                                            if ro == "Hood":
                                                result_11 = result_3-10
                                                print("You now have" , result_11)
                                            elif ro == "Dagger":
                                                result_12 = result_3-15
                                                print("You now have" , result_12)
                                            elif ro == "Shawl":
                                                result_13 = result_3-20
                                                print("You now have" , result_13)
                                            else:
                                                print("Invalid answer!")
                                            print(f"You now have a {ro}")
                                        elif classs == "Bard":
                                            print("You go up to a vendor that is selling a rapier; 25 coins, a dagger; 15 coins, and a Lyre; 30 coins")
                                            ba = input("What would you like to buy? (Rapier/Dagger/Lyre) (Only able to buy one)")
                                            if ba == "Rapier":
                                                result_14 = result_3-25
                                                print("You now have" , result_14)
                                            elif ba == "Dagger":
                                                result_15 = result_3-15
                                                print("You now have" , result_15)
                                            elif ba == "Lyre":
                                                result_16 = result_3-30
                                                print("You now have" , result_16)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now own a {ba}")
                                        elif classs == "Cleric":
                                            print("You go up to a vendor that is selling a cross; 15 coins, bible; 20 coins, and a rapier; 25 coins")
                                            cle = input("What do you want to buy? (Bible/Cross/Rapier) (Only choose 1)")
                                            if cle == "Bible":
                                                result_17 = result_3-20
                                                print("You have" , result_17)
                                            elif cle == "Cross":
                                                result_18 = result_3-15
                                                print("You have" , result_18)
                                            elif cle == "Rapier":
                                                result_19 = result_3-15
                                                print("You have" , result_19)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {cle}")
                                        elif classs == "Druid":
                                            print("You go up to a vendor that is selling a set of forest clothes; 25 coins, a dagger; 15 coins")
                                            dru = input("What do you want to buy? (Forest Clothes/Dagger) (Can only choose 1)")
                                            if dru == "Forest Clothes":
                                                result_20 = result_3-25
                                                print("You have" , result_20)
                                            elif dru == "Dagger":
                                                result_21 = result_3-15
                                                print("You have" , result_21)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {dru}")
                                        elif classs == "Wizard":
                                            print("You go up to a vendor that is selling a staff; 20 coins, a spell book that gives you flame cast; 40 coins, and a set of light armor; 45 coins")
                                            wiz = input("What would you like to buy (Staff/Fire Spellbook/Light Armor) (You can only choose 1)")
                                            if wiz == "Staff":
                                                result_22 = result_3-20
                                                print("You now have" , result_22)
                                            elif wiz == "Fire Spellbook":
                                                result_23 = result_3-40
                                                print("You now have" , result_23)
                                            elif wiz == "Light Armor":
                                                result_24 = result_3-45
                                                print("You now have" , result_24)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {wiz}")
                                        elif classs == "Warlock":
                                            print("You go up to a vendor that is selling a dagger; 15 coins, crossbow(light); 20 coins")
                                            wa = input("What do you want to buy? (Crossbow/Dagger) (Crossbow comes 12 arrows")
                                            if wa == "Crossbow":
                                                result_25 = result_3-20
                                                print("You now have" , result_25)
                                            elif wa == "Dagger":
                                                result_29 = result_3-15
                                                print("You now have" , result_29)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {wa}")
                                        elif classs == "Paladin":
                                            print("You go up to a vendor that is selling a holy shield; 40 coins, long sword; 30 coins, heavy armor; 35 coins")
                                            pa = input("What would you like to buy (Holy Shield/Long Sword/Heavy Armor) (Only can have 1)")
                                            if pa == "Holy Shield":
                                                result_30 = result_3-40
                                                print("You now have" , result_30)
                                            elif pa == "Long Sword":
                                                result_31 = result_3-30
                                                print("You now have" , result_31)
                                            elif pa == "Heavy Armor":
                                                result_32 = result_3-35
                                                print("You now have" , result_32)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {pa}")
                                        elif classs == "Ranger":
                                            print("You go up to a vendor that is selling a short bow; 25 coins, crossbow; 30 coins, arrows; 5 per pack (10 per pack/3 packs)")
                                            ra = input("What do you want to buy? (Short Bow/Crossbow) (Only choose one, both bows come with 12 arrows)")
                                            if ra == "Short Bow":
                                                result_33 = result_3-25
                                                print("You now have" , result_33)
                                            elif ra == "Crossbow":
                                                result_34 = result_3-30
                                                print("You now have" , result_34)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have {ra}")
                                        else:
                                            print("You didn't pick a valid class!")
                                        print("Then you leave the gates of Aethelgard, going East you see a slime and slash it, nothing out of the ordinary... until you see dozens upon dozens of slimes!")
                                    elif what_doyou_mean == "Walk around":
                                        walk = input("You walk around, what now?(Go, Vendor")
                                        if walk == "Go":
                                            print("")
                                        elif walk == "Vendor":
                                            print("You see many vendors but only go to the ones specifically for your class.")
                                        if classs == "Barbarian":
                                            print("You walk up to a vendor selling an axe; 25 coins, a spear; 30 coins, and a dagger; 15 coins")
                                            bar = input("What do you want to buy? (Axe/Spear/Dagger) (You can only choose 1)")
                                            if bar == "Axe":
                                                result_4 = result_3-25
                                                print("You now have" , result_4)
                                            elif bar == "Spear":
                                                result_5 = result_3-30
                                                print("You now have" , result_5)
                                            elif bar == "Dagger":
                                                result_6 = result_3-15
                                                print("You now have" , result_6)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {bar}")
                                        elif classs == "Fighter":
                                            print("You go up to a vendor that is selling a dagger; 15 coins, a set of light armor; 45 coins, and a spear; 30 coins")
                                            fig = input("What do you want to buy? (Dagger/Light Armor/Spear) (You can only choose 1)")
                                            if fig == "Dagger":
                                                result_7 = result_3-15
                                                print("You now have" , result_7)
                                            elif fig == "Light Armor":
                                                result_8 = result_3-45
                                                print("You now have" , result_8)
                                            elif fig == "Spear":
                                                result_9 = result_3-30
                                                print("You now have" , result_9)
                                            else:
                                                print("Invalid answer!")
                                            print(f"You now have a {fig}")
                                        elif classs == "Monk":
                                            print("You go up to a vendor that is selling a set of clothes (tunic, and a cowl); 25 coins. Thats all.")
                                            mon = input("Do you want to buy the set of clothes? (Y/N)")
                                            if mon == "Y":
                                                result_10 = result_3-25
                                                print("You now have" , result_10, "and put on the clothes!")
                                            elif mon == "N":
                                                print("You dont get it all good!")
                                            else:
                                                print("Not a valid answer")
                                        elif classs == "Rogue":
                                            print("You go up to a vendor that is selling, a hood; 10 coins, a dagger; 15 coins, and a shawl; 20 coins")
                                            ro = input("What would you like to buy? (Hood/Dagger/Shawl) (Only able to get one)")
                                            if ro == "Hood":
                                                result_11 = result_3-10
                                                print("You now have" , result_11)
                                            elif ro == "Dagger":
                                                result_12 = result_3-15
                                                print("You now have" , result_12)
                                            elif ro == "Shawl":
                                                result_13 = result_3-20
                                                print("You now have" , result_13)
                                            else:
                                                print("Invalid answer!")
                                            print(f"You now have a {ro}")
                                        elif classs == "Bard":
                                            print("You go up to a vendor that is selling a rapier; 25 coins, a dagger; 15 coins, and a Lyre; 30 coins")
                                            ba = input("What would you like to buy? (Rapier/Dagger/Lyre) (Only able to buy one)")
                                            if ba == "Rapier":
                                                result_14 = result_3-25
                                                print("You now have" , result_14)
                                            elif ba == "Dagger":
                                                result_15 = result_3-15
                                                print("You now have" , result_15)
                                            elif ba == "Lyre":
                                                result_16 = result_3-30
                                                print("You now have" , result_16)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now own a {ba}")
                                        elif classs == "Cleric":
                                            print("You go up to a vendor that is selling a cross; 15 coins, bible; 20 coins, and a rapier; 25 coins")
                                            cle = input("What do you want to buy? (Bible/Cross/Rapier) (Only choose 1)")
                                            if cle == "Bible":
                                                result_17 = result_3-20
                                                print("You have" , result_17)
                                            elif cle == "Cross":
                                                result_18 = result_3-15
                                                print("You have" , result_18)
                                            elif cle == "Rapier":
                                                result_19 = result_3-15
                                                print("You have" , result_19)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {cle}")
                                        elif classs == "Druid":
                                            print("You go up to a vendor that is selling a set of forest clothes; 25 coins, a dagger; 15 coins")
                                            dru = input("What do you want to buy? (Forest Clothes/Dagger) (Can only choose 1)")
                                            if dru == "Forest Clothes":
                                                result_20 = result_3-25
                                                print("You have" , result_20)
                                            elif dru == "Dagger":
                                                result_21 = result_3-15
                                                print("You have" , result_21)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {dru}")
                                        elif classs == "Wizard":
                                            print("You go up to a vendor that is selling a staff; 20 coins, a spell book that gives you flame cast; 40 coins, and a set of light armor; 45 coins")
                                            wiz = input("What would you like to buy (Staff/Fire Spellbook/Light Armor) (You can only choose 1)")
                                            if wiz == "Staff":
                                                result_22 = result_3-20
                                                print("You now have" , result_22)
                                            elif wiz == "Fire Spellbook":
                                                result_23 = result_3-40
                                                print("You now have" , result_23)
                                            elif wiz == "Light Armor":
                                                result_24 = result_3-45
                                                print("You now have" , result_24)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {wiz}")
                                        elif classs == "Warlock":
                                            print("You go up to a vendor that is selling a dagger; 15 coins, crossbow(light); 20 coins")
                                            wa = input("What do you want to buy? (Crossbow/Dagger) (Crossbow comes 12 arrows")
                                            if wa == "Crossbow":
                                                result_25 = result_3-20
                                                print("You now have" , result_25)
                                            elif wa == "Dagger":
                                                result_29 = result_3-15
                                                print("You now have" , result_29)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {wa}")
                                        elif classs == "Paladin":
                                            print("You go up to a vendor that is selling a holy shield; 40 coins, long sword; 30 coins, heavy armor; 35 coins")
                                            pa = input("What would you like to buy (Holy Shield/Long Sword/Heavy Armor) (Only can have 1)")
                                            if pa == "Holy Shield":
                                                result_30 = result_3-40
                                                print("You now have" , result_30)
                                            elif pa == "Long Sword":
                                                result_31 = result_3-30
                                                print("You now have" , result_31)
                                            elif pa == "Heavy Armor":
                                                result_32 = result_3-35
                                                print("You now have" , result_32)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {pa}")
                                        elif classs == "Ranger":
                                            print("You go up to a vendor that is selling a short bow; 25 coins, crossbow; 30 coins, arrows; 5 per pack (10 per pack/3 packs)")
                                            ra = input("What do you want to buy? (Short Bow/Crossbow) (Only choose one, both bows come with 12 arrows)")
                                            if ra == "Short Bow":
                                                result_33 = result_3-25
                                                print("You now have" , result_33)
                                            elif ra == "Crossbow":
                                                result_34 = result_3-30
                                                print("You now have" , result_34)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have {ra}")
                                        else:
                                            print("You didn't pick a valid class!")
                                    
                                    elif what_doyou_mean == "NVM":
                                        print("You leave the gates of Aethelgard, going East you see a slime and slash it, nothing out of the ordinary... until you see dozens upon dozens of slimes!")
                                    else:
                                        print("Not a valid answer!")
                                else:
                                    print("Not a valid answer!")
                            elif chooseee == "2":
                                print("You go to the guild master and he lets you take on the quest. (Banish a banshee from the edge of the WrithingForests) \n A banshee is hard, if you're not a Cleric then you're going to need one.")
                                skele = input("The cleric is in the next town over in Jonshu, do you want to go to him or do you want to do something else before? (Go/No)")
                                if skele == "Go":
                                    print("You go towards Jonshu on foot and make it with no trouble.")
                                elif skele == "No":
                                    wwah = input("What do you want to do instead?(Vendor/Walk Around/NVM)")
                                    if wwah == "Vendor":
                                        if classs == "Barbarian":
                                            print("You walk up to a vendor selling an axe; 25 coins, a spear; 30 coins, and a dagger; 15 coins")
                                            bar = input("What do you want to buy? (Axe/Spear/Dagger) (You can only choose 1)")
                                            if bar == "Axe":
                                                result_4 = result_3-25
                                                print("You now have" , result_4)
                                            elif bar == "Spear":
                                                result_5 = result_3-30
                                                print("You now have" , result_5)
                                            elif bar == "Dagger":
                                                result_6 = result_3-15
                                                print("You now have" , result_6)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {bar}")
                                        elif classs == "Fighter":
                                            print("You go up to a vendor that is selling a dagger; 15 coins, a set of light armor; 45 coins, and a spear; 30 coins")
                                            fig = input("What do you want to buy? (Dagger/Light Armor/Spear) (You can only choose 1)")
                                            if fig == "Dagger":
                                                result_7 = result_3-15
                                                print("You now have" , result_7)
                                            elif fig == "Light Armor":
                                                result_8 = result_3-45
                                                print("You now have" , result_8)
                                            elif fig == "Spear":
                                                result_9 = result_3-30
                                                print("You now have" , result_9)
                                            else:
                                                print("Invalid answer!")
                                            print(f"You now have a {fig}")
                                        elif classs == "Monk":
                                            print("You go up to a vendor that is selling a set of clothes (tunic, and a cowl); 25 coins. Thats all.")
                                            mon = input("Do you want to buy the set of clothes? (Y/N)")
                                            if mon == "Y":
                                                result_10 = result_3-25
                                                print("You now have" , result_10, "and put on the clothes!")
                                            elif mon == "N":
                                                print("You dont get it all good!")
                                            else:
                                                print("Not a valid answer")
                                        elif classs == "Rogue":
                                            print("You go up to a vendor that is selling, a hood; 10 coins, a dagger; 15 coins, and a shawl; 20 coins")
                                            ro = input("What would you like to buy? (Hood/Dagger/Shawl) (Only able to get one)")
                                            if ro == "Hood":
                                                result_11 = result_3-10
                                                print("You now have" , result_11)
                                            elif ro == "Dagger":
                                                result_12 = result_3-15
                                                print("You now have" , result_12)
                                            elif ro == "Shawl":
                                                result_13 = result_3-20
                                                print("You now have" , result_13)
                                            else:
                                                print("Invalid answer!")
                                            print(f"You now have a {ro}")
                                        elif classs == "Bard":
                                            print("You go up to a vendor that is selling a rapier; 25 coins, a dagger; 15 coins, and a Lyre; 30 coins")
                                            ba = input("What would you like to buy? (Rapier/Dagger/Lyre) (Only able to buy one)")
                                            if ba == "Rapier":
                                                result_14 = result_3-25
                                                print("You now have" , result_14)
                                            elif ba == "Dagger":
                                                result_15 = result_3-15
                                                print("You now have" , result_15)
                                            elif ba == "Lyre":
                                                result_16 = result_3-30
                                                print("You now have" , result_16)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now own a {ba}")
                                        elif classs == "Cleric":
                                            print("You go up to a vendor that is selling a cross; 15 coins, bible; 20 coins, and a rapier; 25 coins")
                                            cle = input("What do you want to buy? (Bible/Cross/Rapier) (Only choose 1)")
                                            if cle == "Bible":
                                                result_17 = result_3-20
                                                print("You have" , result_17)
                                            elif cle == "Cross":
                                                result_18 = result_3-15
                                                print("You have" , result_18)
                                            elif cle == "Rapier":
                                                result_19 = result_3-15
                                                print("You have" , result_19)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {cle}")
                                        elif classs == "Druid":
                                            print("You go up to a vendor that is selling a set of forest clothes; 25 coins, a dagger; 15 coins")
                                            dru = input("What do you want to buy? (Forest Clothes/Dagger) (Can only choose 1)")
                                            if dru == "Forest Clothes":
                                                result_20 = result_3-25
                                                print("You have" , result_20)
                                            elif dru == "Dagger":
                                                result_21 = result_3-15
                                                print("You have" , result_21)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {dru}")
                                        elif classs == "Wizard":
                                            print("You go up to a vendor that is selling a staff; 20 coins, a spell book that gives you flame cast; 40 coins, and a set of light armor; 45 coins")
                                            wiz = input("What would you like to buy (Staff/Fire Spellbook/Light Armor) (You can only choose 1)")
                                            if wiz == "Staff":
                                                result_22 = result_3-20
                                                print("You now have" , result_22)
                                            elif wiz == "Fire Spellbook":
                                                result_23 = result_3-40
                                                print("You now have" , result_23)
                                            elif wiz == "Light Armor":
                                                result_24 = result_3-45
                                                print("You now have" , result_24)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {wiz}")
                                        elif classs == "Warlock":
                                            print("You go up to a vendor that is selling a dagger; 15 coins, crossbow(light); 20 coins")
                                            wa = input("What do you want to buy? (Crossbow/Dagger) (Crossbow comes 12 arrows")
                                            if wa == "Crossbow":
                                                result_25 = result_3-20
                                                print("You now have" , result_25)
                                            elif wa == "Dagger":
                                                result_29 = result_3-15
                                                print("You now have" , result_29)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {wa}")
                                        elif classs == "Paladin":
                                            print("You go up to a vendor that is selling a holy shield; 40 coins, long sword; 30 coins, heavy armor; 35 coins")
                                            pa = input("What would you like to buy (Holy Shield/Long Sword/Heavy Armor) (Only can have 1)")
                                            if pa == "Holy Shield":
                                                result_30 = result_3-40
                                                print("You now have" , result_30)
                                            elif pa == "Long Sword":
                                                result_31 = result_3-30
                                                print("You now have" , result_31)
                                            elif pa == "Heavy Armor":
                                                result_32 = result_3-35
                                                print("You now have" , result_32)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {pa}")
                                        elif classs == "Ranger":
                                            print("You go up to a vendor that is selling a short bow; 25 coins, crossbow; 30 coins, arrows; 5 per pack (10 per pack/3 packs)")
                                            ra = input("What do you want to buy? (Short Bow/Crossbow) (Only choose one, both bows come with 12 arrows)")
                                            if ra == "Short Bow":
                                                result_33 = result_3-25
                                                print("You now have" , result_33)
                                            elif ra == "Crossbow":
                                                result_34 = result_3-30
                                                print("You now have" , result_34)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have {ra}")
                                        else:
                                            print("You didn't pick a valid class!")
                                    elif wwah == "Walk Around":
                                        ssoo = input("You walk around (Go to Jonshu/Vendor)")
                                        if ssoo == "Vendor":
                                            if classs == "Barbarian":
                                                print("You walk up to a vendor selling an axe; 25 coins, a spear; 30 coins, and a dagger; 15 coins")
                                                bar = input("What do you want to buy? (Axe/Spear/Dagger) (You can only choose 1)")
                                            if bar == "Axe":
                                                result_4 = result_3-25
                                                print("You now have" , result_4)
                                            elif bar == "Spear":
                                                result_5 = result_3-30
                                                print("You now have" , result_5)
                                            elif bar == "Dagger":
                                                result_6 = result_3-15
                                                print("You now have" , result_6)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {bar}")
                                        elif classs == "Fighter":
                                            print("You go up to a vendor that is selling a dagger; 15 coins, a set of light armor; 45 coins, and a spear; 30 coins")
                                            fig = input("What do you want to buy? (Dagger/Light Armor/Spear) (You can only choose 1)")
                                            if fig == "Dagger":
                                                result_7 = result_3-15
                                                print("You now have" , result_7)
                                            elif fig == "Light Armor":
                                                result_8 = result_3-45
                                                print("You now have" , result_8)
                                            elif fig == "Spear":
                                                result_9 = result_3-30
                                                print("You now have" , result_9)
                                            else:
                                                print("Invalid answer!")
                                            print(f"You now have a {fig}")
                                        elif classs == "Monk":
                                            print("You go up to a vendor that is selling a set of clothes (tunic, and a cowl); 25 coins. Thats all.")
                                            mon = input("Do you want to buy the set of clothes? (Y/N)")
                                            if mon == "Y":
                                                result_10 = result_3-25
                                                print("You now have" , result_10, "and put on the clothes!")
                                            elif mon == "N":
                                                print("You dont get it all good!")
                                            else:
                                                print("Not a valid answer")
                                        elif classs == "Rogue":
                                            print("You go up to a vendor that is selling, a hood; 10 coins, a dagger; 15 coins, and a shawl; 20 coins")
                                            ro = input("What would you like to buy? (Hood/Dagger/Shawl) (Only able to get one)")
                                            if ro == "Hood":
                                                result_11 = result_3-10
                                                print("You now have" , result_11)
                                            elif ro == "Dagger":
                                                result_12 = result_3-15
                                                print("You now have" , result_12)
                                            elif ro == "Shawl":
                                                result_13 = result_3-20
                                                print("You now have" , result_13)
                                            else:
                                                print("Invalid answer!")
                                            print(f"You now have a {ro}")
                                        elif classs == "Bard":
                                            print("You go up to a vendor that is selling a rapier; 25 coins, a dagger; 15 coins, and a Lyre; 30 coins")
                                            ba = input("What would you like to buy? (Rapier/Dagger/Lyre) (Only able to buy one)")
                                            if ba == "Rapier":
                                                result_14 = result_3-25
                                                print("You now have" , result_14)
                                            elif ba == "Dagger":
                                                result_15 = result_3-15
                                                print("You now have" , result_15)
                                            elif ba == "Lyre":
                                                result_16 = result_3-30
                                                print("You now have" , result_16)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now own a {ba}")
                                        elif classs == "Cleric":
                                            print("You go up to a vendor that is selling a cross; 15 coins, bible; 20 coins, and a rapier; 25 coins")
                                            cle = input("What do you want to buy? (Bible/Cross/Rapier) (Only choose 1)")
                                            if cle == "Bible":
                                                result_17 = result_3-20
                                                print("You have" , result_17)
                                            elif cle == "Cross":
                                                result_18 = result_3-15
                                                print("You have" , result_18)
                                            elif cle == "Rapier":
                                                result_19 = result_3-15
                                                print("You have" , result_19)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {cle}")
                                        elif classs == "Druid":
                                            print("You go up to a vendor that is selling a set of forest clothes; 25 coins, a dagger; 15 coins")
                                            dru = input("What do you want to buy? (Forest Clothes/Dagger) (Can only choose 1)")
                                            if dru == "Forest Clothes":
                                                result_20 = result_3-25
                                                print("You have" , result_20)
                                            elif dru == "Dagger":
                                                result_21 = result_3-15
                                                print("You have" , result_21)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {dru}")
                                        elif classs == "Wizard":
                                            print("You go up to a vendor that is selling a staff; 20 coins, a spell book that gives you flame cast; 40 coins, and a set of light armor; 45 coins")
                                            wiz = input("What would you like to buy (Staff/Fire Spellbook/Light Armor) (You can only choose 1)")
                                            if wiz == "Staff":
                                                result_22 = result_3-20
                                                print("You now have" , result_22)
                                            elif wiz == "Fire Spellbook":
                                                result_23 = result_3-40
                                                print("You now have" , result_23)
                                            elif wiz == "Light Armor":
                                                result_24 = result_3-45
                                                print("You now have" , result_24)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {wiz}")
                                        elif classs == "Warlock":
                                            print("You go up to a vendor that is selling a dagger; 15 coins, crossbow(light); 20 coins")
                                            wa = input("What do you want to buy? (Crossbow/Dagger) (Crossbow comes 12 arrows")
                                            if wa == "Crossbow":
                                                result_25 = result_3-20
                                                print("You now have" , result_25)
                                            elif wa == "Dagger":
                                                result_29 = result_3-15
                                                print("You now have" , result_29)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {wa}")
                                        elif classs == "Paladin":
                                            print("You go up to a vendor that is selling a holy shield; 40 coins, long sword; 30 coins, heavy armor; 35 coins")
                                            pa = input("What would you like to buy (Holy Shield/Long Sword/Heavy Armor) (Only can have 1)")
                                            if pa == "Holy Shield":
                                                result_30 = result_3-40
                                                print("You now have" , result_30)
                                            elif pa == "Long Sword":
                                                result_31 = result_3-30
                                                print("You now have" , result_31)
                                            elif pa == "Heavy Armor":
                                                result_32 = result_3-35
                                                print("You now have" , result_32)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have a {pa}")
                                        elif classs == "Ranger":
                                            print("You go up to a vendor that is selling a short bow; 25 coins, crossbow; 30 coins, arrows; 5 per pack (10 per pack/3 packs)")
                                            ra = input("What do you want to buy? (Short Bow/Crossbow) (Only choose one, both bows come with 12 arrows)")
                                            if ra == "Short Bow":
                                                result_33 = result_3-25
                                                print("You now have" , result_33)
                                            elif ra == "Crossbow":
                                                result_34 = result_3-30
                                                print("You now have" , result_34)
                                            else:
                                                print("Not a valid answer!")
                                            print(f"You now have {ra}")
                                        else:
                                            print("You didn't pick a valid class!")
                                    elif ssoo == "Go to Gonshu":
                                        print("You leave and go to Gonshu")
                                    elif wwah == "NVM":
                                        print("You leave Aethelgard and go on foot to Jonshu, making it there safely.")
                                    else:
                                        print("Not a valid answer!")
                                else:
                                    print("Not a valid answer!")
                            elif chooseee == "3":
                                print("You go to the guild master and he lets you take on the quest. (Escort the princess of Gohmashi to Thornfell) \n Only one hint kid, dont try talking to her, her father wont like that.")  
                                start_mission = input("The princess is outside the gates of Aethelgard, go to her or do something before? (Go/No)")
                                if start_mission == "Go":
                                    print("You go outside and out the gates of Aethelgard, you see the princess and hop into the front of the carrage with the horses and take off.")
                                elif start_mission == "No":
                                    so = input("So what do you want to do instead? (Vendor/ Walk Around/NVM)")
                                    if so == "Vendor":
                                        print("You see different vendors and specifically for your class, you go to that one")
                                        if classs == "Barbarian":
                                            barbar = input("You walk up to a vendor selling an axe; 25 coins, a spear; 30 coins, and a dagger; 15 coins")
                                        elif classs == "Fighter":
                                            print("You go up to a vendor that is selling a dagger; 15 coins, a set of light armor; 45 coins, and a spear; 30 coins")
                                        elif classs == "Monk":
                                            print("You go up to a vendor that is selling a set of clothes (tunic, and a cowl); 25 coins. Thats all.")
                                        elif classs == "Rogue":
                                            print("You go up to a vendor that is selling, a hood; 10 coins, a dagger; 15 coins, and a shawl; 20 coins")
                                        elif classs == "Bard":
                                            print("You go up to a vendor that is selling a rapier; 25 coins, a dagger; 15 coins, and a Lyre; 30 coins")
                                        elif classs == "Cleric":
                                            print("You go up to a vendor that is selling a cross; 15 coins, bible; 20 coins, and a rapier; 25 coins")
                                        elif classs == "Druid":
                                            print("You go up to a vendor that is selling a set of forest clothes; 25 coins, a dagger; 15 coins")
                                        elif classs == "Wizard":
                                            print("You go up to a vendor that is selling a staff; 20 coins, a spell book that gives you flame cast; 40 coins, and a set of light armor; 45 coins")
                                        elif classs == "Warlock":
                                            print("You go up to a vendor that is selling a dagger; 15 coins, crossbow(light); 20 coins, arrows(for crossbow); 5 coins per pack(10 arrows a pack), a staff; 20 coins")
                                        elif classs == "Paladin":
                                            print("You go up to a vendor that is selling a holy shield; 40 coins, long sword; 30 coins, heavy armor; 35 coins")
                                        elif classs == "Ranger":
                                            print("You go up to a vendor that is selling a short bow; 25 coins, crossbow; 30 coins, arrows; 5 per pack (10 per pack)")
                                        else:
                                            print("You didn't pick a valid class!")
                                    elif so == "Walk Around":
                                        walkin = input("You walk around now what?(Vendor/Go to princess)")
                                    elif so =="NVM":
                                        print("You go to the princess and hop into the front and start off towards Gohmashi.")
                                    else:
                                        print("Not a valid answer!")
                                else:
                                    print("Not a valid answer!")
                        elif now_what == "Guild":
                            print(f"You see three different quests {item_2}, {item_6}, and {item_3}.")
                            choose_1 = input(f"Which one do you choose? ({item_2}, {item_6}, or {item_3}(1,2, or 3))")
                            if choose_1 == "1":
                                print(f"You decided to take {item_2}, you take it to the guild master and he allows you to take it. \n Good luck kid Thornfell is to the west, I suggest preparing for the harsh weather on the way.")
                            elif choose_1 == "2":
                                print(f"You decided to take {item_6}, you take it to the guild master and he allows you to take it. \n Good luck kid, Gohmashi is due East, the princess is outside the gates waiting, when you're ready then go to her and speak with her.")
                            elif choose_1 == "3":
                                print(f"You decided to take {item_3}, you take it to the guild master and he allows you to take it. \n Good luck kid, only one piece of advice, never look at its eyes. ")
                        else:
                            print("Not a valid answer!")  
                        
                    elif coins == "Map and Quill":
                        result_2 = 250-20
                        print("You bought the map and quill! You now have" , result_2, "coins")
                        ti.sleep(2)
                        bought = input("You have" , result_2, "coins, would you like to buy the sword as well or no? (Y/N)")
                        if bought == "Y":
                            result_alt = 230-15
                            print("You now have" , result_alt, "coins. Now you put the map and quill in your bag and sheath the sword.")
                            where = input("Do you want to go to the Guild or travel? (Guild/Travel)")
                            if where == "Guild":
                                print("You go to the guild nearby.")
                                quest = input(f"You see three quests, {item_9}, {item_6}, and {item_8} what quest would you like to go on? (1,2,3)")
                                if quest == "1":
                                    print("You go to the guild master to talk to him about it and he lets you take it \n good luck kid, killing a manticore is no easy task... I would sugest geting a fire sword from the shop smith, mind you they're at least 200 coins at most.")
                                elif quest == "2":
                                    print("You go to the guild master to talk to him about it and he lets you take the quest. \n good luck kid, Keep the skeletons the necromancer uses at bay, let the .")
                                elif quest == "3":
                                    print("You go to the guild master to talk to him about it and he lets you take the quest. \n good luck kid, just be careful the full moon is soon.")
                                else:
                                    print("Not a valid answer!")
                            elif where == "Travel":
                                to_where = input("Where do you want to go, (Village, Forest, Cave, Desert?")
                                if to_where == "Village":
                                    print("")
                                elif to_where == "Forest":
                                    print("")
                                elif to_where == "Cave":
                                    print("")
                                elif to_where == "Desert":
                                    print("")
                                else:
                                    print("Not a valid answer!")
                            else:
                                print("Not a valid answer!")   

                        elif bought == "N":
                            print("Okay!")
                        else:
                            print("That's not a valid answer!")
            elif choice_first == "Thornfell":
                print("You get to the bustling city of Thornfell.")
                what = input("What do you want to do, there's no guilds around, but there are vendors would you like to go to one?(Y/N)")
                if what == "Y":
                    print(f"You go to a vendor named: {demi} \n they have a sword/15 coins, map and quill/20 coins, and a staff/20 coins")
                    buy_alr = input("Would you like to buy? (Y/N)")
                    if buy_alr == "Y":
                        ask = input("What would you like to buy? You have 250 coins (Sword, Map and Quill, or Staff)")
                        if ask == "Sword":
                            results = 250-15
                            print("You now have" ,results , "coins, now you have a sword!")
                            buy_mkre = input("Would you like to buy any thing else? (Map and Quill/Staff)")
                            if buy_mkre == "Map and Quill":
                                resultt = 235-20
                            elif buy_mkre == "Staff":
                                resuult = 235-20
                            else:
                                print("Not a valid answer!")
                        elif ask == "Map and Quill":
                            reesults = 250-20
                        elif ask == "Staff":
                            reslute = 250-20
                        else:
                            print("Not a valid answer!")
                    elif buy_alr == "N":
                        why = input("What do you want to do instead? (Travel/Aethelgard/Plains")
                        if why == "Travel":
                            print("You leave Thornfell and enter the nearby cave.")
                        elif why == "Aethelgard":
                            print("You travel to the bustling city of Aethelgard, you see vendors and a guild. \n What would you like to do?")
                            what_like = input("Go to a vendor? Go to a guild? (Vendor/Guild)")
                elif what == "N":
                    question = input("Where do you want to go instead? (Town, Forest, Cave)")
                else:
                    print("Not a valid answer!")
            else:
                print("Not a valid answer")
        elif story == "N":
            print("All Good!")
            ti.sleep(1)
            choice_first_alt = input("Where do you want to go? (Cave/Forest)")
            if choice_first_alt == "Cave":
                print("You travel to a cave, only with a sword and map and quill, on the map shows different places like, Aethelgard, Thornfell, and Whisperwoods which is nearby.")
                goin = input("Do you want to go in? (Y/N)")
                if goin == "Y":
                    print("You go in... it's dark, damp, you hear a bat screech... wait... a bat?")
                    surprise = input("A vampire attacks you! You barely dodge! What do you do! (Flee, Fight)")
                    if surprise == "Flee":
                        print("You run!")
                        ah = input("Where do you run off to? (Forest, Thornfell, Aethelgard)")
                    elif surprise == "Fight":
                        print("You take out your sword and slash at the vampire, it dodges!")
                elif goin == "N":
                    where_alt = input("Where do you want to go instead? (Village, Plains, Forest)")
                else:
                    print("Not a valid answer!")
            elif choice_first_alt == "Forest":
                print("You travel into the forest called Whisperwoods, its very foggy and humid only able to see five feet in front of you. You have a sword and a map and quill.")
                further = input("Do you want to go further in? (Y/N)")
                if further == "Y":
                    print("You go in further and it gets more foggy, then you hear a rustle in a tree...")
                    attack = input("An Owlbear attacks! You barely dodge it's razor sharp claws... what do you do? (Flee, Fight)")
                elif further == "N":
                    where_now = input("Where do you want to go instead? (Village, Plains, Cave)")
                else:
                    print("Not a valid answer!")
            else:
                print("Not a valid answer!")
        else:
            print("Not a valid answer!")
    elif play == "N":
        print("That's to bad, let's play another ti.")

    else:
        print("That's not a valid answer! Try again!")












def main():
    mononster = monsters()
    regular = human_vendors()
    demi = anthro_vendors()
    quests = bounties()
    classes = powers()
    play_game(mononster, regular, demi, quests, classes)
if __name__ == "__main__":
    main()
