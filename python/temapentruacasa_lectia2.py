# Tema pentru acasă - Input, Print


# Exercițiul 1 - Afișează un mesaj care folosește variabile pentru temperatura într-un oraș,
# creând doua variabile oras si temperatura
oras = "London"
temperatura = 30
print("Astazi in orasul " + oras + " este temperatura de " + str(temperatura) + " grade celsius")




# Exercițiul 2 - Folosește .format() pentru a afișa distanța dintre două orașe.
oras1 = "New York"
oras2 = "Washington"
distanta = 2356
print("Distanta dintre orasul {} si orasul {} este de {} km" .format(oras1, oras2, distanta))


# Exercițiul 3 - Folosește f-string pentru a afișa raportul între două numere,
# creând doar doua variabile.
num1 = 465
num2 = 32
raport = num1/num2
print(f"Raportul dintre {num1} si {num2} este :{raport:.2f}")


# Exercițiul 4 - Afișează prețul unui produs după aplicarea unui discount folosind .format().
produs = "Lapte"
pret_initial = 25
discount = 0.03
pret_final = pret_initial - (1 - discount/100)
print("Pretul la produsul {} dupa aplicarea discount-ului de {} este: {}" .format(produs, discount, pret_final))


# Exercițiul 5 - Folosește f-string pentru a afișa volumul unui cub cu latura, citita de la tastatura
# import math
# latura = int(input("Introduceti latura cubului "))
# volum = math.pi * latura**3
# print(f"Volumul cubului cu latura {latura} este {volum:.3f}")



# Exercițiul 6 - Afișează timpul total de lucru după n zile folosind .format().
ore_pe_zi = 8
zile = 5
ore_totale = ore_pe_zi * zile
print(f"Timpul total de lucru dupa {zile} zile este de {ore_totale} h")



# Exercițiul 7 - Folosește f-string pentru a calcula și afișa procentul de rezolvare a unor exerciții.
# nr_ex_totale = 47
# nr_ex_rezolvate = int(input("Introduceti nr de exercitii rezolvate: "))
# procent_de_rezolvare = (nr_ex_rezolvate/nr_ex_totale) * 100
# print(f"Procentul de rezolvare a {nr_ex_rezolvate} exercitii este de {procent_de_rezolvare:.2f}")



# Exercițiul 8 - Folosește .format() pentru a afișa prețul final al unui produs cu TVA.
produs = "Iaurt"
pret_fara_TVA = 47
TVA = 0.12
final = pret_fara_TVA * (1+ TVA/ 100)
print("Pretul la produsul {} cu TVA {} este {:.2f} lei".format(produs, TVA, final))



# Exercițiul 9 - Folosește f-string pentru a afișa vârsta pe care o vei avea în 10 ani.
# varsta = int(input("Introduceti varsta "))
# varsta2 = varsta + 10
# print (f"Varsta in 10 ani va fi {varsta2}")


# Exercițiul 10 - Calculează și afișează suma și media a trei numere folosind f-string,
# citite de la tastatura.

Num1 = int(input("Introduceti primul numar: "))
Num2 = int(input("Introduceti al doilea numar: "))
Num3 = int(input("Introduceti al treilea numar: "))
sum = Num1 + Num2 + Num3
media = (Num1 + Num2 + Num3) / 3
print(f"Suma numerelor este {sum}")
print(f"Media numerelor este {media:.3f}")
