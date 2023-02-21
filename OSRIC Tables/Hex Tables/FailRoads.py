# North-west regional encounters
import random

# Lists of creatures on encounter tables
v = ["Merchants", "Mercenaries", "Travellers"]
v_merchparty = ["Merchants", "Guards"]
v_mercparty = ["Guards", "Leaders"]
v_travelparty = ["Unarmed", "Armed"]

w = ["Nobleman's Escort", "Grand Wizard's Escort", "Holy Convoy", "Large Soldier/Guard Contingent"]
w_noble = ["Guards", "Nobles"]
w_wizard = ["Guards", "Magic-Users", "Grand Wizard"]
w_holyconvoy = ["Level 3 Clerics", "Level 2 Paladins"]
w_soldierconting = ["Level 2 Leaders", "Soldiers"]

x = ["Human Raiders", "Human Raiders", "Hostile Animals", "Noble Party", "Hostile Animal(s)", "Guard Patrol",
     "Guard Patrol", "Guard Patrol", "Passive Animal(s)", "Commoner Party", "Commoner Party",
     "Passive Animal(s)", "Commoner Party", "Guard Patrol", "Guard Patrol", "Commoner Party", "Hostile Animal(s)",
     "Noble Party", "Hostile Animal(s)", "Ajdurian Raiders", "Ajdurian Raiders"]

y = ["Fox(es)", "Wolverine(s)", "Squirrel(s)", "Bird(s)", "Bird(s)", "Bird(s)", "Bird(s)", "Squirrel(s)", "Weasel(s)",
     "Passive Wolves"]

z = ["Hungry Wolves", "Giant Rhino Beetle(s)", "Jackal(s)", "Boar(s)", "Lesser Bear(s)", "Giant Bee(s)",
     "Giant Frog(s)"]


# Dice Functions and Smaller Variables

def main_roll():
    return random.choice(x)


def secondary_roll():
    return random.choice(y)


def tertiary_roll():
    return random.choice(z)

def roll_four():
    return random.choice(v)



def oneDsixplustwo():
    return random.randint(3, 8)


def oneDsix():
    return random.randint(1, 6)


def oneDfour():
    return random.randint(1, 4)


def oneDeightpluseight():
    return random.randint(9, 16)

def oneDeight():
    return random.randint(1, 8)


def oneDeightplusthree():
    return random.randint(3, 11)


def oneDten():
    return random.randint(1, 10)


def oneDtwenty():
    return random.randint(1, 20)


def oneDtwo():
    return random.randint(1, 2)


def threeDten():
    return random.randint(3, 30)


def Roll_Human_Raiders():
    return oneDsixplustwo(), "Human Raiders"


def Roll_Ajdurian_Raiders():
    return oneDsixplustwo(), "Ajdurian Raiders"




    # Main Variables

roll_result = main_roll()
roll_result2 = secondary_roll()
roll_result3 = tertiary_roll()
roll_results4 = roll_four()


# Roll Functions

def roll_passive_animals():
    if roll_result2 == "Fox(es)":
        return oneDfour(), "Fox(es)"
    elif roll_result2 == "Squirrel(s)":
        return oneDten(), "Squirrel(s)"
    elif roll_result2 == "Weasel(s)":
        return oneDsix(), "Weasel(s)"
    elif roll_result2 == "Passive Wolves":
        return oneDten(), "Passive Wolves"
    elif roll_result2 == "Wolverine(s)":
        return oneDsix(), "Wolverine(s)"
    elif roll_result2 == "Bird(s)":
        return oneDtwenty(), "Bird(s)"
    else:
        return None


def roll_hostile_animals():
    if roll_result3 == "Hungry Wolves":
        return oneDfour(), "Hungry Wolves"

    elif roll_result3 == "Giant Rhino Beetle(s)":
        return oneDten(), "Giant Rhino Beetle(s)"

    elif roll_result3 == "Boar(s)":
        return oneDsix(), "Boar(s)"

    elif roll_result3 == "Jackal(s)":
        return oneDten(), "Jackal(s)"

    elif roll_result3 == "Lesser Bear(s)":
        return oneDsix(), "Lesser Bear(s)"

    elif roll_result3 == "Giant Bee(s)":
        return oneDtwenty(), "Giant Bee(s)"

    elif roll_result3 == "Giant Frog(s)":
        return oneDtwenty(), "Giant Frog(s)"

    else:
        return None


def roll_commoner_party():
    if roll_result == "Commoner Party":
        return roll_results4
    if roll_results4 == "Merchants":
        return oneDten(), v_merchparty[0], oneDeight(), v_merchparty[1]
    if roll_results4 == "Mercenaries":
        return oneDeightplusthree(), v_mercparty[0], oneDfour(), v_mercparty[1]
    if roll_results4 == "Travellers":
        return oneDfour()+1, v_travelparty[0], oneDfour()+1, v_travelparty[1]







    # Main Logic

roll_functions = {
    "Human Raiders": Roll_Human_Raiders,
    "Ajdurian Raiders": Roll_Ajdurian_Raiders,
    "Passive Animals": roll_passive_animals,
    "Hostile Animals": roll_hostile_animals,
    "Commoner Party": roll_commoner_party,
}

if roll_result in roll_functions:
    roll_function = roll_functions[roll_result]
    result = roll_function()
    if result is not None:
        print(*result)
else:
    print(roll_result)