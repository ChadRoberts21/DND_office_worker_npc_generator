import sys
import getopt
import random
import csv
from npc import Npc


argumentsHelp = """
*********************************************************
*
*   This app creates a list if 80's office worker npcs
*
*   Options:
*   -g, --gender [any,male,female]: used to be specific about npc gender
*   -c, --count <int>: used to tell the app how many npcs you want
*   -o, --output: flag to output as a csv file
*   -f, --fileName <string>: file name to use for export file
*
"""

validGenders = ['any', 'male', 'female']

def try_parse_int(s, base=10, val=None):
  try:
    return int(s, base)
  except ValueError:
    return val

def validateGender(value):
    if value.lower() not in validGenders:
        raise ValueError(f'{value}, is not a valid gender for this app')

def makeCSV(npcs, fileName = 'npcs.csv'):
    fieldnames = vars(npcs[0]).keys()
    with open(fileName, 'w', newline='') as npcFile:
        writer = csv.DictWriter(npcFile, fieldnames=fieldnames)
        writer.writeheader()
        for npc in npcs:
            writer.writerow(vars(npc))

def printToTerminal(npcs):
    for npc in npcs:
        print(npc)

def main(argv):
    appGender = 'any'
    appRequiredNPCCount = 1
    export = False
    exportFileName = None
    try:
        opts, args = getopt.getopt(argv, "hoc:g:f:", ["count=", "gender=", 'output', 'fileName='])
    except getopt.GetoptError:
        print(argumentsHelp)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print()
            sys.exit()
        elif opt in ("-c", "--count"):
            if arg:
                appRequiredNPCCount = try_parse_int(arg, val= 1)
        elif opt in ("-g", "--gender"):
            try:
                validateGender(arg)
                if arg: 
                    appGender = arg.lower()
            except:
                appGender = 'any'
        
        if opt in ('-o', '-output'):
            export = True
        
        if opt in ('-f', '--fileName'):
            exportFileName = arg
    
    npcs = []
    for x in range(0, appRequiredNPCCount):
        localGender = appGender
        if localGender == 'any':
            localGender = random.choice(['male', 'female'])
        npcs.append(Npc(localGender))
    
    if(export):
        if(exportFileName):
            makeCSV(npcs, exportFileName)
        else:
            makeCSV(npcs)
    else:
        printToTerminal(npcs)
    

if __name__ == "__main__":
    main(sys.argv[1:])
