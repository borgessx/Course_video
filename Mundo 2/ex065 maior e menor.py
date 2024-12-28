resp = "S"

media = soma = cont = maior = menor = 0

while resp in "Ss":
    núm = int(input("Digite um número:"))
    cont = cont + 1
    soma = soma + núm
    media = soma / núm
    if cont == 1:
        maior = menor = núm    
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm

    resp = str(input("Quer continuar [s/n]?")).upper().strip()[0]
print("acabou !\nA soma dos números digitados foi {} e a média {}.\nO maior número foi {} e menor foi {}. ".format(soma,media, maior, menor))