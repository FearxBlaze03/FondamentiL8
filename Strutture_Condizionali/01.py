# Scrivi Un Programma Che, Data una Temperatura in Gradi Celsius, Indichi in che stato si trova l'acqua

# Sotto 0°C -> "Solido (Ghiaccio)"
# Da 0°C a 100°C -> "Liquido"
# Sopra 100°C -> "Gassoso (Vapore)"

temperatura = int(input("Inserisci Temperatura: "))
if temperatura < 0:
    print("l'Acqua è in Stato: Solido (Ghiaccio)")
elif 0 < temperatura < 100:
    print("L'Acqua è in Stato: Liquido")
else:
    print("L'Acqua è in Stato: Gassoso (Vapore)")