# Crea un Calcolatore che Determini il Costo e La Durata di un Viaggio in Auto

print("=== CALCOLATORE DI VIAGGIO ===")
distanza = float(input("Inserisci La Distanza (Km): "))
consumo_medio = int(input("Inserisci il Consumo Medio (Litri / 100km): "))
prezzo_carburante = float(input("Inserisci Il Prezzo Carburante (€ / Litro): "))
velocita_media = int(input("Inserisci La Velocità Media (KM / H): "))

print("\n=== RISULTATI ===")
print(f"Distanza: {distanza} Km")
print(f"Consumo Medio: {consumo_medio} Litri / 100Km")
print(f"Prezzo Carburante: €{prezzo_carburante} / Litro")
print(f"Velocità Media: {velocita_media} Km / h")
print("============================================")


litri_necessari = float(distanza * (consumo_medio / 100))
costo_carburante = float(litri_necessari * prezzo_carburante)
tempo = int(distanza / velocita_media)


print(f"Litri Necessari: {litri_necessari:.2f} Litri")
print(f"Costo Carburante: €{costo_carburante:.2f}")
print(f"Tempo di Viaggio: {tempo} Ore, {(tempo % 1)*60} Minuti")

