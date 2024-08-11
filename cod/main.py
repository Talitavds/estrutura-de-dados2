import time
import os
import pandas as pd
import modelo1
import modelo2
import modelo3

num_tentativas = 50

tempos = {
    'modelo1': [],
    'modelo2': [],
    'modelo3': []
}

def tempo():
    for i in range(num_tentativas):
        for j, modelo in enumerate([modelo1, modelo2, modelo3], start=1):
            inicio = time.time()
            modelo.executar()
            fim = time.time()
            tempos[f'modelo{j}'].append(fim - inicio)

tempo()

os.system('cls' if os.name == 'nt' else 'clear')

df = pd.DataFrame(tempos)

df.loc['Média'] = df.mean()

print(df)

melhor_modelo = df.loc['Média'].idxmin()
print(f"\nO melhor modelo em média foi: {melhor_modelo} com tempo médio de {df.loc['Média', melhor_modelo]:.6f} segundos.")


'''
DE MODO GERARL PODEMOS DIZER QUE A BUSCA BINÁRIA PARA UMA QUANTIDADE REDUZIDA DE DADOS 
É MAIS EFICIENTE EM TERMOS DE TEMPO DE EXECUÇÃO
'''