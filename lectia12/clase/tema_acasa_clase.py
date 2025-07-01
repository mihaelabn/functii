"""
TASK pentru determinarea variantei:

Calculați suma valorilor ASCII pentru fiecare caracter din numele și prenumele vostru,
apoi determinați varianta după formula: (suma % 3) + 1

HINT: Folosiți funcția ord() pentru a converti un caracter în valoarea sa ASCII

Exemplu de implementare:
Dacă numele este "Ana Pop":
- Pentru 'A': ord('A') = 65
- Pentru 'n': ord('n') = 110
- Pentru 'a': ord('a') = 97
- Pentru ' ': ord(' ') = 32
- Pentru 'P': ord('P') = 80
- Pentru 'o': ord('o') = 111
- Pentru 'p': ord('p') = 112
Suma totală = 65 + 110 + 97 + 32 + 80 + 111 + 112 = 607
Varianta = (607 % 3) + 1 = 2


După ce v-ați determinat varianta ((suma_ASCII % 3) + 1), veți primi una din următoarele sarcini:

Varianta 1: Perfect Number
- Un număr perfect este un număr natural care este egal cu suma divizorilor săi proprii (toți divizorii pozitivi în afară de numărul însuși)
- Exemplu: 28 este număr perfect pentru că: 1 + 2 + 4 + 7 + 14 = 28
- Alte exemple: 6 (1 + 2 + 3 = 6), 496 (1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248 = 496)
- Trebuie să implementați o clasă care verifică dacă un număr este perfect

Varianta 2: Armstrong Number
- Un număr Armstrong este un număr care este suma cifrelor sale ridicate la puterea 3
- Exemplu: 371 este număr Armstrong pentru că: 3^3 + 7^3 + 1^3 = 27 + 343 + 1 = 371
- Alte exemple: 153, 370, 407
- Trebuie să implementați o clasă care verifică dacă un număr este Armstrong

Varianta 3: Harshad Number
- Un număr Harshad este un număr care este divizibil cu suma cifrelor sale
- Exemplu: 18 este număr Harshad pentru că: 1 + 8 = 9 și 18 este divizibil cu 9
- Alte exemple: 20 (2+0=2, 20/2=10), 21 (2+1=3, 21/3=7)
- Trebuie să implementați o clasă care verifică dacă un număr este Harshad

Pentru oricare din variante, clasa trebuie să conțină:
1. Constructor care primește numărul
2. Metodă pentru verificarea proprietății
3. Metodă pentru afișarea rezultatului

Structura clasei trebuie să fie similară cu:

class NumarSpecial:
    def __init__(self, number):
        self.number = number
        self.is_special = False

    def check(self):
        # Implementați verificarea specifică variantei
        pass

    def print_state(self):
        # Afișați rezultatul verificării
        pass
"""
from tabnanny import check


# sum = 0
# nume = "Alexandr Tisliuc"
# for i in nume:
#     sum += ord(i)
#
# print((sum % 3) + 1)

# Varianta 3

class NumarSpecial:
    def __init__(self, number):
        self.number = number
        self.is_special = False

    def check(self):
        nr = str(self.number)
        suma = 0
        for i in range(len(nr)):
            suma += int(nr[i])
        if self.number % suma == 0:
            self.is_special = True
        return self.is_special

    def print_state(self):
        if self.is_special:
            return f"Nr {self.number} este nr Harshad"
        else:
            return f"Nr {self.number} nu este nr Harshad"

n = NumarSpecial(18)
# print(n.check())
# print(n.print_state())

