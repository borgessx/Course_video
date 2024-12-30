nomes_núm = ("zero","um","dois","três","quatro",
             "cinco","seis","sete","oito","nove",
             "dez","onze","doze","treze","catorze",
             "quinze","dezesseis","dezessete","dezoito",
             "dezenove","vinte")

while True:
    n = int(input("Digite um número entre 0 e 20:  "))
    
    if n >=0 and n <=20:
        print(f"Você digitou o número {nomes_núm[n]}")
        continuar = str(input("Você deseja continuar [SIM OU NÃO]?")).upper().strip()[0]
        if continuar == "N":
            break
    
    print("Tente novamente!! Digite um número entre 0 e 20.")
    
