# This exercise asks you to come up with a class design for a Role-playing Game.
# -   The application has information about every player. They all have a name, health, strength and intelligence.
# -   When each player is created, it gets:
#     -   a health value of 100
#     -   a random strength value (between 2 and 12, inclusive)
#     -   a random intelligence value (between 2 and 12 inclusive)
#     The random values are determined by a call to a `roll_dice` method that **shouldn't** be accessed outside of the class. The `roll_dice` method should not take any arguments.
# @@@-   You can set and change the strength and intelligence in the constructors. However, once an object is constructed, the values may not change.
# -   Health can only be changed by the methods `heal` and `hurt`. Each method accepts one argument, the amount of change to the health. 
#     The `heal` increases the health value by the indicated amount, while the `hurt` decreases the value.
# -   A player can be a warrior, a paladin, a magician, or a bard.
# -   Warriors receive an additional 2 points of strength when they're created. The resulting strength range is thus between 4 and 14, inclusive.
# -   Magicians receive an additional 2 points of intelligence when they're created. The resulting intelligence range is thus between 4 and 14, inclusive.
# -   Warriors and paladins have the ability to wear armor. They need access to 2 additional methods: `attach_armor` and `remove_armor`.
# -   Paladins, magicians and bards can cast spells. They need access to a `cast_spell` method, that accepts one argument, `spell`.
# -   Bards are a special type of magician that can also create potions. They have a `create_potion` method.
# -   If you pass a player instance to `print` function, it should print information about the player in this format:
#     ```plaintext
#     Name: John
#     Class: Warrior
#     Health: 100
#     Strength: 7
#     Intelligence: 5
#     ```
# Create a set of classes based on the description of the role-playing application. Your classes should show any inheritance relationships, mix-in inheritance, 
#  and methods necessary to meet the requirements.
# This exercise is about designing class relationships, and how you organize your classes, behaviors, and state. Your methods should provide the details needed 
#  to fulfill the requirements. In some cases, you may be able to use `pass` as the method body. Don't include any functionality we don't describe above. 
#  In particular, you don't need to show the code that fetches, adds, deletes, or updates players.

import random

class ArmourMixin:
# -   Warriors and paladins have the ability to wear armor. They need access to 2 additional methods: `attach_armor` and `remove_armor`.
    def attach_armor(self, armour_piece):
        pass
        
    def remove_armor(self, armour_piece):
        pass

class SpellMixin:
# -   Paladins, magicians and bards can cast spells. They need access to a `cast_spell` method, that accepts one argument, `spell`.
    def cast_spell(self, spell):
        pass

# -   The application has information about every player. They all have a name, health, strength and intelligence.
# -   When each player is created, it gets:
#     -   a health value of 100
#     -   a random strength value (between 2 and 12, inclusive)
#     -   a random intelligence value (between 2 and 12 inclusive)
#     The random values are determined by a call to a `roll_dice` method that **shouldn't** be accessed outside of the class. The `roll_dice` method should not take any arguments.
# @@@-   You can set and change the strength and intelligence in the constructors. However, once an object is constructed, the values may not change.
#           - From Brandi: "I think if I were working on this as a take-home project and couldn't ask for clarification, I would default to the highest level of restriction."
class Character:
    STARTING_HP = 100

    def __init__(self, name):
        self.name = name
        self._health = Character.STARTING_HP
        self.__str = self._roll_dice()
        self.__intel = self._roll_dice()

    @staticmethod
    def _roll_dice():
        return random.randint(2, 12)

# -   Health can only be changed by the methods `heal` and `hurt`. Each method accepts one argument, the amount of change to the health. 
#     The `heal` increases the health value by the indicated amount, while the `hurt` decreases the value.
    def heal(self, amount):
        self._health += amount

    def hurt(self, amount):
        self._health -= amount
    
    # -   If you pass a player instance to `print` function, it should print information about the player in this format:
#     ```plaintext
#     Name: John
#     Class: Warrior
#     Health: 100
#     Strength: 7
#     Intelligence: 5
#     ```
    def __str__(self):
        return (f'Name: {self.name}'
                f'\nClass: {self.__class__.__name__}'
                f'\nHealth: {self._health}'
                f'\nStrength: {self.__str}'
                f'\nIntelligence: {self.__intel}\n'
        )

# -   A player can be a warrior, a paladin, a magician, or a bard.
class Warrior(ArmourMixin, Character):
# -   Warriors receive an additional 2 points of strength when they're created. The resulting strength range is thus between 4 and 14, inclusive.
# -   Warriors and paladins have the ability to wear armor. They need access to 2 additional methods: `attach_armor` and `remove_armor`.
    def __init__(self, name):
        super().__init__(name)
        self._Character__str += 2

class Paladin(ArmourMixin, SpellMixin, Character):
# -   Warriors and paladins have the ability to wear armor. They need access to 2 additional methods: `attach_armor` and `remove_armor`.
# -   Paladins, magicians and bards can cast spells. They need access to a `cast_spell` method, that accepts one argument, `spell`.
    pass

class Magician(SpellMixin, Character):
# -   Magicians receive an additional 2 points of intelligence when they're created. The resulting intelligence range is thus between 4 and 14, inclusive.
# -   Paladins, magicians and bards can cast spells. They need access to a `cast_spell` method, that accepts one argument, `spell`.
    def __init__(self, name):
        super().__init__(name)
        self._Character__intel += 2
    
class Bard(Magician):
# -   Paladins, magicians and bards can cast spells. They need access to a `cast_spell` method, that accepts one argument, `spell`.
# -   Bards are a special type of magician that can also create potions. They have a `create_potion` method.
    def create_potion(self):
        pass

warrior = Warrior('Joe')
paladin = Paladin('Bob')
magician = Magician('Frank')
bard = Bard('Jeff')

print(warrior)
print(paladin)
print(magician)
print(bard)

# print(bard._Character__intel)
