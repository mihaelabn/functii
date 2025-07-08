# exercitiul 1


#afiseaza pe ecran


#car_name = "Volvo"
#car_name = "Polester"
#print(car_name)


y = 1234
x = 3000
#y, x = 1234, 3000


sum_numere = x + y

sum_numere = 1+2+3+4+5+6+7+8+9+10

#suma lui Gauss

n = 10

sum_numere = (n*(n+1)) /2
print(sum_numere)

print(f"suma_numere * 3 ={sum_numere*3}")

nume_prenume = "Popa Ana"
numar_intreg = 10
print(nume_prenume + " "+str(numar_intreg))


#variabila constanta
CONSTANTA_MATEMATICA = 4
print(CONSTANTA_MATEMATICA)
CONSTANTA_MATEMATICA = 5
print(CONSTANTA_MATEMATICA)


#citirea de la tastatura a 5 produse din lista

produs1 = input("introduceti produsul1:")
pret1 = input("introduceti pretul1:")

produs2 = input("introduceti produsul2:")
pret2 = input("introduceti pretul2:")

produs3 = input("introduceti produsul3:")
pret3 = input("introduceti pretul3:")

produs4 = input("introduceti produsul4:")
pret4 = input("introduceti pretul4:")

produs5 = input("introduceti produsul5:")
pret5 = input("introduceti pretul5:")

print(f"{"PRODUSUL":>25} {"PRET:"<20}")
print(20*"_")
print(f"{produs1:>25} {pret1:<20}")
print(f"{produs2:>25} {pret2:<20}")
print(f"{produs3:>25} {pret3:<20}")
print(f"{produs4:>25} {pret4:<20}")
print(f"{produs5:>25} {pret5:<20}")


#aria unui cerc

import math
raza = float(input("Introduceti raza cerculu:"))
aria = math.pi * raza **2
print(f"Aria {aria:4f}")


#lungimea cercului
lungimea = 2* math.pi *raza
print(f"Lungimea cercului: {lungimea:.6f}")
