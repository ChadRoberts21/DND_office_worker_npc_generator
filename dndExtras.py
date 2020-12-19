import random
from range import Range

races = {
    'Dragonborn': {
        'height': Range(150, 220, 'cm'),
        'weight': Range(80, 140, 'kg'),
        'age': Range(15, 80, 'years'),
        'commonalityValue': 10
    },
    'Dwarf': {
        'height': Range(120, 155, 'cm'),
        'weight': Range(55, 80, 'kg'),
        'age': Range(45, 250, 'years'),
        'commonalityValue': 200
    },
    'Elf': {
        'height': Range(150, 200, 'cm'),
        'weight': Range(45, 75 ,'kg'),
        'age': Range(100, 600, 'years'),
        'commonalityValue': 250
    },
    'Gnome': {
        'height': Range(80, 130, 'cm'),
        'weight': Range(10, 30, 'kg'),
        'age': Range(35, 320, 'years'),
        'commonalityValue': 110
    },
    'Half-Elf' : {
        'height': Range(150, 190, 'cm'),
        'weight': Range(55, 120, 'kg'),
        'age': Range(20, 140, 'years'),
        'commonalityValue': 80
    },
    'Halfling': {
        'height': Range(80, 120, 'cm'),
        'weight': Range(10, 30, 'kg'),
        'age': Range(20, 170, 'years'),
        'commonalityValue': 150
    },
    'Half-Orc': {
        'height': Range(150, 200, 'cm'),
        'weight': Range(80, 140, 'kg'),
        'age': Range(15, 55, 'years'),
        'commonalityValue': 50
    },
    'Human': {
        'height': Range(150, 200, 'cm'),
        'weight': Range(55, 115, 'kg'),
        'age': Range(20, 60, 'years'),
        'commonalityValue': 1000
    },
    'Tiefling': {
        'height': Range(150, 200, 'cm'),
        'weight': Range(55, 115, 'kg'),
        'age': Range(20, 80, 'years'),
        'commonalityValue': 5
    },
}

alignments = {
    'type': ['Lawful', 'Chaotic', 'Neutral'],
    'morals': ['Good', 'Evil', 'Neutral']
} 

class RaceGenerator:
    def __init__(self, races, alignments):
        self.totalCommonalityValue = 0
        for raceDetails in races.values():
            self.totalCommonalityValue += raceDetails['commonalityValue']

        self.races = races
        self.alignments = alignments

    def new(self):
        randNumber = random.randint(1, self.totalCommonalityValue)
        minIncrementor = 0
        selectedRace = None
        for raceName, raceDetails in races.items():
            maxIncrementor = minIncrementor + raceDetails['commonalityValue']
            if randNumber > minIncrementor and randNumber <= maxIncrementor:
                # return details.
                selectedRace = raceName
                break
            else:
                minIncrementor = maxIncrementor
        
        alignmentTypes = self.alignments['type']
        alignmentMorals = self.alignments['morals']
        alignment = f'{random.choice(alignmentTypes)} {random.choice(alignmentMorals)}' 

        # use selected race to generate Npc paramters based on there race
        return {
            'race' : selectedRace,
            'height': self.races[selectedRace]['height'].randomValue(),
            'weight': self.races[selectedRace]['weight'].randomValue(),
            'age': self.races[selectedRace]['age'].randomValue(),
            'alignment': alignment,
        }

