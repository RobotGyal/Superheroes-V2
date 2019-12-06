import random

class Ability:
    def __init__(self, name, attack_strength):
        '''
       Initialize the values passed into this
       method as instance variables.
        '''

        self.name = name
        self.max_damage = int(attack_strength)

    def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''

      random_value = random.randint(0, self.max_damage)
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

class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        random_value = random.randint(self.max_damage//2, self.max_damage)
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
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        self.armors.append(armor)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total_damage:Int
        '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):  #, damage_amt
        '''Calculate the total block amount from all armor blocks.
            return: total_block:Int
        '''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        defense = self.defend()    
        self.current_health -= damage - defense

    def is_alive(self):  
        '''Return True or False depending on whether the hero is alive or not.
        '''
        if self.current_health <= 0:
            return False
        return True

    def fight(self, opponent):
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
        else:
            while self.is_alive() and opponent.is_alive():
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
                if opponent.is_alive() == False: #if opponent loses
                    print("Winner is: ", self.name)
                    self.add_kill(1)
                    opponent.add_death(1)
                else: #if opponent wins
                    print("Winner is: ", opponent.name)
                    self.add_death(1)
                    opponent.add_kill(1)

    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.kills += num_deaths

class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes
        '''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def view_all_heroes(self):
            '''Prints out all heroes to the console.'''
            for hero in self.heroes:
                print(hero.name)

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero)

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            print("Hero: ", hero.name)
            print("Number of kills: ", str(hero.kills))
            print ("Number of deaths: ", str(hero.deaths))
            if hero.deaths == 0:
                print("No deaths and {hero.kills} kills")
            else:
                kd = hero.kills / hero.deaths
                print("Kill/Deaths: ", kd)

    def survivors(self):
        living = list()
        for hero in self.heroes:
            if hero.is_alive():
                living.append(hero)
        return living

    def revive_heroes(self):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        while len(self.survivors()) > 0 or len(other_team.survivors() > 0):
            hero = random.choice(self.survivors())
            opponent = random.choice(other_team.survivors())

            return hero.fight(opponent)
            
class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = list()
        self.team_two = list()

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        ability = input("What is the ability name?  ")
        max_damage = input("What is the max damage of the ability?  ")

        return Ability(ability, max_damage)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        weapon = input("What is the name of the weapon?")
        max_damage = input("What is the max damage of the weapon?")
        return Weapon(weapon, max_damage)

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        armor = input("What type of armor will you add to your hero?")
        max_block = input("What is the max block foor the armor?")
        return Armor(armor, max_block)

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add Armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               ability = self.create_ability()
               hero.add_ability(ability)
           elif add_item == "2":
               weapon = self.create_weapon()
               hero.add_weapon(weapon)
           elif add_item == "3":
               armor = self.create_armor()
               hero.add_armor(armor)
        return hero

    def build_team_one(self):
        name = input("\nWhat is the name of Team 1? ")
        team_one_size = input("How many heros do you want on your first team?  ")
        self.team_one = Team(name)
        for _ in range(int(team_one_size)):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        name = input("\nWhat is the name of Team 2? ")
        team_two_size = input("How many heros do you want on your second team?  ")
        self.team_two = Team(name)
        for _ in range(int(team_two_size)):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)
        if len(self.team_one.survivors()) > 0 and len(self.team_two.survivors()) == 0:
            self.winner = self.team_one.name
            return self.winner
        else:
            self.winner = self.team_two.name
            return self.winner

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Show surviving heroes.
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        # Some help on how to achieve these tasks:
        # TODO: for each team, loop through all of their heroes,
        # and use the is_alive() method to check for alive heroes,
        # printing their names and increasing the count if they're alive.
        #
        # TODO: based off of your count of alive heroes,
        # you can see which team has more alive heroes, and therefore,
        # declare which team is the winning team
        #
        # TODO for each team, calculate the total kills and deaths for each hero,
        # find the average kills and deaths by dividing the totals by the number of heroes.
        # finally, divide the average number of kills by the average number of deaths for each team
        self.team_one.stats()
        self.team_two.stats()
        




if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    
    arena.show_stats()