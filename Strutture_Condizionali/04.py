# Scrivi un Programma Che Verifica Se un Alimento può essere consumato o vietato in base al
# tipo di dieta di una persona

Vegano = ["carne", "pesce", "latte", "uova", "formaggio", "miele"]
Vegetariano = ["carne", "pesce"]
Senza_Glutine = ["pane", "pasta", "pizza", "biscotti"]

Tipo_Dieta = input("Inserisci Tipo di Dieta: ").lower()
Alimento = input("Inserisci L'Alimento: ").lower()

if Tipo_Dieta == "vegano":
    if Alimento in Vegano:
        print("Non Puoi Mangiare Questo Alimento")
    else:
        print("Puoi Mangiarlo")

elif Tipo_Dieta == "vegetariano":
    if Alimento in Vegetariano:
        print("Non Puoi Mangiare Questo Alimento")
    else:
        print("Puoi Mangiarlo")


elif Tipo_Dieta == "senza glutine":
    if Alimento in Senza_Glutine:
        print("Non Puoi Mangiare Questo Alimento")
    else:
        print("Puoi Mangiarlo")


else:
    print("Tipo di Dieta Non Valido")





