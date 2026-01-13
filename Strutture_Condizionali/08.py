# Scrivere un Programma Che Calcoli Il Costo Finale Di Un Abbonamento in Palestra In Base a Età, Tipo di Abbonamento e Durata

eta = int(input("Inserisci Età: "))

if eta < 14:
    print("Iscrizione Non Consentita")
    exit()

tipo_abbonamento = input("Inserisci Tipologia Abbonamento (Mensile, Trimestrale, Annuale): ").lower()
durata = int(input("Inserisci il Numero di Mesi: "))

if tipo_abbonamento == "mensile":
    prezzo_mensile_base = 40
elif tipo_abbonamento == "trimestrale":
    prezzo_mensile_base = 35
elif tipo_abbonamento == "annuale":
    prezzo_mensile_base = 25
else:
    print("Tipo Di Abbonamento Non Valido")
    exit()

prezzo_mensile = prezzo_mensile_base
sconto_eta = 0

if 14 <= eta <= 17:
    sconto_eta = 20
elif eta >= 65:
    sconto_eta = 30
else:
    sconto_eta = 0

prezzo_mensile = prezzo_mensile - (prezzo_mensile * (sconto_eta / 100))

totale = prezzo_mensile * durata

sconto_durata = 0
if durata > 6:
    sconto_durata = 10
    totale = totale - (totale * (sconto_durata / 100))

print("\n=== RIEPILOGO ===")
print(f"Età Utente: {eta} Anni")
print(f"Tipo Di Abbonamento: {tipo_abbonamento}")
print(f"Durata: {durata} Mesi")
print(f"\nPrezzo Mensile Base: {prezzo_mensile_base}€")
print(f"Sconto Applicato per Età: {sconto_eta}%")
print(f"Sconto Applicato Per Durata: {sconto_durata}%")
print(f"Prezzo Mensile Finale: {prezzo_mensile}€")
print(f"Costo Totale Da Pagare: {totale}€")

