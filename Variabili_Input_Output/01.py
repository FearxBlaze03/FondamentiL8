# Crea un Programma che Calcoli il Prezzo Finale di un Prodotto dopo l'applicazione
# Di uno sconto percentuale

prezzo = float(input("Inserisci Prezzo: "))
sconto = int(input("Inserisci Sconto: "))

sconto_euro = prezzo * (sconto / 100)


print("\n=== CALCOLATORE SCONTO ===")
print(f"Prezzo Originale: {prezzo:.2f}€")
print(f"Sconto: {sconto}%\n")

print("=== RISULTATI ===")
print("===================")
print(f"Prezzo: {prezzo:.2f}€")
print(f"Sconto: -€{sconto_euro:.2f} ({sconto}%)")
print("===================")
print(f"Finale: €{prezzo-sconto_euro:.2f}")



