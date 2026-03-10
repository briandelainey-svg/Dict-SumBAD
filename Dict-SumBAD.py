#imports
import pickle
from pathlib import Path

#Dictionary
items = {
    'Weapon' : {},
    'Spell' : {},
    'Artifact' : {}
    }

#Functions
def item(items):#a list of all items
    print('-' * 10)#start of list
    
    spell = list(items['Spell'].keys())#makes a list of all spell names
    artifact = list(items['Artifact'].keys())#makes a list of all artifact names
    weapon = list(items['Weapon'].keys())#makes a list of all weapon names
    
    index = 0#prints all weapons
    print('Weapons:')
    while index < (len(weapon) / 2):
        print('    ', items['Weapon'])
        index += 1
        
    index = 0#prints all spells
    print('Spell:')
    while index < (len(spell) / 2):
        print('    ', items['Spell'])
        index += 1
        
    index = 0#prints all artifacts
    print('Artifact:')
    while index < (len(artifact)):
        print('    ', items['Artifact'])
        index += 1
        
    print('-' * 10)#end of list
        
def new_item(items):#function for making new items
    category = input('''Item Category?
Weapon
Spell
Artifact
>>> ''')#item category
    name = input('''What is your items name?
>>> ''')#items name
    if category == 'Weapon' or category == 'Spell':#checks if item needs damage
        damage = input('''How much damage does it do?
>>> ''')#how much damage item does
    price = input('''How much does it cost?
>>> ''')#items price
    
    items[category][name] = {}#adds item to dictionary
    if category == 'Weapon' or category == 'Spell':
        items[category][name]['Damage'] = damage
    items[category][name]['Value'] = price

#Main
data = Path('data.pkl')#defines file path
if data.exists() and data.stat().st_size > 0:#checks if file already exists
    with open(data, 'rb') as pickle_file:#grabs all items from data.pkl
        items = pickle.load(pickle_file)
else:
    with open('data.pkl', 'wb') as pickle_file:#creates data.pkl if it doesnt exist
        pickle.dump(items, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    
while True:
    if not items['Weapon'] and not items['Spell'] and not items['Artifact']:#checks if there are any items
        new_item(items)
    else:#if there are items, you can create or remove one
        item(items)
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
        elif choice == '2':
            category = input('''Item Category?
Weapon
Spell
Artifact
>>> ''')
            choice = input('''What Item do you need to remove?
>>> ''')
            del items[category][choice]
            
choice = input('''Do you want to save these items?
1. Yes
2. No
>>> ''')

#Save
if choice == '1':
    if data.exists():
        with open('data.pkl', 'wb') as pickle_file:
            pickle.dump(items, pickle_file)