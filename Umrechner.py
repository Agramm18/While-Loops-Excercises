

while True:

    Zahl1 = float(input("Geben sie eine Zahl ein: "))

    Umrechner1 = input("Geben sie eine Einheit ein: ")
    Umrechner2 = input("Geben sie eine einheit ein: ")


#mm in

    if Umrechner1 == "mm" and Umrechner2 == "cm":
        Ergebnis = Zahl1 * 10
        print(Ergebnis)

    elif Umrechner1 == "mm" and Umrechner2 == "dm":
        Ergebnis = Zahl1 / 100
        print(Ergebnis)

    elif Umrechner1 == "mm" and Umrechner2 == "m":
        Ergebnis = Zahl1 / 100
        print(Ergebnis)

    elif Umrechner1 == "mm" and Umrechner2 == "km":
        Ergebnis = Zahl1 / 1000 * 1000
        print(Ergebnis)

#mm in

#cm in

    elif Umrechner1 == "cm" and Umrechner2 == "mm":
        Ergebnis = Zahl1 / 10
        print(Ergebnis)

    elif Umrechner1 == "cm" and Umrechner2 == "dm":
        Ergebnis = Zahl1 * 10
        print(Ergebnis)

    elif Umrechner1 == "cm" and Umrechner2 == "m":
        Ergebnis = Zahl1 / 100
        print(Ergebnis)

    elif Umrechner1 == "cm" and Umrechner2 == "km":
        Ergebnis = Zahl1 / 100 * 1000
        print(Ergebnis)


#cm in


#dm in

    elif Umrechner1 == "dm" and Umrechner2 == "mm":
        Ergebnis = Zahl1 * 10
        print(Ergebnis)

    elif Umrechner1 == "dm" and Umrechner2 == "cm":
        Ergebnis = Zahl1 / 10
        print(Ergebnis)

    elif Umrechner1 == "dm" and Umrechner2 == "m":
        Ergebnis = Zahl1 / 10
        print(Ergebnis)

    elif Umrechner1 == "dm" and Umrechner2 == "km":
        Ergebnis = Zahl1 / 10 * 100
        print(Ergebnis)

#dm in


#m in

    elif Umrechner1 == "m" and Umrechner2 == "mm":
        Ergebnis = Zahl1 * 1000
        print(Ergebnis)

    elif Umrechner1 == "m" and Umrechner2 == "cm":
        Ergebnis = Zahl1 * 100
        print(Ergebnis)

    elif Umrechner1 == "m" and Umrechner2 == "dm":
        Ergebnis = Zahl1 * 100
        print(Ergebnis)

    elif Umrechner1 == "m" and Umrechner2 == "km":
        Ergebnis = Zahl1 / 1000
        print(Ergebnis)

    elif Umrechner1 == "m" and Umrechner2 == "seemeile":
        Ergebnis = Zahl1 / 1852
        print(Ergebnis)


#m in

    elif Umrechner1 == "km" and Umrechner2 == "mm":
        Ergebnis = Zahl1 / 1000000
        print(Ergebnis)

    elif Umrechner1 == "km" and Umrechner2 == "cm":
        Ergebnis = Zahl1 / 100000
        print(Ergebnis)

    elif Umrechner1 == "km" and Umrechner2 == "dm":
        Ergebnis = Zahl1 / 10000
        print(Ergebnis)

    elif Umrechner1 == "km" and Umrechner2 == "m":
        Ergebnis = Zahl1 * 1000
        print(Ergebnis)

    elif Umrechner1 == "km" and Umrechner2 == "seemeile":
        Ergebnis = Zahl1 / 1,852
        print(Ergebnis)

#km in

#seemeile in

    elif Umrechner1 == "seemeile" and Umrechner2 == "m":
        Ergebnis = Zahl1 * 1852
        print(Ergebnis)

    elif Umrechner1 == "seemeile" and Umrechner2 == "km":
        Ergebnis = Zahl1 * 1,852
        print(Ergebnis)


# seemeile in


#Währung


    elif Umrechner1 == "Euro" and Umrechner2 == "Pfund":
        Ergebnis = Zahl1 * 0,87
        print(Ergebnis)

    elif Umrechner1 == "Euro" and Umrechner2 == "Dollar":
        Ergebnis = Zahl1 * 1.07
        print(Ergebnis)

    elif Umrechner1 == "Euro" and Umrechner2 == "Yen":
        Ergebnis = Zahl1 * 162.16
        print(Ergebnis)

    elif Umrechner1 == "Pfund" and Umrechner2 == "Euro":
        Ergebnis = Zahl1 / 0.87
        print(Ergebnis)

    elif Umrechner1 == "Dollar" and Umrechner2 == "Euro":
        Ergebnis = Zahl1 / 1.07
        print(Ergebnis)

    elif Umrechner1 == "Yen" and Umrechner2 == "Euro":
        Ergebnis = Zahl1 / 162.16
        print(Ergebnis)



    if Zahl1 or Umrechner1 or Umrechner2 == "Ende":
        break

    else:
        continue