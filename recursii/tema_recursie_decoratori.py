# Tema pentru acasă - Lecția 5.4: Recursie și Decoratori

"""
Task: Creați o funcție recursivă cu numele "task_1" care calculează factorialul unui număr.
Factorial: n! = n * (n-1) * (n-2) * ... * 1
Cazul de bază: 0! = 1 și 1! = 1
Exemplu: task_1(5) -> 120
         task_1(3) -> 6
         task_1(0) -> 1
"""

# CODUL TĂU VINE MAI JOS:
print("Task 1")
def task_1(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * task_1(n - 1)
print(task_1(5)) 
print(task_1(3)) 
print(task_1(0)) 

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție recursivă cu numele "task_2" care calculează suma numerelor 
de la 1 la n.
Exemplu: task_2(5) -> 15 (1+2+3+4+5)
         task_2(3) -> 6 (1+2+3)
         task_2(1) -> 1
"""

# CODUL TĂU VINE MAI JOS:
print("Task 2")
def task_2(n):
    if n == 1:
        return 1
    else:
        return n + task_2(n - 1)
print(task_2(5))
print(task_2(3))
print(task_2(1))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție recursivă cu numele "task_3" care calculează al n-lea număr Fibonacci.
Secvența Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
Exemplu: task_3(6) -> 8
         task_3(10) -> 55
"""

# CODUL TĂU VINE MAI JOS:
print("Task 3")
def task_3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return task_3(n - 1) + task_3(n - 2)
print(task_3(6))
print(task_3(10))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție recursivă cu numele "task_4" care calculează puterea unui număr.
Folosiți formula: a^n = a * a^(n-1), cu cazul de bază a^0 = 1.
Exemplu: task_4(2, 3) -> 8
         task_4(5, 2) -> 25
         task_4(10, 0) -> 1
"""

# CODUL TĂU VINE MAI JOS:
print("Task 3")
def task_4(a, n):
    if n == 0:
        return 1
    else:
        return a * task_4(a, n - 1)
print(task_4(2, 3))
print(task_4(5, 2))
print(task_4(10, 0))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție recursivă cu numele "task_5" care numără cifrele unui număr pozitiv.
Exemplu: task_5(12345) -> 5
         task_5(987) -> 3
         task_5(7) -> 1
"""

# CODUL TĂU VINE MAI JOS:
print("Task 5")
def task_5(n):
    if n < 10:
        return 1
    else:
        return 1 + task_5(n // 10)
print(task_5(12345))
print(task_5(987))
print(task_5(7))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție recursivă cu numele "task_6" care inversează un string.
Exemplu: task_6("hello") -> "olleh"
         task_6("python") -> "nohtyp"
         task_6("a") -> "a"
"""

# CODUL TĂU VINE MAI JOS:
print("Task 6")
def task_6(s):
    if len(s) <= 1:
        return s
    else:
        return task_6(s[1:]) + s[0]
print(task_6("hello"))
print(task_6("python"))
print(task_6("a"))
# CODUL TĂU VINE MAI SUS:

"""
Task: Creați un decorator simplu cu numele "task_7" care afișează un mesaj 
înainte și după executarea unei funcții.
Mesajul să fie: "Începe [nume_functie]" și "Termină [nume_functie]"
Testați-l pe o funcție care afișează "Bună ziua!".
"""

# CODUL TĂU VINE MAI JOS:
print("Task 7")
def task_7(func):
    def wrapper():
        print(f"Începe {func.__name__}")
        func()
        print(f"Termină {func.__name__}")
    return wrapper

@task_7
def salut():
    print("Bună ziua!")

salut()

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați un decorator cu numele "task_8" care numără de câte ori 
a fost apelată o funcție și afișează numărul de apeluri.
Exemplu: "Funcția [nume_functie] a fost apelată de [nr] ori"
Testați pe o funcție simplă.
"""

# CODUL TĂU VINE MAI JOS:
print("Task 8")
def task_8(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Funcția {func.__name__} a fost apelată de {wrapper.count} ori")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper
@task_8
def salut():
    print("Salut!")

salut()
salut()
salut()


# CODUL TĂU VINE MAI SUS:

"""
Task: Creați un decorator cu numele "task_9" care afișează argumentele 
cu care a fost apelată o funcție.
Exemplu: "Funcția [nume_functie] apelată cu argumentele: args=(1, 2), kwargs={'x': 3}"
Testați pe o funcție care primește mai multe argumente.
"""

# CODUL TĂU VINE MAI JOS:
print("TASK 9")
def task_9(func):
    def wrapper(*args, **kwargs):
        print(f"Funcția {func.__name__} apelată cu argumentele: args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper
@task_9
def aduna(a, b, x=0):
    return a + b + x

rezultat = aduna(1, 2, x=3)
print("Rezultat:", rezultat)

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați un decorator cu numele "task_10" care măsoară timpul de execuție 
al unei funcții și afișează rezultatul.
Folosiți modulul time pentru măsurătoare.
Exemplu: "Funcția [nume_functie] a rulat în [timp] secunde"
"""

# CODUL TĂU VINE MAI JOS:
print("TASK 10")
import time

def task_10(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rezultat = func(*args, **kwargs)
        end = time.time()
        durata = end - start
        print(f"Funcția {func.__name__} a rulat în {durata:.6f} secunde")
        return rezultat
    return wrapper
@task_10
def salut():
    time.sleep(1)
    print("Bună ziua!")

salut()


# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție recursivă cu numele "task_11" care verifică dacă 
un string este palindrom (se citește la fel în ambele sensuri).
Exemplu: task_11("radar") -> True
         task_11("hello") -> False
         task_11("aba") -> True
"""

# CODUL TĂU VINE MAI JOS:
print("TASK 11")
def task_11(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return task_11(s[1:-1])
print(task_11("radar"))  
print(task_11("hello"))  
print(task_11("aba"))    

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați un decorator cu numele "task_12" care validează că argumentele 
unei funcții sunt numere pozitive. Dacă nu sunt, să afișeze o eroare.
Testați pe o funcție care calculează media a două numere.
"""

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție recursivă cu numele "task_13" care calculează 
suma cifrelor unui număr.
Exemplu: task_13(123) -> 6 (1+2+3)
         task_13(456) -> 15 (4+5+6)
         task_13(7) -> 7
"""

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați o funcție recursivă cu numele "task_14" care găsește 
cel mai mare divizor comun (GCD) a două numere folosind algoritmul lui Euclid.
GCD(a, b) = GCD(b, a % b) dacă b != 0, altfel GCD(a, 0) = a
Exemplu: task_14(48, 18) -> 6
         task_14(100, 25) -> 25
"""

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

"""
Task: Creați un decorator cu numele "task_15" care transformă toate 
argumentele string ale unei funcții în majuscule înainte de execuție.
Testați pe o funcție care concatenează două string-uri.
"""

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

# Testare opțională - decomentează pentru a testa funcțiile
"""
# Test recursie
print("=== TEST RECURSIE ===")
print(f"Factorial 5: {task_1(5)}")
print(f"Suma 1-5: {task_2(5)}")
print(f"Fibonacci 6: {task_3(6)}")
print(f"2^3: {task_4(2, 3)}")
print(f"Cifre în 12345: {task_5(12345)}")
print(f"Inversez 'hello': {task_6('hello')}")

# Test decoratori
print("\\n=== TEST DECORATORI ===")

@task_7
def spune_salut():
    print("Bună ziua!")

@task_8
def conta_apeluri():
    print("Această funcție este numărată")

spune_salut()
conta_apeluri()
conta_apeluri()
conta_apeluri()
"""