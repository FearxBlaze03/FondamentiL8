# Scrivi un Programma che Determini Se Un Anno è Bisestile Secondo Le Regole Del Calendario
# Gregoriano

anno = int(input("Inserisci Anno: "))

if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
    print("Anno Bisestile")
else:
    print("Anno NON Bisestile")
