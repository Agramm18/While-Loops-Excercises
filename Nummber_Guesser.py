import random

Spieler_Zahl = int(input("Geben sie eine Zahl ein: "))

Pc_Zahl = random.randint(1, 10)

while True:

    print(Pc_Zahl)

    if Pc_Zahl == Spieler_Zahl:

        print("Der spieler hat gewonnen")
    else:
        print("Der Pc hat gewonnen")



    break