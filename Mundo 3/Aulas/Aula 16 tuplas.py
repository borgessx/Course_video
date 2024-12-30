lanche = ("hambúrguer","Suco","Pizza","Pudim","Batata Frita")
#Tuplas são imutáveis

# print(lanche[:1])

# print(len(lanche))

# #maneira de ver os posição dos números
# for cont in range(0, len(lanche)):
#     print(cont)
# #outra opção, agora é para no lugar dos números colocar nomes
# for cont in range(0,len(lanche)):
#     print(lanche[cont])

#primeira forma
for comida in lanche:
    print(f"Eu vou cair de boca em {comida}")
print()
#segunda forma
for cont in range (0,len(lanche)):
    print(f"Eu vou me lambusar com {lanche[cont]}")
print()
#terceira forma "minha criação"
for cont in range(0,len(lanche)):
    print(f"{cont} - {lanche[cont]}")
print()
#quarta maneira
for pos,comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")
print()
#simples e rápido
for comida in lanche:
    print(f"Eu vou comer {comida}")
print()

#Usar SORTED(significa:organizado), deixa em ordem alfabetica
print(sorted(lanche))
#mas como a tupla é imutavel, ele não muda a ordem, mas sim imprimi em ordem
#demostração
print(lanche)#continua do mesmo jeito

print()

#Soma de tuplas
a = (2,5,4)
b = (5,8,1,2)
soma = a+b
soma2 = a+b+b+a
print(soma)
#contador, quantas vezes aparece o número 5
print(soma.count(5))
#encontra a posição do que voce procura
print(soma.index(8))
print(soma2.index(8))#ele sempre mostra a posição do primeiro oite que aparece
#Nessa vai procura o cinco, depois da posição 1.
print(soma.index(5,1))
#cinco é o número que procura e o um é que posição voce deseja começar
print()
pessoa = ("Gustavo",39,"M",99.80)
#del(pessoa) #Apaga a tupla
#No python ele não aceita excluir apenas um item mais sim a tupla inteira.
#exemplo:
#delete na pisção 1
#del(pessoa[1])
print(pessoa)