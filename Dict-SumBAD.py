#Imports
import pickle

#Functions
def item(items):
    print('-' * 10)
    index = 0
    weapon = list(items['Weapon'].keys())
    spell = list(items['Spell'].keys())
    artifact = list(items['Artifact'].keys())
    while index < items['Weapon']:
        print(items['Weapon'] )
          
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
    items[category]['Name'] = name
    if category == 'Weapon' or category == 'Spell':
        items[category]['Damage'] = damage
    items[category]['Value'] = price

#Dictionary
items = {
    'Weapon' : {},
    'Spell' : {},
    'Artifact' : {}
    }

#Main
while True:
    
    if not items:
        new_item(items)
    elif items:
        choice = input('''Are you done?
1. Yes
2. No
>>> ''')
        if choice =='1':
            break
        choice = input('''What would you like to do?
1. Create a new item
2. Delete an item
>>> ''')
        if choice == '1':
            new_item(items)
        item(items)
#Save
        
