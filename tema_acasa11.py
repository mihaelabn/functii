"""
Task: Creați o funcție cu numele "task_1" care va returna o listă cu numerele de la 1 la 10
Utilizați list comprehension.
"""
from math import factorial

# CODUL TĂU VINE MAI JOS:
def task_1():
    return[i for i in range(1,11)]
print(task_1())
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_2" care va returna o listă cu pătratele numerelor de la 1 la 10.
Utilizați list comprehension în proces
"""

# CODUL TĂU VINE MAI JOS:
def task_2():
    return[x**2 for x in range(1,11) ]
print(task_2())
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_3" care va returna o listă cu numerele impare de la 1 la 10.
Utilizați list comprehension în proces.
"""

# CODUL TĂU VINE MAI JOS:
def task_3():
    return[x for x in range(1,11) if x%2 != 0]
print(task_3())
# CODUL TĂU VINE MAI SUS:

"""
    Task: Creați o funcție cu numele "task_4" care primind ca argument o matrice de liste precum [[1, 2], [3, 4], [5, 6]]
    va returna o listă aplatizată sau altfel spus o listă cu elementele fiecărei liste , adică [1, 2, 3, 4, 5, 6]
"""

# CODUL TĂU VINE MAI JOS:
def task_4(lista):
    result = []
    for sublist in lista:
        result.extend(sublist)
    return result
lista = [[1,2],[3,4],[5,6]]
print(task_4(lista))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_5" care utilizând list comprehension va returna o listă care conține string-ul "par" sau "impar" pentru fiecare număr de la 1 până n (inclusiv n).
Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
Exemplu: Pentru n=10 rezultatul returnat va fi ["impar", "par", "impar", "par", "impar", "par", "impar", "par", "impar", "par"]
"""

# CODUL TĂU VINE MAI JOS:
def task_5(n):
    return["par" if x%2 ==0 else "impar" for x in range(1, n+1)]
print(task_5(3))

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_6" care utilizând list comprehension va returna un dicționar care mappează fiecare număr de la 1 la 5 la cubul său.
Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face maparea.
Exemplu: Pentru n=5 rezultatul returnat va fi {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
"""

# CODUL TĂU VINE MAI JOS:
print("Ex 6:")
def task_6(n):
    return {x: x**3 for x in range(1, n + 1)}
print("Ex 6:")
n = int(input("Introduceti n: "))
print(task_6(n))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_7" care utilizând list comprehension va returna un set cu multiplii de 3 de la 1 la n, unde n este un argument al funcției.
Funcția va primi ca argument un număr n care va reprezenta numărul până la care se va face multiplicarea.
Exemplu: Pentru n=50 rezultatul returnat va fi {3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48}       
"""

# CODUL TĂU VINE MAI JOS:
print("Ex 7:")
def task_7(n):
    return {x for x in range(1, n + 1) if x % 3 == 0}
n = int(input("Introduceti n: "))
print(task_7(n))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_8" care are ca argument o listă de numere și va returna media aritmetică a numerelor din listă.
Exemplu: Pentru lista [1, 2, 3, 4, 5] rezultatul va fi 3.0
"""

# CODUL TĂU VINE MAI JOS:
print("EXERCITIUL 8")
def task_8(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)
input_ = input("Introdu elementele listei: ")
lista = [float(x) for x in input_.split(',')]
print(task_8(lista))

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_9" care are ca argument un număr și va returna `True` dacă numărul este par, altfel `False`.
Exemplu: Pentru numărul 4 rezultatul va fi `True`, iar pentru numărul 5 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
print("Ex 9:")
def task_9(n):
    if n%2 ==0:
        return True
    else:
        return False
numar = int(input("Introduceti numarul: "))
print(task_9(numar))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_10" care are ca argument numele și vârsta unei persoane ca argumente poziționale și orașul ca un argument opțional,
apoi returnează o descriere a persoanei în forma "Nume: *nume*, Varsta: *varsta*, Oras: *oras*".
Exemplu: Pentru numele "Ana", vârsta 32 și orașul "București" rezultatul va fi "Nume: Ana, Varsta: 32, Oras: București"
"""

# CODUL TĂU VINE MAI JOS:
print("Ex 10:")
def task_10(nume, varsta, oras = "Chisinau"):
    return f"Nume: {nume}, Varsta{varsta}, Oras:{oras}"
nume = input("Introduceti numele: ")
varsta = input("Introduceti varsta: ")
print(task_10(nume, varsta, oras="Chisinau"))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_11" care acceptă o listă variabilă de numere și returnează valoarea maximă.
Exemplu: Pentru lista [10, 20, 30, 40, 50] rezultatul va fi 50
"""

# CODUL TĂU VINE MAI JOS:
print("ex 11:")
def task_11(lista):
    if not lista:
        return None
    return max(lista)
lista = [10, 20, 30, 40, 50]
rezultat_task11 = task_11(lista)
print(rezultat_task11)

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_12" care acceptă un număr și returnează factorialul său.
Exemplu: Pentru numărul 5 rezultatul va fi 120
"""

# CODUL TĂU VINE MAI JOS:
print("Ex 12:")
def task_12(n):
    if n < 0:
        return None  # Factorialul nu e definit pentru numere negative
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
nr = int(input("Al cui factorial doriti sa il calculati?: "))
print(task_12(nr))


# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_13" care acceptă două numere și returnează suma și produsul lor.
Exemplu: Pentru numerele 3 și 4 rezultatul va fi (7, 12)
"""

# CODUL TĂU VINE MAI JOS:
print("Ex 13:")
def task_13(a, b):
    suma = a + b
    produs = a * b
    return (suma, produs)
a = int(input("Dati a: "))
b = int(input("Dati b: "))
print(task_13(a, b))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_14" care acceptă un număr ce reprezintă vârsta unei persoane și returnează textul "minor" dacă vârsta este sub 18 ani, "adult" dacă vârsta este între 18 și 65 ani și "senior" dacă vârsta este peste 65 de ani.
Exemplu: Pentru vârsta 32 rezultatul va fi "adult"
"""

# CODUL TĂU VINE MAI JOS:
print("Ex 14:")
def task_14(varsta):
    if varsta < 18:
        return "minor"
    elif varsta <= 65:
        return "adult"
    else:
        return "senior"
varsta = int(input("Dati varsta: "))
print(task_14(varsta))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_15" care acceptă un string și returnează `True` dacă string-ul este un palindrom, altfel `False`.
Exemplu: Pentru string-ul "ana" rezultatul va fi `True`, iar pentru string-ul "test" rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
print("Ex 15:")
def task_15(sir):
    sir = sir.lower()  
    sir = sir.replace(" ", "")  
    return sir == sir[::-1]
str = input("Dati un string: ")
print(task_15(str))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_16" care acceptă un string și returnează același string cu literele inversate.
Exemplu: Pentru string-ul "test" rezultatul va fi "tset"
"""

# CODUL TĂU VINE MAI JOS:
print("Ex 16:")
def task_16(sir):
    return sir[::-1]
str = input("Dati un string: ")
print(task_16(str))

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_17" care acceptă un string și returnează numărul de cuvinte din string.
Exemplu: Pentru string-ul "Hello, World!" rezultatul va fi 2
"""

# CODUL TĂU VINE MAI JOS:
print("Ex 17:")
def task_17(sir):
    cuvinte = sir.strip().split()
    return len(cuvinte)
str = input("Dati un string: ")
print(task_17(str))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_18" care acceptă un număr ce reprezintă temperatura în grade Celsius și returnează temperatura în grade Fahrenheit.
Exemplu: Pentru temperatura 0 rezultatul va fi 32.0
"""

# CODUL TĂU VINE MAI JOS:
print("Ex 18:")
def task_18(temp_celsius):
    return (temp_celsius * 9/5) + 32
temp = float(input("Dati temperatura in C: "))
print(task_18(temp))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_19" care acceptă un număr și returnează `True` dacă numărul este prim, altfel `False`.
Exemplu: Pentru numărul 7 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
print("Ex 19:")
def task_19(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
nr = int(input("Dati un numar: "))
print(task_19(nr))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_20" care acceptă un număr și returnează `True` dacă numărul este un număr perfect, altfel `False`.
Un număr perfect este un număr întreg pozitiv care este egal cu suma divizorilor săi, excluzând numărul însuși.
Exemplu: Pentru numărul 28 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
print("Ex 20:")
def task_20(n):
    if n <= 0:
        return False
    suma_divizori = 0
    for i in range(1, n):
        if n % i == 0:
            suma_divizori += i
    return suma_divizori == n
nr = int(input("Dati un numar: "))
print(task_20(nr))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_21" care acceptă un număr și returnează `True` dacă numărul este un număr Armstrong, altfel `False`.
Un număr Armstrong este un număr care este egal cu suma puterilor sale de cifre.
Exemplu: Pentru numărul 153 rezultatul va fi `True`, iar pentru numărul 10 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
# print("Ex 21:")

# nr = int(input("Dati un numar: "))
# print(task_21(nr))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_22" care acceptă un număr și returnează `True` dacă numărul este un număr Harshad, altfel `False`.
Un număr Harshad este un număr care este divizibil cu suma cifrelor sale.
Exemplu: Pentru numărul 18 rezultatul va fi `True`, iar pentru numărul 14 rezultatul va fi `False`.
"""

# CODUL TĂU VINE MAI JOS:
# print("Ex 22:")

# nr = int(input("Dati un numar: "))
# print(task_22(nr))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_23" care primește ca argument un număr și returneaeză o listă cu primele n numere ale seriei Fibonacci.
Exemplu: Pentru numărul 5 rezultatul va fi [0, 1, 1, 2, 3]
"""

# CODUL TĂU VINE MAI JOS:
print("Ex 23:")
def task_23(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib
nr = int(input("Dati un numar: "))
print(task_23(nr))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție cu numele "task_24" care primește ca argument un număr și returnează o listă cu divizorii numărului respectiv.
Exemplu: Pentru numărul 10 rezultatul va fi [1, 2, 5, 10]
"""

# CODUL TĂU VINE MAI JOS:
print("Ex 24:")

def task_24(n):
    if n <= 0:
        return []
    return [i for i in range(1, n + 1) if n % i == 0]

# Exemplu de utilizare:
nr = int(input("Dati un numar: "))
print(task_24(nr))


# CODUL TĂU VINE MAI SUS:
