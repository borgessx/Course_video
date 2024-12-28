"""
Simplificar ele
n= 0
cont = 0
soma = 0
"""
n=cont=soma=0
n = int(input("Digite um número [999 STOP!] :"))
while n != 999:
    soma += n
    cont += 1
    n= int(input("Digite um número [999 STOP!] :"))
    #colocando a variavel (N) fora e no final do while faz que ela não entre na condição soma e cont

print("Você digitou {} números, e a soma entre eles foi {} .".format(cont,soma))


