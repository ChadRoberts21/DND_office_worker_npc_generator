import sys
import getopt
import random
from npc import Npc


argumentsHelp = """
*********************************************************
*
*   This app creates a list if 80's office worker npcs
*
*   Options:
*   -g, --gender [any,male,female]: used to be specific about npc gender
*   -c, --count <int>: used to tell the app how many npcs you want
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

def main(argv):
    appGender = 'any'
    appRequiredNPCCount = 1
    try:
        opts, args = getopt.getopt(argv, "hc:g:", ["count=", "gender="])
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
    
    for x in range(0, appRequiredNPCCount):
        localGender = appGender
        if localGender == 'any':
            localGender = random.choice(['male', 'female'])
        npc = Npc(localGender)
        print (npc)
    

if __name__ == "__main__":
    main(sys.argv[1:])
