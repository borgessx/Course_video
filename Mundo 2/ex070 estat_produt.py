print("_--"*30)
print("LOJÃO DO BGZIN".center(60))
print("_--"*30)
total = cont = c = 0
menor="NAda"
while True:
    prod=str(input("Qual produto você deseja?")).upper()
    preço=float(input("Qual o preço?"))
    c =c +1
    if c == 1:
        c = preço
        menor = prod
    else:
        if preço < c:
            c =preço
            menor = prod
    if preço >= 1000:
        cont += 1
    total = total+ preço
    print("_--"*30)

    continuar=str(input("Vai comprar mais? [sim/não]")).upper().strip()[0]
    if continuar == "N":
        print("_--"*30)
        print(f"O valor total da compra foi {total}.\nSão {cont} produtos que valem mais de 1.000 reais.\nO produto mais barato foi {menor} e custa {c}.")
        break
    print("_--"*30)