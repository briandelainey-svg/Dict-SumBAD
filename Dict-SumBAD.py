
#Functions
def item(items):
    print('-' * 10)
    
    spell = list(items['Spell'].keys())
    artifact = list(items['Artifact'].keys())
    weapon = list(items['Weapon'].keys())
    
    index = 0
    print('Weapons:')
    while index < (len(weapon) / 2):
        print('    ', items['Weapon'] )
        index += 1
        
    index = 0
    print('Spell:')
    while index < (len(spell) / 2):
        print('    ', items['Spell'] )
        index += 1
        
    index = 0
    print('Artifact:')
    while index < (len(artifact)):
        print('    ', items['Artifact'] )
        index += 1
        
    print('-' * 10)
        
def new_item(items):
    category = input('''Item Category?
Weapon
Spell
Artifact
>>> ''')
    name = input('''What is your items name?
>>> ''')
    if category == 'Weapon' or category == 'Spell':
        damage = input('''How much damage does it do?
>>> ''')
    price = input('''How much does it cost?
>>> ''')
    items[category][name] = {}
    if category == 'Weapon' or category == 'Spell':
        items[category][name]['Damage'] = damage
    items[category][name]['Value'] = price

#Dictionary
items = {
    'Weapon' : {},
    'Spell' : {},
    'Artifact' : {}
    }

#Main
start = 0
while True:
    if start == 0:
        new_item(items)
        start += 1
    elif start >= 1:
        choice = input('''Are you done?
1. Yes
2. No
>>> ''')
        item(items)
        if choice =='1':
            break
        choice = input('''What would you like to do?
1. Create a new item
2. Delete an item
>>> ''')
        if choice == '1':
            new_item(items)
#Save
        
