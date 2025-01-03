n1=int(input("Digite um número:"))
n2=int(input("Digite mais um número:"))
n3=int(input("Digite o terceiro número:"))
n4=int(input("Digite o último número:"))

números = (n1,n2,n3,n4)

print("Você digitou os valores {}".format(números))

print(f"O número 9 foi digitado {números.count(9)} vezes.")
if 3 in números:
    print(f"O número 3 aparece na {números.index(3)+1}ª posição.")
else:
    print("O número 3 não foi digitado.")

print("Os números pares digitados foram", end=" ")
for n in números:
    if n % 2 ==0:
        print(n,end=" ")
