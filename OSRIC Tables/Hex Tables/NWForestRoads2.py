# North-west regional encounters
import random
import inspect

# Encounter variable lists
u = ["Ajdurian Raiders", "Human Raiders"]

v = ["Merchants", "Mercenaries", "Travellers"]

w = ["Nobleman's Escort", "Grand Wizard's Escort", "Holy Convoy", "Large Soldier/Guard Contingent"]

x = ["Human Raiders", "Human Raiders", "Hostile Animals", "Noble Party", "Hostile Animal(s)", "Guard Patrol",
     "Guard Patrol", "Guard Patrol", "Passive Animal(s)", "Commoner Party", "Commoner Party",
     "Passive Animal(s)", "Commoner Party", "Guard Patrol", "Guard Patrol", "Commoner Party", "Hostile Animal(s)",
     "Noble Party", "Hostile Animal(s)", "Ajdurian Raiders", "Ajdurian Raiders"]

y = ["Fox(es)", "Wolverine(s)", "Squirrel(s)", "Bird(s)", "Bird(s)", "Bird(s)", "Bird(s)", "Squirrel(s)", "Weasel(s)",
     "Passive Wolves"]

z = ["Hungry Wolves", "Giant Rhino Beetle(s)", "Jackal(s)", "Boar(s)", "Lesser Bear(s)", "Giant Bee(s)",
     "Giant Frog(s)"]

# Roll Functions: functions which roll on the main variable matrices

def MainRoll():
    return random.choice(x)

def HostileAnimalRoll():
    return random.choice(z)

def PassiveAnimalRoll():
    return random.choice(y)

def CommonPartyRoll():
    return random.choice(v)

def NoblePartyRoll():
    return random.choice(w)

# Roll Function Variables; variables which store the resulting data from the Roll Functions

MainVar = MainRoll()
HostAnimVar = HostileAnimalRoll()
PassAnimVar = PassiveAnimalRoll()
CommPartyVar = CommonPartyRoll()
NoblePartyVar = NoblePartyRoll()

# Dice and Fixed Value Functions and Variables

def oneDfour():
     return random.randint(1, 4)

def oneDsix():
    return random.randint(1, 6)

def oneDeight():
    return random.randint(1, 8)

def oneDten():
    return random.randint(1, 10)

def oneDtwenty():
    return random.randint(1, 20)


# Encounter detail functions
def CommonerPartyDtl():
    if CommonPartyRoll() == "Merchants":
        return oneDten(), "Merchants", oneDeight(), "Guards"
    elif CommPartyVar == "Mercenaries":
        return random.randint(4, 11), "Guards", oneDfour(), "Leaders"
    elif CommPartyVar == "Travellers":
        return random.randint(2, 5), "Armed Travellers", random.randint(2, 5), "Unarmed Travellers"
    else: return "Error"

def NoblePartyDtl():
    if NoblePartyRoll() == "Nobleman's Escort":
        return random.randint(6, 13), "Guards", oneDfour(), "Nobles"
    elif NoblePartyVar == "Grand Wizard's Escort":
        return random.randint(4, 7), "Guards", random.randint(4, 9), "Magic-Users"
    elif NoblePartyVar == "Holy Convoy":
        return random.randint(3, 8), "Level 3 Clerics", random.randint(2, 5), "Paladins"
    elif NoblePartyVar == "Large Soldier/Guard Contingent":
        return oneDfour(), "Level 2 Leaders", random.randint(2,24), "Guards"
    else: return "Error"

def GuardPatrolDtl():
    return random.randint(2, 6), "Guards"

def HostileAnimalDtl():
    if HostileAnimalRoll() == "Hungry Wolves":
        return oneDfour(), "Hungry Wolves"
    elif HostAnimVar == "Giant Rhino Beetle(s)":
        return oneDten(), "Giant Rhino Beetle(s)"
    elif HostAnimVar == "Boar(s)":
        return oneDsix(), "Boar(s)"
    elif HostAnimVar == "Jackal(s)":
        return oneDten(), "Jackal(s)"
    elif HostAnimVar == "Lesser Bear(s)":
        return oneDsix(), "Lesser Bear(s)"
    elif HostAnimVar == "Giant Bee(s)":
            return oneDtwenty(), "Giant Bee(s)"
    elif HostAnimVar == "Giant Frog(s)":
        return oneDtwenty(), "Giant Frog(s)"
    else:
        return "Error"

def PassiveAnimalDtl():
    if PassiveAnimalRoll() == "Fox(es)":
        return oneDfour(), "Fox(es)"
    elif PassAnimVar == "Squirrel(s)":
        return oneDten(), "Squirrel(s)"
    elif PassAnimVar == "Weasel(s)":
        return oneDsix(), "Weasel(s)"
    elif PassAnimVar == "Passive Wolves":
        return oneDten(), "Passive Wolves"
    elif PassAnimVar == "Wolverine(s)":
        return oneDsix(), "Wolverine(s)"
    elif PassAnimVar == "Bird(s)":
        return oneDtwenty(), "Bird(s)"
    else:
        return "Error"

def RaiderDtl():
    if MainRoll() == "Ajdurian Raiders" or "Human Raiders":
        return random.choice(u), random.randint(1, 2)
    else:
        return "Error"

# Primary Logic

EncounterMatrix = {
"Human Raiders": RaiderDtl(),
"Ajdurian Raiders": RaiderDtl(),
"Guard Patrols": GuardPatrolDtl(),
"Passive Animal(s)": PassiveAnimalDtl(),
"Hostile Animal(s)": HostileAnimalDtl(),
"Commoner Party": CommonerPartyDtl(),
"Noble Party": NoblePartyDtl(),
}


#Final

encounter_type, encounter_details = random.choice(list(EncounterMatrix.items()))

print(f"Encounter Type: {encounter_type}")
print(f"Details: {encounter_details}")










