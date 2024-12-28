c =0
h= 0
i=0
while True:
    print("-"*30)
    print("CADASTRE UMA PESSOA")
    print("-"*30)
    nome=str(input("Digite o nome:"))
    idade=int(input("Digite a idade:"))
    
    if idade >= 18:
        c += 1
    sexo=str(input("Qual o sexo: [Maculino/Feminino]")).upper().strip()[0]
    if sexo == "M":   
        h += 1
    if sexo == "F" and idade <= 20:
        i +=1
    print("-"*30)
    continuar = str(input("Deseja continuar?[SIM/NÃO]")).upper().strip()[0]
    if continuar == "N":
        print("Tem {} com mais de 18 anos.\nTem {} homens cadastrado.\nTem {} mulheres de com menos de 20 anos.".format(c,h,i))
        break
    
