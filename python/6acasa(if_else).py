
if __name__=="__main__":
    #  1. Sumați toate elementele dintr-o listă dată.
    print("Sumați toate elementele dintr-o listă dată.")
    lista = [4, 5, 6]
    print(sum(lista))


    # 2. Verificați dacă elementul 'x' există în lista dată.
    print("Verificați dacă elementul 'x' există în lista dată.")
    lista = [1, 'x', 3]
    print('x' in lista)

    # 3. Verificați dacă un string este palindrom (se citește la fel și de la dreapta la stânga).
    print("Verificați dacă un string este palindrom (se citește la fel și de la dreapta la stânga).")
    text = "radar"
    print(text == text[::-1])

    # 4. Verificați dacă o listă este sortată crescător.
    print("Verificați dacă o listă este sortată crescător.")
    lista = [1, 2, 3, 4, 5]
    print(lista == sorted(lista))

    # 5. Verificați dacă o listă este subsecvență a altei liste.
    # Exemplu: lista ['a', 'b', 'c'] este subsecventa a listei ['a', 'b', 'c', 'd', 'e'] dar nu este secventa a listei ['a', 'b', 'f', 'c', 'd', 'e']
    print("Verificați dacă o listă este subsecvență a altei liste.")
    lista1 = ['a', 'b', 'c']
    lista2 = ['a', 'b', 'c', 'd', 'e']
    lista3 = ['a', 'b', 'f', 'c', 'd', 'e']

    index_lista1 = 0  # Index pentru a ține evidența poziției curente în lista1
    for elem in lista2:
        if index_lista1 < len(lista1) and elem == lista1[index_lista1]:
            index_lista1 += 1  # Trecem la următorul element din lista1
        if index_lista1 == len(lista1):
            break  # Am găsit toate elementele din lista1 în lista2

    # Verificăm dacă toate elementele din lista1 au fost găsite în lista2
    este_subsecventa_lista2 = index_lista1 == len(lista1)

    index_lista1 = 0  # Resetăm indexul pentru a verifica cu lista3
    for elem in lista3:
        if index_lista1 < len(lista1) and elem == lista1[index_lista1]:
            index_lista1 += 1  # Trecem la următorul element din lista1
        if index_lista1 == len(lista1):
            break  # Am găsit toate elementele din lista1 în lista3

    # Verificăm dacă toate elementele din lista1 au fost găsite în lista3
    este_subsecventa_lista3 = index_lista1 == len(lista1)

    print("Lista ['a', 'b', 'c'] este subsecvență a listei ['a', 'b', 'c', 'd', 'e']:", este_subsecventa_lista2)
    print("Lista ['a', 'b', 'c'] este subsecvență a listei ['a', 'b', 'f', 'c', 'd', 'e']:", este_subsecventa_lista3)



    # 6. Creați o sub-listă care să contina doar elementele interioare ignorand elementele de pe margini.
    print("# 6. Creați o sub-listă care să contina doar elementele interioare ignorand elementele de pe margini.")
    matrice_4x4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    # Inițializăm o listă goală pentru a stoca elementele interioare
    elemente_interioare = []

    # Parcurgem fiecare linie a matricei, excluzând prima și ultima linie
    for i in range(1, len(matrice_4x4) - 1):
        # Parcurgem fiecare element al liniei, excluzând primul și ultimul element
        for j in range(1, len(matrice_4x4[i]) - 1):
            # Adăugăm elementul curent la lista de elemente interioare
            elemente_interioare.append(matrice_4x4[i][j])

    print("Elementele interioare ale matricei sunt:", elemente_interioare)



    # 7. Verificați dacă un string introdus este 'da', 'nu' sau altceva.
    print("7. Verificați dacă un string introdus este 'da', 'nu' sau altceva.")
    raspuns = "poate"
    if raspuns == "da":
        print("Ai răspuns cu da.")
    elif raspuns == "nu":
        print("Ai răspuns cu nu.")
    else:
        print("Răspuns nerecunoscut.")


    # 8.Verificați dacă un număr este într-un interval dat. e.g. intre 1 si 10
    print("8. Verificați dacă un număr este într-un interval dat. e.g. intre 1 si 10")
    numar = 5
    if 1 <= numar <= 10:
        print("Numărul este în intervalul 1-10")
    else:
        print("Numărul nu este în intervalul 1-10")


    # 9. Dată fiind o variabilă `an`, verificați dacă este un an bisect.
    print('9. Dată fiind o variabilă `an`, verificați dacă este un an bisect.')
    an = 1900
    if an % 4 == 0:
        if an % 100 == 0:
            if an % 400 == 0:
                print("An bisect")
            else:
                print("Nu este an bisect")
        else:
            print("An bisect")
    else:
        print("Nu este an bisect")