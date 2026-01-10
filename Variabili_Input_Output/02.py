# Crea un Programma Che Converta un Numero di Secondi in Ore, Minuti e Secondi

print("=== CONVERTITORE DI TEMPO ===")
secondi = float(input("\nInserisci i Secondi: "))

ore = int(secondi//3600)
minuti = int(secondi % 3600) // 60
sec = int(secondi % 60)

print(f"Conversione: {ore:02d} Ore, {minuti:02d} Minuti, {sec:02d} Secondi")
