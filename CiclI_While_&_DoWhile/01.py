# ====================================================================
# Contatore Semplice
# contatore = 1
#
# while contatore <= 5:
#     print(f"Interazione {contatore}")
#     contatore = contatore + 1
#
# print("Ciclo Terminato!")
# ====================================================================
# Somma Dei Primi N Numeri

# n = int(input("Inserisci un Numero: "))
# somma = 0
# contatore = 1
#
# while contatore <= n:
#     somma = somma + contatore
#     contatore = contatore + 1
#
# print(f"La Somma Dei Primi {n} Numeri è: {somma}")
# ====================================================================
# Input Dell'Utente

# password = ""
#
# while password != "python123":
#     password = input("Password: ").lower() # ".lower()" converte la password in minuscola
#
#     if password != "python123":
#         print("Password errata!")
#     else:
#         print("Accesso Consentito!")
# ====================================================================

# Istruzione Break
# contatore = 1
#
# while contatore <= 10:
#     if contatore == 5:
#         print("Trovato il 5! Uscita.")
#         break
#
#     print(f"Numero: {contatore}")
#     contatore = contatore + 1
#
# print("Dopo il Ciclo")
#
# ====================================================================

# Break: Ricerca di Un Numero
# numero_segreto = 42
# tentativi = 0
# massimo_tentativi = 5
#
# while tentativi < massimo_tentativi:
#     tentativo = int(input("Indovina il Numero (1 - 100): "))
#     tentativi = tentativi + 1
#
#     if tentativo == numero_segreto:
#         print(f"Complimenti! Hai Indovinato in {tentativi} Tentativi!")
#         break # Termina Programma
#     elif tentativo < numero_segreto:
#         print("Troppo Basso!")
#     else:
#         print("Troppo Alto!")
#
#     if tentativi == massimo_tentativi:
#         print(f"Game Over! Il Numero era {numero_segreto}")
# ====================================================================

# Menu Interattivo
scelta = ""

while scelta != "4":
    print("=== MENÚ ===")
    print("1. Somma")
    print("2. Sottrazione")
    print("3. Moltiplicazione")
    print("4. Esci")

    scelta = input("Scegli Un Opzione: ")

    if scelta not in ["1", "2", "3"]:
        print("Scelta Non Valida!")
        continue

    a = float(input("Inserisci Pirmo Numero: "))
    b = float(input("Inserisci Secondo Numero: "))

    if scelta == "1":
        print(f"Risultato: {a + b}")
    elif scelta == "2":
        print(f"Risultato: {a - b}")
    elif scelta == "3":
        print(f"Risultato: {a * b}")
    elif scelta == "4":
        print("Arrivederci!")
        break

# ====================================================================
# Scrivere un Programma che Stampi Un Conto Alla Rovescia Da un Numero Inserito Dall'Utente Fino a Zero
#
# numero = int(input("Inserisci Numero: "))
#
# while numero >= 0:
#     print(numero)
#     numero -=  1
#
# print("Partenza!")

# ====================================================================

# Calcolare La Somma Di Tutti I Numeri Pari Da 2 A N (Dove N è Inserito dall'utente)

# n = int(input("Inserisci Il Limite: "))
# somma = 0
# numero = 2
#
# while numero <= n:
#     somma += numero
#     numero = numero + 2
#
# print(f"La Somma Dei Numeri Pari da 2 a {n} è: {somma}")

# ====================================================================

# Calcolare il Fattoriale Di Un Numero (N! = 1 x 2 x 3 ... x N)

# n = int(input("Inserisci Numero: "))
#
# fattoriale = 1
# count = 1
#
# while count <= n:
#     fattoriale = fattoriale * count
#     count = count + 1
#
# print(f"Il Fattoriale di {n} è: {fattoriale}")