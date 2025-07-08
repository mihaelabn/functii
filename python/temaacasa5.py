"""
# =====================================================================

# Exercitii cu citirea datelor din input și stocarea lor într-o listă

# =====================================================================
"""
# Exercițiul 1: Realizează o listă cu trei orașe preferate. Afișează ultimul oraș din listă folosind slicing negativ.
# Sugestie: Folosește -1 ca index pentru a accesa ultimul element din listă.
# orase = ["Chisinau", "Balti", "Orhei"]
# print(f"ultimul element din lista{orase} este {orase[-1]}")
a = "="
a*=100

# Exercițiul 2: Scrie un program care citește de la utilizator 5 activități preferate și le stochează într-o listă.
# Apoi, folosește index() pentru a afla poziția unei activități specificate de utilizator și afișeaz-o.
# Sugestie: Folosește input() pentru a obține activitățile și index() pentru a găsi poziția.

# activitati = []

# for i in range (5):
#     activitate  = input(f"Introduceti activitatea {i+1} ")
#     activitati.append(activitate)
# print(f"activitatile tale sunt: {activitati}")

# cautare = input("Activitatea cautata este: ")
# try:
#     pozitie = activitati.index(cautare)
#     print(f"Activitatea cautata se afla pe pozitia {pozitie}")
# except ValueError:
#     print("Activitatea nu se aflta in lista")
"""
# =====================================================================

# Exersare cu append, concatenare, extend, remove, del

# =====================================================================
"""

# Exercițiul 3: Creează o listă goală de cumpărături. Citește de la utilizator trei produse și adaugă-le în listă
# folosind append(). Afișează lista la final.
# cumparaturi = []
# for i in range (3):
#     lista_cmparaturi  = input(f"Introduceti lista {i+1} ")
#     cumparaturi.append(lista_cmparaturi)
# print(f"Lista ta de cumparaturi este: {cumparaturi}")

# Exercițiul 4: Folosește del pentru a elimina ultimul element din lista de cumpărături creată mai sus.
# Afișează lista după ștergere.
# del cumparaturi[-1]
# print(f"Lista finala este {cumparaturi}")
# Exercițiul 5: Creează o listă cu trei culori preferate.
# Cere utilizatorului să introducă o culoare și elimină-o din listă folosind remove(). Afișează lista.


"""
# =====================================================================

# Exersare cu pop, extend, remove, del

# =====================================================================
"""

# Exercițiul 6: Creează o listă de trei activități preferate. Elimină ultima activitate cu pop(),
# afișând atât activitatea eliminată, cât și lista rămasă.
# lista = ["citit", "dormit", "invatat"]
# print(lista)
# eliminare = lista.pop()
# print(f"Elementul eliminat din lista este {eliminare} \nLista finala este {lista}")

# Exercițiul 7: Creează o listă cu patru cărți. Adaugă o carte nouă la finalul listei cu append().
# Elimină prima carte din listă folosind del.
carti = ["romane", "drame", "detectiv", "thriller"]
print(f"Lista initiala: {carti}")
carti.append("actiune")
del carti[0]
print(f"Lista după adăugare și ștergere este: {carti}")
print(a)
# Exercițiul 8: Folosește lista de cărți creată mai sus. Scoate ultima carte cu pop()
# și afișează cartea scoasă împreună cu lista rămasă.
carti1 = carti.pop()
print(f"Cartea scoasa este: {carti1}\nLista finala: {carti}")
print(a)


"""
# =====================================================================

# Exerciții mai complexe cu liste

# =====================================================================
"""


# Exercițiul 9: Creează o listă de trei destinații de vacanță preferate. După ce utilizatorul adaugă o nouă destinație,
# îmbină lista originală cu cea nouă și afișeaz-o în ordine alfabetică.
vacanta = ["Monaco", "Dubai", "Spania"]
vacanta2 = ["Maldives"]
final = vacanta + vacanta2
final.sort()
print(final)
print(a)

# Exercițiul 10: Creează o listă cu numere de la 1 la 10. Afișează doar numerele pare folosind slicing și apoi elimină
# numerele impare din listă. Afișează lista finală cu numere pare.
numere = [1,2,3,4,5,6,7,8,9,10]
print(numere[1::2])
del numere[0::2]
print(numere)
print(a)