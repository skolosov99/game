from abc import ABC, abstractmethod
import random

# Unit
# __init__
# health
# attack
# name
# defence

class Unit(ABC):

    _name = None
    _health = 100
    _dmg = 10
    _defence = 5

    def hp_check(self):
        if self._health < 0:
            self._health = 0

    @property
    def damage_multiplier(self):
        crit = 0.5
        if random.random < crit:
            return 1
        return 2

    @property
    def miss_multiplier(self):
        miss = 0.5
        if random.random < miss:
            return 1
        return 0


    @property
    def is_alive(self):
        return self._health > 0

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def _get_dmg(self):
        pass

    @abstractmethod
    def _get_defence(self):
        pass

class Mage(Unit):

    def __init__(self, name, spell_book, defence):
        if not isinstance(spell_book, Spell_book):
            raise Exception
        self._name = name
        self._dmg = spell_book
        self._defence = defence


    def _get_dmg(self):
        return self._dmg.get_random_spell()

    def _get_defence(self):
        # modify self._defence here
        return self._defence

    def attack(self, enemy):
        if not isinstance(enemy, Unit):
            raise Exception("it's not a unit")  # todo: do informative exception !
        if not enemy.is_alive:
            return
        _dmg = self._get_dmg()
        _defence = enemy._get_defence()

        enemy._health += (_defence - _dmg * self.damage_multiplier) * enemy.miss_multiplier
        enemy.hp_check()

class Knight(Unit):

    def __init__(self, name, dmg, defence):
        self._name = name
        self._dmg = dmg
        self._defence = defence



    def _get_dmg(self):
        # modify self._dmg here
        return self._dmg

    def _get_defence(self):
        # modify self._defence here
        return self._defence

    def attack(self, enemy):
        if not isinstance(enemy, Unit):
            raise Exception("it's not a unit")
        if not enemy.is_alive:
            return
        _dmg = self._get_dmg()
        _defence = enemy._get_defence()

        enemy._health += ((_defence / 2) - _dmg * self.damage_multiplier) * enemy.miss_multiplier
        enemy.hp_check()

class Stuff:
    list_of_users = []

    def __init__(self, health, dmg, defence):
        self._health = health
        self._dmg = dmg
        self._defence = defence

class Spell_book(Stuff):
    list_of_users = [Mage]
    dict_of_spells = {
        'fireball': 10,
        'frozen arrow': 5,
        'lightning bolt': 7,
    }

    def get_random_spell(self):
        name, damage = random.choice(list(self.dict_of_spells.items()))
        return float(damage)