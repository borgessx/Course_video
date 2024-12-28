print("="*30)
print('{:^30}'.format('BANCO GRANDE'))
print("="*30)
valor = int(input("Que valor irá sacar?"))
total = valor
ced=50
totaced=0

while True:
    if total >= ced:
        total = total - ced
        totaced +=1
    else:
        if totaced > 0:
            print(f"total de {totaced} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totaced = 0
        if total == 0:
            break
print("="*30)
print("PROGRAMA ENCERRADO !!!") 
