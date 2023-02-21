import time
import sys

def foresthex():
    pass

print("Welcome to...")
for i in range(10):
    time.sleep(0.2)
    print("...")
print("Raziel's Scriptorium")

time.sleep(2)

for i in range(4):
    time.sleep(0.2)
    print(".")

username = input("What is your name?\n")
print("\nWelcome "+ username+".", " Here is the list of HexScripts\n")
print("Use the shorthanded name to the right of the colon.")
time.sleep(1)
print("--------------------")
print("North-West Forest Matrix: NWFM")
time.sleep(0.4)
print("North-West Forest Road Matrix: NWFRM")
time.sleep(0.4)
print("Failroads")
time.sleep(0.4)
print("Hallman")
print("--------------------")

newvar = input()

while True:
    if "cum" in newvar or "Cum" in newvar or "penis" in newvar or "Penis" in newvar or "fuck" in newvar or "Fuck" in newvar or "dick" in newvar or "Dick" in newvar or "pussy" in newvar or "Pussy" in newvar:
        print("Die, fucker")
        time.sleep(1)
        sys.exit()
    if newvar == "NWFM":
        foresthex()
    elif newvar == "exit":
        break
    else: print("Invalid, please try again")
    brvar=input()