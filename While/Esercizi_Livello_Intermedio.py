# Chiedi all'utente di Inserire un numero intero e usa un ciclo While per verificare se è un numero primo
# (divisibile solo per 1 e per sè stesso). Se non è primo, chiedi un altro numero finché non ne inserisce uno che lo è

"""numero = int(input("Inserisci Numero: "))

while True:
    if numero < 2:
        primo = False
    else:
        primo = True
        i = 2
        while i * i <= numero:
            if numero % i == 0:
                primo = False
                break
            i += 1
    if primo:
        break
    print("Numero Non Primo. Riprova")
    numero = int(input("Inserisci Numero: "))

print(f"Hai Inserito un Numero Primo: {numero}")"""

# ====================================================

# Chiedi all'utente di inserire una parola e continua a richiederla finché la parola inserita non ha esattamente 8 caratteri. Quando l'utente inserisce una parola di 8 lettere, il programma termina e mostra un
# messaggio di conferma.

"""parola = input("Inserisci Una Parola di 8 Lettere: ")

while len(parola) != 8:
    print("La Parola Deve Essere Esattamente di 8 Caratteri.")
    parola = input("Inserisci Una Parola di 8 Lettere: ")

print("Hai Inserito una Parola di 8 Lettere!")"""

# ====================================================

# Chiedi all'utente di inserire numeri interi positivi e somma progressivamente i valori (solo se il numero è divisibile per 7.). Il programma
# termina solo quando la somma totale supera 100, poi mostra il totale e quanti numeri sono stati inseriti.

somma = 0
conteggio = 0

while somma <= 100:
    numero = int(input("Inserisci Numero: "))
    if  numero > 0 and numero % 7 == 0:
        somma += numero
        conteggio += 1

print(f"Somma Totale: {somma}")
print(f"Numeri Inseriti (Divisibili per 7): {conteggio}")