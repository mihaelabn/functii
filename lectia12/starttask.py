# START TASK - Lecția 5.2 Funcții
# Timp estimat: 15 minute
# Branch: start-task-lesson-5-2

# Exercițiul 1: Creați o funcție care calculează aria unui dreptunghi
# Funcția să primească două parametri: lungime și lățime
# Ambii parametri să aibă valori default de 1
def aria_dreptunghi(lungime = 1, latime = 1):
    return lungime * latime
    

# Testare:
print(aria_dreptunghi())        # Ar trebui să afișeze 1 (1*1)
print(aria_dreptunghi(5))       # Ar trebui să afișeze 5 (5*1)  
print(aria_dreptunghi(5, 3))    # Ar trebui să afișeze 15 (5*3)


# Exercițiul 2: Creați o funcție de salut personalizat
# Funcția să primească nume (obligatoriu) și titlu (opțional, default "Domnule/Doamna")
# Să returneze un mesaj de salut
def salut_personalizat(nume, titlu="Domnule/Doamna"):
    # CODUL TĂU AICI
    return f"Buna ziua, {titlu} {nume}!"

# Testare:
print(salut_personalizat("Ion"))                    # "Bună ziua, Domnule/Doamna Ion!"
print(salut_personalizat("Ana", "Dr."))             # "Bună ziua, Dr. Ana!"
print(salut_personalizat(titlu="Prof.", nume="Pop")) # "Bună ziua, Prof. Pop!"


# Exercițiul 3: Creați o funcție care calculează prețul final după reducere
# Parametri: pret_initial (obligatoriu), reducere_procent (default 10), tva_procent (default 19)
# Să calculeze: pret_dupa_reducere = pret_initial * (1 - reducere_procent/100)
#               pret_final = pret_dupa_reducere * (1 + tva_procent/100)
def calculeaza_pret_final(pret_initial, reducere_procent = 10, tva_procent = 19):
    # CODUL TĂU AICI
    pret_dupa_reducere = pret_initial * (1 - reducere_procent / 100)
    pret_final = pret_dupa_reducere * (1 + tva_procent / 100)
    return pret_final

# Testare:
print(calculeaza_pret_final(100))                      # Preț 100, reducere 10%, TVA 19%
print(calculeaza_pret_final(100, 20))                  # Preț 100, reducere 20%, TVA 19%  
print(calculeaza_pret_final(100, reducere_procent=15, tva_procent=21))  # Toate specificate