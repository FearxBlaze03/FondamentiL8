# Scrivi un Programma Che Calcoli  la Classe di Rischio di un Automobilista e il Coefficiente
# di Premio Assicurativo, basandosi su età, anni di patente e numero di incidenti recenti

eta = int(input("Inserisci Età: "))
if eta < 18:
    print("Non Può Guidare")
    exit()
else:
    annipatente = int(input("Inserisci Gli Anni Di Patente: "))
    incidenti = int(input("Inserisci Il Numero Di Incidenti Negli Ultimi 5 Anni: "))

if annipatente < 2:
    rischio = "Molto Alto"
    coefficiente = 50

elif incidenti > 2:
    rischio = "Molto Alto"
    coefficiente = 50

elif incidenti >= 1:
    rischio = "Alto"
    coefficiente = 35

elif eta < 25:
    rischio = "Medio"
    coefficiente = 20

else:
    rischio = "Basso"
    coefficiente = 0

print(f"Classe di Rischio: {rischio}")
print(f"Coefficiente Premio: +{coefficiente}%")



