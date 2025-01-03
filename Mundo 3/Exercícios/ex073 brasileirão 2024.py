times=("Botafogo","Palmeiras","Flamengo","Fortaleza","Internacional",
       "São Paulo","Corinthians","Bahia","Cruzeiro",
       "Vasco da Gama","EC Vitória","Atlético-MG","Fluminense",
       "Grêmio","Juventude","Bragantino","Athletico-PR",
       "Criciúma","Atlético-GO","Cuiabá")

print("="*30) 
print(f"Os 5 primeiro times:\n{times[0:5]} ")
print("="*30)
print(f"Os últimos 4 colocado:\n{times[-4:]}")#partir do -4 até o final
print("="*30)
print(f"Times em ordem alfabética:\n{sorted(times)}")
print("="*30)
print(f"O time São Paulo está na {times.index('São Paulo')+1}ª posição")#O mais um é para dar a posição exata, sem acrescentar o 0
print("="*30)
