# Scrivere un Programma in Python Che Simuli la Gestione Di Un Cliente in Un Negozio

eta = int(input("Inserisci L'Età Del Cliente: "))

if eta < 16:
    print("Accesso Negato")
    exit()

tipologia_cliente = input("Inserisci Tipologia Cliente: ").lower()

if tipologia_cliente != "standard" and tipologia_cliente != "premium":
    print("Tipo Di Cliente Non Valido")
    exit()

totale_spesa = int(input("Inserisci Totale Spesa: "))

sconto = 0

if tipologia_cliente == "standard":
    if totale_spesa < 50:
        sconto = 0
        print(f"\nSconto: {sconto}%")
        print(f"Prezzo Finale: {totale_spesa}")

    elif totale_spesa >= 50 and totale_spesa <= 99.99:
        sconto = 5
        totale_spesa = totale_spesa - (totale_spesa * (sconto / 100))

        print(f"\nSconto: {sconto}%")
        print(f"Prezzo Finale: {totale_spesa}")


    elif totale_spesa >= 100:
        sconto = 10
        totale_spesa = totale_spesa - (totale_spesa * (sconto / 100))

        print(f"\nSconto: {sconto}%")
        print(f"Prezzo Finale: {totale_spesa}")


if tipologia_cliente == "premium":
    if totale_spesa < 50:
        sconto = 10
        totale_spesa = totale_spesa - (totale_spesa * (sconto / 100))

        print(f"\nSconto: {sconto}%")
        print(f"Prezzo Finale: {totale_spesa}")

    elif totale_spesa >= 50 and totale_spesa <= 99.99:
            sconto = 15
            totale_spesa = totale_spesa - (totale_spesa * (sconto / 100))

            print(f"\nSconto: {sconto}%")
            print(f"Prezzo Finale: {totale_spesa}")

    elif totale_spesa >= 100:
            sconto = 20
            totale_spesa = totale_spesa - (totale_spesa * (sconto / 100))

            print(f"\nSconto: {sconto}%")
            print(f"Prezzo Finale: {totale_spesa}")




