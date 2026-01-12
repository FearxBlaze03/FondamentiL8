# Scrivere un Programma Che Calcoli il Prezzo Del Biglietto Per un Parco Divertimenti in Base a Età
# Tipo di Biglietto e Numero di Ingressi

eta = int(input("Inserisci Età: "))

tipo_biglietto = input("Inserisci Tipologia Biglietto (Standard, Vip o Familiare): ").lower()
numero_ingressi = int(input("Inserisci Il Numero Di Biglietti: "))

if tipo_biglietto == "standard":
    prezzo_biglietto = 20
elif tipo_biglietto == "vip":
    prezzo_biglietto = 50
elif tipo_biglietto == "familiare":
    prezzo_biglietto = 35
else:
    print("Tipo Di Biglietto non Valido")
    exit()

sconto_eta = 0
if eta < 5:
    prezzo_biglietto = 0
    sconto_eta = 0
    print("L'Ingresso è Gratuito!")

elif 5 <= eta <= 12 and (tipo_biglietto == "standard" or tipo_biglietto == "familiare"):
    sconto_eta = 50
    prezzo_biglietto = prezzo_biglietto - (prezzo_biglietto * (sconto_eta / 100))

elif eta >= 60 and (tipo_biglietto == "standard" or tipo_biglietto == "familiare"):
    sconto_eta = 30
    prezzo_biglietto = prezzo_biglietto - (prezzo_biglietto * (sconto_eta / 100))

totale = prezzo_biglietto * numero_ingressi

sconto_ingressi = 0

if numero_ingressi > 4:
    sconto_ingressi = 10
    totale = totale - (totale * (sconto_ingressi / 100))

print(f"\nPrezzo Per Biglietto: {prezzo_biglietto}")
print(f"Sconto Applicato per Età: {sconto_eta}%")
print(f"Sconto Applicato per Quantità: {sconto_ingressi}%")
print(f"Totale Da Pagare: {totale}€")




