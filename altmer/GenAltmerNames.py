import random

def genName(gender):
    prefix = ''
    suffix = ''

    if gender == 'f':
        femalePrefixes = ['Andra', 'Ca', 'Cymba', 'Kori', 'Lili', 'Lora', 'Mor', 'Psy', 'Saur', 'Sha', 'Valli', 'Zeno']
        femaleSuffixes = ['ginia', 'lia', 'lina', 'mia', 'na', 'sara', 'sephona', 'sha', 'tha']

        prefix = random.choice(femalePrefixes)
        suffix = random.choice(femaleSuffixes)
    elif gender == 'm':
        malePrefixes = ['Core', 'Corri', 'Cyre', 'Gan', 'Kala', 'Kelkemme', 'Liliand', 'Lovi', 'Mith', 'Saru', 'Soli']
        maleSuffixes = ['dalf', 'las', 'lian', 'llon', 'man', 'mon', 'nar', 'ra', 'rili', 'ril', 'ron', 'tar']

        prefix = random.choice(malePrefixes)
        suffix = random.choice(maleSuffixes)

    return prefix + suffix

gender = input('Is your character male or female? (m/f): ')
if gender == 'm' or gender == 'f':
    print(genName(gender))
else:
    gender = input('Is your character male or female? (m/f): ')


