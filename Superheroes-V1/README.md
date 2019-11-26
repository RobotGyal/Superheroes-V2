# Superhero Team!
"There are times when the powers of good and evil come together in a mighty clash of force. When this happens, it's up to all of us to make sure that we make every one of our assets count. What better than a simulation to make sure you have the best team with you when the time comes to stand up to the evil forces of the galaxy's greatest foes.

Our task is to create a superhero team dueling application so we can be sure we've got the best people to fight evil with. This time we're going to use Object Oriented Programming to build our applications instead of relying completely on functions."

## Code Example
```
    def fight(self, opponent):
        while (self.is_alive() == True and opponent.is_alive() == True):
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
```

## Frameworks
This project was built with
* pytest
* requests
For a complete list see `requirements.txt`

## Features

## Installation

## Testing

## How to Use