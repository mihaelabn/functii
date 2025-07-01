def determina_varianta(nume_prenume):
    suma_ascii = sum(ord(c) for c in nume_prenume)
    varianta = (suma_ascii % 3) + 1
    return varianta

nume = "Ana Pop"
print(f"Varianta pentru '{nume}' este: {determina_varianta(nume)}")
