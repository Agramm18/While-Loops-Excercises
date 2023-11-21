
while True:

    Number = int(input("Geben sie eine Zahl ein: "))
    Number_2 = int(input("Geben sie eine Zweite Zahl ein: "))

    Operator = input("Geben sie Plus, Minus Mal oder geteil ein: ")

    if Operator == "Plus":

        Rechnung = Number + Number_2

    elif Operator == "Minus":

        Rechnung = Number - Number_2

    elif Operator == "Mal":

        Rechnung = Number * Number_2

    elif Operator == "Geteilt":
        Rechnung = Number / Number_2


    Ergebnis = Rechnung

    print(f"Ihr Ergebnis ist {Ergebnis}")

    break