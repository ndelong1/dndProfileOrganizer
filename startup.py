#creates a player's Character instance, and stores all items

#Assist Player in Character build
from Player import *
from rollAttribute import *


user_profiles = {}

NAME = input("What is your Characters Name? >> ")
race_info = "Dwarf: Dwarves are stout and sturdy, known for their craftsmanship and resilience. They have subraces like Hill Dwarf and Mountain Dwarf.\nElf: Elves are graceful and agile beings with a deep connection to nature. Subraces include High Elf, Wood Elf, and Dark Elf (Drow).\nHalfling: Halflings are small and nimble folk who often possess a strong sense of luck. Subraces include Lightfoot Halfling and Stout Halfling.\nHuman: Humans are versatile and adaptable, with no specific subraces.\nDragonborn: Dragonborn have dragon-like features and are known for their breath weapons. They are not divided into subraces.\nGnome: Gnomes are inventive and curious, with a knack for tinkering. Subraces include Forest Gnome and Rock Gnome.\nHalf-Elf: Half-elves are a mix of human and elf ancestry, with a balance of both races' qualities.\nHalf-Orc: Half-orcs combine the strengths of humans and orcs, often serving as formidable warriors.\nTiefling: Tieflings have infernal ancestry, often displaying demonic features and possessing unique abilities.\nAarakocra: Bird-like humanoid creatures that can fly.\nGenasi: Genasi are tied to the elements and have subraces representing Earth, Air, Fire, and Water Genasi.\nAasimar: Aasimar are celestial-blooded and often serve as champions of good.\nTriton: Tritons are aquatic beings, adapted to life underwater.\nFirbolg: Large, reclusive creatures with a strong connection to nature.\nGoliath: Massive and strong, Goliaths are known for their endurance and athleticism.\nTabaxi: Cat-like humanoids with agility and curiosity.\nKenku: Crow-like creatures known for their mimicry and artistic talents.\nLizardfolk: Reptilian humanoids with an affinity for water and survival skills.\nYuan-Ti Pureblood: Serpent-like humanoids with a wide range of abilities.\nChangeling: Shape-shifters with the ability to change their appearance.\nKalashtar: Mystical beings with psychic abilities and a connection to dreams.\nShifters: Humanoid shape-shifters with animal-like features.\nWarforged: Constructs created for warfare, now seeking purpose in peacetime.\nMinotaur: Bull-headed beings with great strength and combat abilities\nCentaur: Half-human, half-horse creatures known for their speed and archery skills.\nGith: The Gith race includes Githyanki and Githzerai, each with distinct abilities and backgrounds.\nKobold: Small, reptilian humanoids known for their cleverness and traps.\nGoblin: Small and agile creatures often associated with mischief and cunning.\nHobgoblin: Larger and militaristic goblins with a penchant for discipline and strategy.\nBugbear: Tall and menacing goblinoids with a natural aptitude for stealth."
print(race_info)
RACE = input("What race is your Character? >> ")
class_info = "Barbarian\n\tPath of the Berserker\n\tPath of the Totem Warrior\n\tPath of the Ancestral Guardian\n\tPath of the Storm Herald\n\tPath of the Zealot\n\tPath of the Wild Soul (Unearthed Arcana)\nBard\n\tCollege of Lore\n\tCollege of Valor\n\tCollege of Glamour\n\tCollege of Swords\n\tCollege of Whispers\n\tCollege of Eloquence (Mythic Odysseys of Theros)\n\tCollege of Creation (Unearthed Arcana)\nCleric\n\tKnowledge Domain\n\tLife Domain\n\tLight Domain\n\tNature Domain\n\tTempest Domain\n\tTrickery Domain\n\tWar Domain\n\tForge Domain (Xanathar's Guide to Everything)\n\tGrave Domain (Xanathar's Guide to Everything)\n\tOrder Domain (Guildmasters' Guide to Ravnica)\n\tPeace Domain (Mythic Odysseys of Theros)\n\tTwilight Domain (Unearthed Arcana)\nDruid\n\tCircle of the Land\n\tCircle of the Moon\n\tCircle of Dreams (Xanathar's Guide to Everything)\n\tCircle of the Shepherd (Xanathar's Guide to Everything)\n\tCircle of Spores (Guildmasters' Guide to Ravnica)\n\tCircle of the Stars (Unearthed Arcana)\nFighter\n\tChampion\n\tBattle Master\n\tEldritch Knight\n\tArcane Archer (Xanathar's Guide to Everything)\n\tCavalier (Xanathar's Guide to Everything)\n\tSamurai (Xanathar's Guide to Everything)\n\tPsi Knight (Unearthed Arcana)\nMonk\n\tWay of the Open Hand\n\tWay of Shadow\n\tWay of the Four Elements\n\tWay of the Drunken Master (Xanathar's Guide to Everything)\n\tWay of the Kensei (Xanathar's Guide to Everything)\n\tWay of the Sun Soul (Xanathar's Guide to Everything)\n\tWay of Mercy (Unearthed Arcana)\nPaladin\n\tOath of Devotion\n\tOath of the Ancients\n\tOath of Vengeance\n\tOath of Conquest (Xanathar's Guide to Everything)\n\tOath of Redemption (Xanathar's Guide to Everything)\n\tOath of the Crown (Sword Coast Adventurer's Guide)\n\tOath of Glory (Mythic Odysseys of Theros)\n\tOath of the Watchers (Unearthed Arcana)\nRanger\n\tHunter\n\tBeast Master\n\tGloom Stalker (Xanathar's Guide to Everything)\n\tHorizon Walker (Xanathar's Guide to Everything)\n\tMonster Slayer (Xanathar's Guide to Everything)\n\tFey Wanderer (Unearthed Arcana)\n\tSwarmkeeper (Unearthed Arcana)\nRogue\n\tThief\n\tAssassin\n\tArcane Trickster\n\tSwashbuckler (Sword Coast Adventurer's Guide)\n\tMastermind (Xanathar's Guide to Everything)\n\tInquisitive (Xanathar's Guide to Everything)\n\tScout (Unearthed Arcana)\n\tPhantom (Unearthed Arcana)\nSorcerer\n\tDraconic Bloodline\n\tWild Magic\n\tStorm Sorcery (Xanathar's Guide to Everything)\n\tDivine Soul (Xanathar's Guide to Everything)\n\tShadow Magic (Xanathar's Guide to Everything)\n\tClockwork Soul (Unearthed Arcana)\nWarlock\n\tThe Archfey\n\tThe Fiend\n\tThe Great Old One\n\tThe Celestial (Xanathar's Guide to Everything)\n\tThe Hexblade (Xanathar's Guide to Everything)\n\tThe Undying (Sword Coast Adventurer's Guide)\n\tThe Genie (Unearthed Arcana)\nWizard\n\tSchool of Abjuration\n\tSchool of Conjuration\n\tSchool of Divination\n\tSchool of Enchantment\n\tSchool of Evocation\n\tSchool of Illusion\n\tSchool of Necromancy\n\tSchool of Transmutation\n\tBladesinging (Sword Coast Adventurer's Guide)\n\tWar Magic (Xanathar's Guide to Everything)\n\tOrder of Scribes (Unearthed Arcana)"
print(class_info)
CLASS_INFO = input("What is your character's class? >> ")


#create_profile = input("Would you like to create a new Profile? (Y or N) >> ")



profile = Player(NAME, RACE, CLASS_INFO)

print(f"Random Attribute Scores: {attribute_scores}")

s = input("What is your Strength score? >> ")
d = input("What is your Dexterity score? >>")
c = input("What is your Constitution score? >>")
i = input("What is your Intelligence score? >>")
w = input("What is your Wisdom score? >>")
ch = input("What is your Charisma score? >>")

profile.set_attributes("strength", s)
profile.set_attributes("dexterity", d)
profile.set_attributes("constitution", c)
profile.set_attributes("intelligence", i)
profile.set_attributes("wisdom", w)
profile.set_attributes("charisma", ch)

#set skill mods: 












print(profile.get_player_info())
print(profile.set_attribute_mods())