# password = ""
#
# while password != "python123":
#     password = input("Password: ")
#
# if password != "python123":
#     print("Password Errata!")
#
# else:
#     print("Accesso Consentito")

# ======================================================
# totale = 0
#
# while True:
#     p = float(input("Inserisci Prezzo: "))
#     q = int(input("Inserisci Quantità: "))
#
#     totale = totale + (p * q)
#
#     continua = str(input("Vuoi Continuare?: "))
#
#     # DA SISTEMARE IL FATTO CHE SE SCRIVO QUALSIASI COSA DIVERSO DA SI, FA IL BREAK A PRESCINDERE
#     if continua != "si":
#         break
#
# if totale > 150:
#     totale = totale - (totale * 0.05)
#
# print(f"Il Totale Da Pagare è: {totale}")
# ======================================================

# VERIFICARE SE UN NUMERO E' PRIMO (DIVISIBLE PER 1 E SE STESSO)

n = int(input("Inserisci Un Numero: "))

if n < 2:
    print(f"{n} NON È UN NUMERO PRIMO!")
else:
    divisore = 2
    primo = True

    while divisore < n:
        if n % divisore == 0:
            primo = False
            break

        divisore = divisore + 1

    if primo:
        print(f"{n} È UN NUMERO PRIMO")
    else:
        print(f"{n} NON È UN NUMERO PRIMO!")
