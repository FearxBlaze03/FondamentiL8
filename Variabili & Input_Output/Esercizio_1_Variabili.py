# ESERCIZIO 1:
# CREA UN PROGRAMMA CHE CALCOLI IL PREZZO FINALE DI UN PRODOTTO DOPO L'APPLICAZIONE DI UNO SCONTO PERCENTUALE

# VARIABILI
prezzo = float(input("Inserisci Prezzo: "))
percentuale = int(input("Inserisci Percentuale Di Sconto: "))

# STAMPE
print("=== CALCOLATORE SCONTO ===")
print()

print(f"Prezzo Originale: €{prezzo}")
print(f"Sconto: {percentuale}%")

sconto = (percentuale / 100) * prezzo
finale = prezzo - sconto

print()
print("Risultati")
print("--------------------")
print(f"Prezzo:    €{prezzo}")
print(f"Sconto:    -€{sconto} ({percentuale}%)")
print("--------------------")
print(f"FINALE:     €{finale}")
print()
print(f"Hai Risparmiato €{sconto}!")

