from random import randint
sorteado=(randint(1,10),randint(1,10),randint(1,10),
          randint(1,10),randint(1,10))
print("Os valores sorteados foram:",end=" ")
for n in sorteado:
    print(f" {n} ", end=" ")
print(f"\nO maior número foi {max(sorteado)}")#max é o maior
print(f"O menor número foi {min(sorteado)}")#min é o menor