class Ability:
    def __init__(self, name, attack_strength):
        # Initialize starting values
        self.name = name
        self.attack_strength = int(attack_strength)

    def attack(self):
        # Return attack value
        return self

    def update_attack(self, attack_strength):
        # Update attack value
        self.attack_strength +=1


class Hero:
    def __init__(self, name, health = 100):
        # Initialize starting values
        self.name = name
        self.abilities = []

    def add_ability(self, ability):
        # Add ability to abilities list
        self.abilities.append(ability)

    def attack(self):
        # Run attack() on every ability hero has
        
