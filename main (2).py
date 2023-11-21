import random


def Spiel():

    Numer_Spieler = input("Geben sie eine Nummer zwischen 1 und 20 ein: ")

    Nummer_PC = random.randint(1,2)

    if Nummer_PC == Numer_Spieler:

        print("Der Pc hat gewonnen")



    else:

        print("Der Spieler hat gewonnen")



Spiel()