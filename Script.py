import time
import os
import phonenumbers 

verde = "\033[92m"
vermelho = "\033[91m"
azul = '\033[94m'
ciano = '\033[96m'
magenta = '\033[95m'
marrom = '\033[33m'
branco = '\033[97m'

nums = []

while True:
    os.system("clear")
    time.sleep(1)
    print("\n")
    print(ciano+"┏"+"━━━━"*5+"┓")
    print(ciano+" ["+marrom+"1"+ciano+"] "+marrom+"BruteBuzon")
    print(ciano+" ["+marrom+"2"+ciano+"] "+marrom+"Verificar Número")
    print("     Específico")
    print(ciano+"┗"+"━━━━"*5+"┛")
    print("\n")
    print(branco+"Oque deseja? ")
    fa=input(ciano+"["+marrom+"•"+ciano+"] "+marrom)
    print("\n")
    if fa=="1":
        import phonenumbers
        from phonenumbers import carrier
        import os
        numero_base = input(branco + "Digite a base (+55XXXXXXX): " + marrom)
        nuf = "f.txt"
        nums = []

        with open(nuf, "r") as file:
            for linha in file:
                linha = linha.rstrip()
                numero_completo = numero_base + linha


                def validar_numero_telefone(numero):
                    try:
                        numero_parseado = phonenumbers.parse(numero, "BR")
                        if phonenumbers.is_valid_number(numero_parseado):
                            return True
                        else:
                            return False
                    except phonenumbers.phonenumberutil.NumberParseException:
                        return False
                 if validar_numero_telefone(numero_completo):
                     numero_parseado = phonenumbers.parse(numero_completo, "BR")
                     operadora = carrier.name_for_number(numero_parseado, "pt-br")
                     os.system("clear")
                     if phonenumbers.is_valid_number(numero_parseado) is True:
                        if operadora == "Claro":
                            print(numero_completo + verde + " é Claro!")
                            nums.append(numero_completo)
                        else:
                            print(numero_completo + vermelho + " não é Claro!")

        os.system("clear")
        print("Os números válidos são:")
        print(nums)
        print("\n")
        print("Deseja tentar de novo?"+marrom+"[S|N]"+vermelho+" (Não esqueça de salvar os números)")
        re=input(ciano+"["+marrom+"•"+ciano+"] "+marrom)
        if re=="S":
            os.system("clear")
        else:
            break
    elif fa== "2":
        print(branco+"Digite o número assim "+marrom+"(+558877776666):")
        numero=input(ciano+"["+marrom+"•"+ciano+"] "+marrom)
        def validar_numero_telefone(numero):
            try:
                numero_parseado = phonenumbers.parse(numero, "BR")
                if phonenumbers.is_valid_number(numero_parseado):
                    return True
                else:
                    return False
            except phonenumbers.phonenumberutil.NumberParseException:
                return False
        def operadora_3():
            if operadora_nome== "Claro":
                print(vermelho)
                print(" ______________ ")
                print(" __  ____/__  /_____ _____________ ")
                print(" _  /    __  /_  __ `/_  ___/  __ |")
                print(" / /___  _  / / /_/ /_  /   / /_/ /")
                print(" \____/  /_/  \__,_/ /_/    \____/ ")
            elif operadora_nome == "Vivo":
                print(ciano)
                print(" ___    ______              ")
                print(" __ |  / /__(_)__   _______ ")
                print(" __ | / /__  /__ | / /  __ /")
                print(" __ |/ / _  / __ |/ // /_/ /")
                print(" _____/  /_/  _____/ \____/")
            elif operadora_nome== "Oi":
                print(verde)
                print(" ____________ ")
                print(" __  __ \__(_)")
                print(" _  / / /_  / ")
                print(" / /_/ /_  /  ")
                print(" \____/ /_/   ")
            elif operadora_nome== "Tim":
                print(azul)
                print(" ____________            ")
                print(" ___  __/__(_)______ ___ ")
                print(" __  /  __  /__  __ `__ |")
                print(" _  /   _  / _  / / / / /")
                print(" /_/    /_/  /_/ /_/ /_/ ")
        if validar_numero_telefone(numero):
            numero_parseado = phonenumbers.parse(numero, "BR")
            operadora_nome = carrier.name_for_number(numero_parseado, "pt-br")
            os.system("clear")
            print(ciano+"┏"+"━━━━"*5+"┓")
            print(" "+marrom+numero)
            print("\n")
            print(verde+" Válido")
            operadora_3()
            print(ciano+"┗"+"━━━━"*5+"┛")
            time.sleep(2)
            print("\n")
            print("Deseja tentar de novo?"+marrom+"[S|N]"+marrom)
            re=input(ciano+"["+marrom+"•"+ciano+"] "+marrom)
            if re=="S":
                os.system("clear")
            else:
                break
        else:
            print(ciano+"┏"+"━━━━"*5+"┓")
            print(marrom+numero)
            print("\n")
            print(vermelho+"INVALIDO")
            print(ciano+"┗"+"━━━━"*5+"┛")
            time.sleep(2)
            print("\n")
            print("Deseja tentar de novo?"+marrom+"[S|N]"+marrom)
            re=input(ciano+"["+marrom+"•"+ciano+"] "+marrom)
            if re=="S":
                os.system("clear")
            else:
                break
