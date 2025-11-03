# Chiedi all'utente di inserire una password. Continua a Chiedere Finchè la password inserita non coincide con quella corretta. Usa 3 - While e If per controllare la correttezza.

""" password_corretta = "python123"

password = input("Inserisci Password: ")

while password != password_corretta:
    print("Password Errata. Riprova.")
    password = input("Inserisci Password: ")

print("Accesso Consentito.")  """
    
# ====================================================

# Fai Inserire Numeri all'utente finché non digita 0. Usa If per contare quanti numeri pari e quanti dispari sono stati inseriti, poi mostra il risultato.

""" pari = 0
dispari = 0

numero = int(input("Inserisci Un Numero (0 Per Terminare): "))

while numero != 0:
    if numero % 2 == 0:
        pari += 1
    else:
        dispari += 1
    numero = int(input("Inserisci Un Numero (0 Per Terminare): "))

print(f"Numeri Pari Inseriti: {pari}")
print(f"Numeri Dispari Inseriti: {dispari}") """

# ====================================================

# L'utente inserisce una serie di numeri interi. Inserendo 0 si interrompe il ciclo. Alla Fine, stampa il numero più grande inserito.

""" numero = int(input("Inserisci Un Numero Intero (0 Per Terminare): "))
massimo = numero

while numero != 0:
    if numero > massimo:
        massimo = numero
    numero = int(input("Inserisci Un Numero Intero (0 Per Terminare): "))

print(f"Il Numero Più Grande Inserito è: {massimo}") """

# ====================================================



