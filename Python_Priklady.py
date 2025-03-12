
# Príklad Python kódu

# Iterácia cez čísla od 0 po 4
for i in range(5):
    # Tlačíme aktuálnu hodnotu iterátora
    print(i)
    
    # Debug: Vypíšeme informáciu o spracovanom čísle
    print(f"Spracované číslo: {i}")

# Ukážka tabuliek v Python kóde
from tabulate import tabulate

data = [
    ["Hodnota 1", "Hodnota 2", "Hodnota 3"],
    ["Hodnota 4", "Hodnota 5", "Hodnota 6"]
]
headers = ["Stlpec 1", "Stlpec 2", "Stlpec 3"]

# Tlač tabulky s formátom
print(tabulate(data, headers=headers, tablefmt="grid"))

# Príklad na spracovanie poznámok pod čiarou
poznamka = "Toto je poznámka pod čiarou."
print(f"Poznámka: {poznamka}")
