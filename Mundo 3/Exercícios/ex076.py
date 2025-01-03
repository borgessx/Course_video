preços=("carro",40000,"moto",25000,
        "borracha",2.50,"caneta",3,"celular",2300,
        "saco",0.50,"caderno",15,"corretivo",4)

print("-"*40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-"*40)

for c in range(0,len(preços)):
    if c %2==0:
        print(f"{preços[c]:.<30}", end = '')
    else:
        print(f"R${preços[c]:>7.2f}")
print("-"*40)