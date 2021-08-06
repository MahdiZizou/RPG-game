import random

class bcolors:
    HEADER = '\033[33;1;4m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\033[33m'
    TITLE = '\033[1;43m'
    TITLE2 = '\033[1;95m'
    TITLE3 = '\033[1;91m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m' #it ends color
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    TITLE4 = '\033[1;30;42m'


class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk +10
        self.df = df
        self.magic = magic
        self.action = ['Attack', 'Magic'] #it is a static feature not based on inputs

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        mgl = self.magic[i] ['dmg'] - 5
        mgh = self.magic[i]['dmg'] + 5
        return random.randrange(mgl, mgh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]['name']

    def get_spell_mp_cost(self, i):
        return self.magic[i]['cost']

    def choose_action(self):
        i = 1
        print('Actions')
        for item in self.action:
            print(str(i) + ':', item)
            i += 1

    def choose_magic(self):
        i = 1
        print('Magics')
        for spell in self.magic:
            print(str(i) + ':', spell['name'], '(cost:', str(spell['dmg']) + ")")
            i += 1