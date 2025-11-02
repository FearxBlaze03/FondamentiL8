# Chiedi all' utente di inserire un numero e usa un ciclo while per determinare se è un numero perfetto (la somma dei suoi divisori propri è
# uguale al numero stesso). Continua finché l'utente non inserisce un numero perfetto.

"""numero = int(input("Inserisci Un Numero Intero: "))

while True:
    somma_divisori = 0
    i = 1
    while i < numero:
        if numero % 1 == 0:
            somma_divisori += i
        i += 1
    if somma_divisori == numero:
        break
    print("Non è un numero Perfetto. Riprova.")
    numero = int(input("Inserisci Un Numero Intero: "))

print(f"Hai Inserito Un Numero Perfetto: {numero}") """

# ====================================================

# Fai inserire all'utente una serie di numeri interi uno dopo l9altro. Il programma deve continuare finché i numeri inseriti sono strettamente
# crescenti; quando l'utente inserisce un numero minore o uguale al precedente, il ciclo si interrompe e mostra quanti numeri validi sono stati inseriti.

"""conteggio = 1
precedente = int(input("Inserisci Il Primo Numero Intero: "))
numero = int(input("Inserisci Il Prossimo Numero: "))

while numero > precedente:
    conteggio += 1
    precedente = numero
    numero = int(input("Inserisci Il Prossimo Numero: "))

print(f"Hai Inserito {conteggio}, Numeri Strettamente Crescenti.")"""

# ====================================================

# Chiedi all'utente di inserire un indirizzo email e usa if per verificare che contenga il simbolo @ e il .it. Ripeti finchè l'email non rispetta le regole.

email = input("Inserisci Email Che Contenga '@' e '.it': ")

while not ("@" in email and ".it" in email):

    print("Email Non Valida. Riprova.")
    email = input("Inserisci Email Che Contenga '@' e '.it': ")

print(f"Email Valida: {email}")
