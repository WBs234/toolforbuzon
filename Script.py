import phonenumbers
import time
import os
from phonenumbers import carrier

while True:
    os.system("clear")
    time.sleep(1)
    numero = input("digite a base(+55XXXXXX): ")
    
    nuf = "f.txt"

    with open(nuf,"r") as file:

        nummf = file.read().splitlines()
        str(nummf)


        compnum=numero+nummf

    numero_parsed = phonenumbers.parse(compnum)

    if phonenumbers.is_valid_number(numero_parsed):

        operadora = carrier.name_for_number(numero_parsed, "pt-br")

        break
    else:

        print("Número de telefone inválido.")
os.system("clear")
while True:

    if operadora == "Claro":

        print(numero+verde+"é Claro!")

        nums=[]

        nums.append(compnum)

    else:

        print(numero+vermelho+"não é Claro!")
os.system("clear")
print("Os números válidos são:", nums)
