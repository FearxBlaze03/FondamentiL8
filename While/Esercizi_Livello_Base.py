# Chiedi all'utente di inserire una password. Continua a Chiedere Finchè la password inserita non coincide con quella corretta. 
# Usa While e If per controllare la correttezza.

password_corretta = "python123"

password = input("Inserisci Password: ")

while password != password_corretta:
    print("Password Errata. Riprova.")
    password = input("Inserisci Password: ")

print("Accesso Consentito.") 
    
