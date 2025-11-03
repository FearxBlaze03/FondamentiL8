# # CREA UN PROGRAMMA CHE CALCOLA SE IL NUMERO E' PARI O DISPARI
#
# # VARIABILE DATA DALL'UTENTE
# N = int(input("Inserisci Numero: "))
#
# # CONDIZIONE CHE VERIFICA SE IL NUMERO E' PARI O DISPARI
#
# if N % 2 == 0:
#     print("Il Numero è Pari!")
# else:
#     print("Il Numero è Dispari")


# CREA UN PROGRAMMA CHE CALCOLA LO SCONTO APPLICABILE A UN CLIENTE IN BASE ALLA SUA ETA' E ALL'IMPORTO TOTALE DELL'ACQUISTO

eta = int(input("Inserisci Età: "))
spesa = float(input("Inserisci Spesa: "))

if eta < 18:
    sconto = 0

elif eta <= 60:
    if spesa > 100:
        sconto = 10
    else:
        sconto = 5
else:
    sconto = 15

print(f"Lo Sconto è di: {sconto}%")