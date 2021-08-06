#cite:
# https://github.com/salaheldinaz/RPG-Battle-Script/blob/master/classes/game.py

import os
from classes.game import Person, bcolors


os.chdir('C:\\1.Research Files\\Github\\RPG')

magic = [{'name': 'Fire', 'cost': 10, 'dmg': 100},
         {'name': 'Thunder', 'cost': 10, 'dmg': 124},
         {'name': 'Blizzard', 'cost': 10, 'dmg': 100}]

magic[1] ['name']
magic[1] ['dmg']
magic[1] ['cost']

player = Person(460, 65, 60, 34, magic)

print(player.generate_damage())
print(player.generate_spell_damage(0)) #it is for Fire
print(player.generate_spell_damage(1)) #it is for Thunder

enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + 'Enemy attacks' + bcolors.ENDC)
while running:
    print('===============================')
    player.choose_magic()
    choice = input('Choose actions:')
    index = int(choice) - 1 #in python indexing starts from 0

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print('You attcked for ', dmg, 'Enemy HP:', enemy.get_hp())
    
    elif index == 1:
        pla
        magic_dmg = player.generate_spell_damage()

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print('Enemy attcked for ', enemy_dmg, 'Your HP:', player.get_hp())
    
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN+ 'You win' +bcolors.ENDC)
        running = False
        
    elif player.get_hp() == 0:
        print(bcolors.FAIL+ 'You lost' +bcolors.ENDC)
        running = False

