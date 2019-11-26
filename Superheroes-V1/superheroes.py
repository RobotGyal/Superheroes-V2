import random
import sys

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength
    def attack(self):
        return random.randint(0,self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    def block(self):
        return random.randint(0, self.max_block)

class Weapon(Ability):
    def attack(self):
        return random.randint(self.max_damage//2, self.max_damage)

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.kills = 0
        self.deaths = 0
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)
    def add_armor(self, armor):
        '''Add armore to self.armor'''
        self.armors.append(armor)
    def add_kill(self, num_kills):
        self.kills += num_kills
    def add_deaths(self, num_deaths):
        self.deaths+=num_deaths
    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)

    def attack(self):
        total_damage=0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self, damage_amt=0):
        total_armor = 0
        for damage_amt in self.armors:
            total_armor += damage_amt.block()
        return total_armor

    def take_damage(self, damage):
        self.current_health -= damage

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        while self.is_alive() == True and opponent.is_alive() == True:
            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())
            if opponent.is_alive() == False: #if opponent loses
                self.add_kill(1)
                opponent.add_deaths(1)
                print("Winner is: ", self.name)
            else: #if opponent wins
                self.add_deaths(1)
                opponent.add_kill(1)
                print("Winner is: ", opponent.name)

class Team(Hero):
    def __init__(self, name):
        self.name = name
        self.heroes = []
        self.alive = []

    def add_hero(self, hero):
        self.heroes.append(hero)
    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero) 
        return 0
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def remaining_alive(self):
        for hero in self.heroes:
            if hero.is_alive():
                alive.append(hero)
        return alive
    def attack(self, other_team):
        hero = random.choice(self.remaining_alive())
        opponent = random.choice(other_team.remaining_alive())
        return hero.fight(opponent)
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health
    def stats(self):
        print("Here are the current team stats: \n")
        for hero in self.heroes:
            print("Hero: ", hero.name)
            print("Number of kills: ", str(hero.kills))
            print ("Number of deaths: ", str(hero.deaths))

class Arena:
    def __init__(self):

        self.team_one = None
        self.team_two = None
        self.winning_team = None

    def create_ability(self):
        '''Prompt for ability info
        Return abilities and values from user inputs'''
        Ability.name = input("Please enter a ability: ")
        Ability.attack_strength = input("Please enter a attack strength: ")
        return Ability.name, Ability.attack_strength

    def create_weapon(self):
        '''Prompt for weapon info
        Return weapon and values from user inputs'''
        Weapon.name = input("Please enter a weapon: ")
        Weapon.attack_strength = input("Please enter a attack strength: ")
        return Weapon.name, Weapon.attack_strength

    def create_armor(self):
        '''Prompt for Armor info
        Return armor and values from user inputs'''
        Armor.name = input("Please enter a armor: ")
        Armor.max_block = input("Please enter a block strength: ")
        return Armor.name, Armor.max_block

    def create_hero(self):
        '''Prompt for hero information
        return Hero with assosciates values 
        '''
        hero_name= input("\nPlease pick a name for your hero  ")
        starting_health = input("What is your heroes starting health?  ")
        hero = Hero(hero_name, starting_health)

        adding = True
        while adding:
            option = input("Would you like to add: armor(A), ability(B), weapon(W), or Finished(F) ")
            if option.lower() == 'a':
                armor = self.create_armor()
                hero.add_armor(armor)
            elif option.lower() == 'b':
                ability = self.create_ability()
                hero.add_ability(ability)
            elif option.lower() == 'w':
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif option.lower() == 'f':
                adding = False
            else:
                print("Invalid response")
        return hero
    def attack(self):
        pass
    def build_team_one(self):
        name = input("\nWhat is the name of Team 1? ")
        self.team_one=Team(name)
        team_one_size = input("How many heros do you want on your first team?  ")
        for hero in range(int(team_one_size)):
            self.create_hero()
            self.team_one.add_hero(hero)
    def build_team_two(self):
        name = input("\nWhat is the name of Team 2? ")
        self.team_two=Team(name)
        team_two_size = input("How many heros do you want on your second team?  ")
        for hero in range(int(team_two_size)):
            self.create_hero()
            self.team_two.add_hero(hero)
    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        self.team_one.stats()
        self.team_two.stats()

        if len(self.team_one.remaining_alive())>0 and len(self.team_two.remaining_alive()) == 0:
            self.winning_team = self.team_one
            print("The winning team is team {}! Congratulations!".format(self.winning_team))
            return self.winning_team
        else:
            self.winning_team = self.team_two
            print("The winning team is team {}! Congratulations!".format(self.winning_team))
            return self.winning_team



if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()