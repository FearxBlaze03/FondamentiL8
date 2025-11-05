# ==================================
# REGISTRO SCOLASTICO
# ==================================

studenti = []
classi = []
voti = []
assenze = []

nome_stud = ""
voto = 0
indice = 0
num_assenze = 0

scelta = 0
n = 0

while scelta != 10:
    print("==================================")
    print(" REGISTRO SCOLASTICO")
    print("==================================")
    print("1. Aggiungi uno studente")
    print("2. Mostra elenco studenti")
    print("3. Inserisci un voto a uno studente")
    print("4. Inserisci un’assenza")
    print("5. Mostra voti e assenze di uno studente")
    print("6. Calcola media di uno studente")
    print("7. Calcola media generale della classe")
    print("8. Mostra classifica studenti per media")
    print("9. Mostra studenti con troppe assenze")
    print("10. Stampa tabella riepilogativa")
    print("11. Esci")
    print("----------------------------------")

    scelta = int(input("Scegli Un'Opzione: "))

    if scelta == 1:
        print("TODO: aggiungi studente")
        n = int(input("Inserisci Numero Di Elementi: "))

        for i in range(n):
            nome_stud = input(f"Nome Studente {i + 1}: ")
            studenti.append(nome_stud)

            classe = input(f"Classe Studente {i + 1}: ")
            classi.append(classe)
            voti.append([])
            assenze.append([])

    elif scelta == 2:
        print("TODO: Mostra Elenco")
        for i in range(len(studenti)):
            print(f"{i + 1}. {studenti[i]} ({classi[i]})")

    elif scelta == 3:
        print("TODO: Inserisci Voto")
        nome_stud = input("Inserisci Il Nome Dello Studente: ")

        if nome_stud in studenti:
            indice = studenti.index(nome_stud)
            voto = int(input("Inserisci Voto: "))
            voti[indice].append(voto)
            print("Voto Aggiunto Correttamente!")

        else:
            print("Studente Non Trovato!")


    elif scelta == 4:
        print("TODO: Inserisci Assenza")
        nome_stud = input("Inserisci Il Nome Dello Studente: ")

        if nome_stud in studenti:
            indice = studenti.index(nome_stud)
            data_assenza = input("Data Dell'Assenza (gg/mm/aaaa): ")
            assenze[indice].append(data_assenza)
            print("Assenza Registrata!")
        else:
            print("Studente Non Trovato!")


    elif scelta == 5:
        print("TODO: Mostra Voti e Assenze")
        nome_stud = input("Inserisci Il Nome Dello Studente Da Mostrare: ")

        if nome_stud in studenti:
            indice = studenti.index(nome_stud)

            print(f"Voti di {studenti[indice]}: {voti[indice]}")
            print(f"Assenze di {studenti[indice]}: {assenze[indice]}")

    elif scelta == 6:
        print("TODO: Calcola Media Studente")

        nome_stud = input("Inserisci Il Nome Dello Studente Da Calcolare La Media: ")

        if nome_stud in studenti:
            indice = studenti.index(nome_stud)

            if len(voti[indice]) > 0:
                media = sum(voti[indice]) / len(voti[indice])
                print(f"Media di {nome_stud}: {media}")
            else:
                print("Nessun Voto Disponibile Per Questo Studente")

        else:
            print("Studente Non Trovato!")


    elif scelta == 7:
        print("TODO: Calcolo Media Generale")

        totale_voti = 0
        totale_numero = 0

        for voti_studente in voti:
            totale_voti += sum(voti_studente)
            totale_numero += len(voti_studente)

        if totale_numero > 0:
            media = totale_voti / totale_numero
            print(f"Media Generale Della Classe: {media}")
        else:
            print("Nessun Voto Disponibile")


    elif scelta == 8:
        print("Classifica studenti per media:")

        classifica = []
        for i in range(len(studenti)):
            if len(voti[i]) > 0:
                media_studente = sum(voti[i]) / len(voti[i])
            else:
                media_studente = 0
            classifica.append((media_studente, studenti[i]))

        classifica.sort(reverse=True)

        for idx, (media, nome) in enumerate(classifica, start=1):
            print(f"{idx}. {nome} - {media:.2f}")


    elif scelta == 9:
        print("Studenti con troppe assenze:")

        limite_assenze = 3
        troppi_assenti = []

        for i in range(len(studenti)):
            numero_assenze = len(assenze[i])
            if numero_assenze > limite_assenze:
                troppi_assenti.append((studenti[i], numero_assenze))

        if len(troppi_assenti) == 0:
            print("Tutti gli studenti hanno un numero accettabile di assenze.")
        else:
            for nome, num in troppi_assenti:
                print(f"- {nome} ({num} assenze)")


    elif scelta == 10:
        break
