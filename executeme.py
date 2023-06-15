import os
print("INSTALADOR")
print("\n")
os.system("pip install --upgrade pip")
os.system("clear")
print("INSTALADOR")
print("\n")
os.system("pip install phonenumbers")
with open('f.txt', 'w') as file:
    for i in range(10000):
        number = str(i).zfill(4)
        file.write(number + '\n')
