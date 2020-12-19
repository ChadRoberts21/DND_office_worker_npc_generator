from names import firstNames, lastNames, jobTitles
from dndExtras import RaceGenerator, races, alignments
import random

class Npc:
    def __init__(self, gender):
        self.firstName = random.choice(firstNames[gender])
        self.lastName = None
        if random.randint(1,100) > 90:
            self.lastName = random.choice(lastNames['rare'])
        else:
            self.lastName = random.choice(lastNames['common'])

        self.gender = gender
        self.jobTitle = random.choice(jobTitles)

        raceAttributes = RaceGenerator(races, alignments).new()
        self.age = raceAttributes['age']
        self.height = raceAttributes['height']
        self.weight = raceAttributes['weight']
        self.race = raceAttributes['race']
        self.alignment = raceAttributes['alignment']

    def __str__(self):
        return f'Name: {self.firstName} {self.lastName}, Gender: {self.gender}, Race: {self.race}, Age: {self.age}, Height: {self.height}, Weight: {self.weight}, Alignment: {self.alignment}, Job: {self.jobTitle}'
    
    def __repr__(self):
        return self.__str__()