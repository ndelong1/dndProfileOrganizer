class DNDPlayer:
    def __init__(self, name, race, character_class, level=1):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.level = level
        self.hit_points = 10  # Initial hit points
        self.skills = {}  # Dictionary to store skills and their levels

    def level_up(self):
        self.level += 1
        self.hit_points += 5  # Increase hit points on level up

    def add_skill(self, skill_name, skill_level):
        self.skills[skill_name] = skill_level

    def get_skills(self):
        return self.skills

    def get_info(self):
        info = f"Name: {self.name}\nRace: {self.race}\nClass: {self.character_class}\nLevel: {self.level}\nHit Points: {self.hit_points}\nSkills: {', '.join(self.skills.keys())}"
        return info

# Example usage:
# Create a D&D player character
player1 = DNDPlayer("Eldric", "Elf", "Wizard")
player1.add_skill("Arcana", 5)
player1.add_skill("History", 4)

# Level up the character
player1.level_up()

# Display player character information
print(player1.get_info())