def kilosToPounds(value):
    return value/0.45359237

def poundsToKilos(value):
    return value/2.2046226218

def cmToInches(value):
    return value/2.54

def cmToFeet(value):
    inInches = cmToInches(value)
    feet = int(inInches/12)
    remainder = inInches%12
    return f'{feet}\'{remainder}"'