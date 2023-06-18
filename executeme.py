import os
os.system("clear")
print("INSTALADOR")
print("\n")
os.system("pip install --upgrade pip")
os.system("pip install phonenumbers")
os.system("pip install twilio")
os.system("clear")
print("INSTALAÇÃO FINALIZADA")
print("Criando wordlist..")
time.sleep(2)
with open('f.txt', 'w') as file:
    for i in range(10000):
        number = str(i).zfill(4)
        file.write(number + '\n')
