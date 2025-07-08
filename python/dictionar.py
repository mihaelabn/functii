# numere = {}
# valori= ["unu", "doi", "trei", "patru", "cinci"]
# for i in range (1,6):
#     numere[i] = valori[i-1]
# for cheie, valoare in numere.items():
#     print(f"{cheie}: \"{valoare}\"")

dictionar = {1:"cheie", 
             2: "valoare", 
             "cheie2": "test", 
             "cheie3":3, 
             "cheie4:" : 3.3, 
             1: 2.2, 
             5.3: "valoare", 
             2:"valoare", 
             2:2.2}
dictionar_nou = {}
for key, value in dictionar.items():
    if type(key) == int:
        dictionar_nou[key] = value

print(dictionar_nou)