# North-west regional encounters
import random

# Lists of creatures on encounter tables

x = ["Human Raiders", "4 Ajdurian Raiders", "3 Ajdurian Raiders", "Hostile Animals", "Hostile Animals",
     "Hostile Animals",
     "Passive Animals", "Passive Animals", "Passive Animals", "Passive Animals", "Passive Animals", "Passive Animals",
     "Passive Animals", "Passive Animals", "Hostile Animals", "Hostile Animals", "Hostile Animals",
     "3 Ajdurian Raiders",
     "4 Ajdurian Raiders", "Ajdurian Raiders"]
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


def oneDsixplustwo():
    return random.randint(3, 8)


def oneDsix():
    return random.randint(1, 6)


def oneDfour():
    return random.randint(1, 4)


def oneDeightpluseight():
    return random.randint(9, 16)


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


# Main Logic

roll_functions = {
    "Human Raiders": Roll_Human_Raiders,
    "Ajdurian Raiders": Roll_Ajdurian_Raiders,
    "Passive Animals": roll_passive_animals,
    "Hostile Animals": roll_hostile_animals,
}

if roll_result in roll_functions:
    roll_function = roll_functions[roll_result]
    result = roll_function()
    if result is not None:
        print(*result)
else:
    print(roll_result)


