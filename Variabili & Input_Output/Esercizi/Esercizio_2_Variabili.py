# ESERCIZIO 2
# CREA UN PROGRAMMA CHE CONVERTA UN NUMERO DI SECONDI IN ORE, MINUTI E SECONDI

print("--------------------")
print("CONVERTITORE DI TEMPO")
print("--------------------")

# VARIABILI
secondi = int(input("Inserisci Secondi: "))

# FORMULE PER IL CALCOLO
ore = secondi // 3600
minuti = (secondi % 3600) // 60
secondi_rimanenti = secondi % 60

print(f"CONVERSIONE: {ore} ore, {minuti} minuti, {secondi_rimanenti} secondi")





