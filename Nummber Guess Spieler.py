import random

Nummer_PC = random.randint(1.20)

Nummer_Spieler = input("An welche Nummer denkt der PC?: ")

if Nummer_Spieler == Nummer_PC:
    print("Der Spieler hat gewonnen")

else:
    print("Der PC hat gewonne")