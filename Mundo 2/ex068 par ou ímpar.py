from random import randint
from time import sleep
while True:  
    print("=-="*30)
    print("VAMOS JOGAR PAR OU ÍMPAR")
    print("=-="*30)

    valor = int(input("Digite um valor:"))
    esc = str(input("Par ou Ímpar ? [P\I]")).upper().strip()[0]
    comp= randint(1,11)
    t= valor + comp
    total = t%2
    fim=0


    if total == 0:
        fim="P"
    else:
        fim="I"

    if fim == esc:
        bi= "JOGADOR GANHOUU !!!!"
    else:
        bi="COMPUTADOR GANHOU"
        

    print("=-="*30)
    print("Você jogou {} e o computador {}. Total de {} DEU {}".format(valor,comp,t, "PAR" if fim == "P" else "ÍMPAR"))
    print("=-="*30)
    print(bi)
    
    sleep(2)
    print("=-="*30)
    conti =str(input("Deseja continuar? [SIM/NÃO]")).upper().strip()[0]
    if conti == "N":
            print("ENCERRADO.")
            break
    elif conti == "S":
        if bi == "JOGADOR GANHOUU !!!!":
            print("DESSA VEZ VOU TE AMASSAR !!!")       

        elif bi == "COMPUTADOR GANHOU":
                print("BORAAA NOVAMENTE!!\nPERDE PARA MIM")








