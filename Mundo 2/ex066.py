cont=soma=0
while True:
    n=int(input("Digite um número:"))
    if n == 999:
        break
    cont = cont + 1
    soma = soma + n
print(f"Você digitou {cont} números e soma deles são {soma}")