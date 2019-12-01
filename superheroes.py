import random

class Ability:
    def __init__(self, name, attack_strength):
        '''
       Initialize the values passed into this
       method as instance variables.
        '''

        self.name = name
        self.max_damage = attack_strength

    def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''

      random_value = random.randint(0,self.max_damage)
      return random_value


class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''

        self.name = name
        self.max_block = max_block

    def block(self):
        '''
        Return a random value between 0 and the
        initialized max_block strength.
        '''
        random_value = random.randint(0, self.max_block)
        return random_value

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
        '''

        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        ''' Add ability to abilities list '''

        self.abilities.append(ability)




if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Debugging Ability", 50)
    print(ability.name)
    print(ability.attack())
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())
    hero = Hero("Grace Hopper", 200)
    print(hero.name)
    print(hero.current_health)
    hero.add_ability(ability)
    print(hero.abilities)
