import random


Zahl_PC = random.randint(1,10)

Zahl_User = int(input("Gib eine Zahl zwischen 1 und 10 ein: "))

while True:

    if Zahl_User == Zahl_PC:
        print("Sie haben gewonnen")
        break

    else:
        print("Das war leider falsch")
        continue

    break