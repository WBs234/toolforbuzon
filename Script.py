import phonenumbers
import time
import os
from phonenumbers import carrier

verde = "\033[92m"
vermelho = "\033[91m"

while True:
    os.system("clear")
    time.sleep(1)
    numero = input("Digite a base (+55XXXXXX): ")

    nuf = "f.txt"

    with open(nuf, "r") as file:
        nummf = file.read().splitlines()

    nums = []
    nummf(str)
    compnum = numero + nummf
    numero_parsed = phonenumbers.parse(compnum)
    operadora = carrier.name_for_number(numero_parsed, "pt-br")
               
    if operadora == "Claro":
         print(numero + verde + " é Claro!")
         nums.append(compnum)
    else:
         print(numero + vermelho + " não é Claro!")

    os.system("clear")
    print("Os números válidos são:", nums)

