# Unendliche Schleife für fortlaufende Berechnungen
while True:
    
    # Festlegung der Zinssätze für private und geschäftliche Überziehungen
    Privat = 5
    Buissness = 9

    # Basiszins, der zu jedem Zinssatz addiert wird
    Basiszins = 3.12

    # Berechnung der effektiven Zinssätze für private und geschäftliche Überziehungen
    Zins_Privat = Privat + Basiszins
    Zins_Buissness = Buissness + Basiszins

    # Definition der Tage in einem Monat und einem Jahr für die Zinsberechnung
    Monat = 30
    Jahr = 360

    # Eingabe der Art der Verwendung (privat oder geschäftlich) und des überzogenen Betrags
    Anwendung = input("Sind Sie privat oder geschäftlich unterwegs: ")
    Überzogen = float(input("Wie hoch ist der überzogene Betrag: "))

    # Eingabe der Anzahl der überzogenen Tage
    Überzugs_Dauer_in_Tagen = int(input("Wie viele Tage haben Sie überzogen: "))

    # Festlegung des Zinssatzes entsprechend der Art der Verwendung
    if Anwendung == "privat":
        Zinssatz = Zins_Privat
    elif Anwendung == "geschäftlich":
        Zinssatz = Zins_Buissness

    # Berechnung der Überziehungszinsen für private und geschäftliche Überziehungen
    Rechnung_Privat = (Überzogen * Zins_Privat * Überzugs_Dauer_in_Tagen) / (Jahr * 100)
    Rechnung_Buissness = (Überzogen * Zins_Buissness * Überzugs_Dauer_in_Tagen) / (Jahr * 100)

    # Runden der Ergebnisse auf zwei Dezimalstellen
    Ergebnis_Privat = round(Rechnung_Privat, 2)
    Ergebnis_Buissness = round(Rechnung_Buissness, 2)

    # Ausgabe der Überziehungszinsen entsprechend der Art der Verwendung
    if Anwendung == "privat":
        print(f"Sie müssen {Ergebnis_Privat} an Überziehungszinsen zahlen")
    elif Anwendung == "geschäftlich":
        print(f"Sie müssen {Ergebnis_Buissness} an Überziehungszinsen zahlen")

    # Beenden der Schleife
    break