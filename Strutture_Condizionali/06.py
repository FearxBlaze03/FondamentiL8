# Scrivere un Programma che Gestisce La Prenotazione Dei Biglietti Per un Cinema

# Richiesta Dell' Età Dell' Cliente
eta = int(input("Inserisci L'Età Del Cliente: "))

# Se il Cliente ha Meno di 6 Anni, L'Acquisto non può essere effettuato
if eta < 6:
    print("Non Puoi Acquistare Biglietti")
    exit()

tipologia_film = input("Inserisci Tipologia Film (Normale, 3D, IMAX): ").lower()
numero_biglietti = int(input("Inserisci Il Numero Di Biglietti da Acquistare: "))

if tipologia_film == "normale":
    prezzo_biglietto = 8
elif tipologia_film == "3d":
    prezzo_biglietto = 12
elif tipologia_film == "imax":
    prezzo_biglietto = 15
else:
    print("Tipologia Film Non Valida")
    exit()


if 6 <= eta <= 12 and (tipologia_film == "3d" or tipologia_film == "imax"):
    prezzo_biglietto /= 2 # Metà Prezzo Per i Film 3D e IMAX per i bambini dai 6 ai 12 anni

totale = prezzo_biglietto * numero_biglietti
sconto = 0

if numero_biglietti > 5:
    sconto = 10
    totale = totale - (totale * (sconto / 100))

print(f"\nPrezzo Per Biglietto: {prezzo_biglietto}€")
print(f"Sconto Applicato: {sconto}%")
print(f"Prezzo Da Pagare: {totale}€")







