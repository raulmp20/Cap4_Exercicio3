import numpy as np

#CARREGANDO UM DATASET

arr = np.loadtxt('space.csv',
                 delimiter=';',
                 encoding='utf-8',
                 dtype=str)

#Exercicio1
sucessos = len(arr[1:, 7]) - np.count_nonzero(np.char.find(arr[1:, 7], "Success"))

print(((sucessos/len(arr[1:, 7]))*100)) #Porcentagem

#Exercicio2
num_missoes = np.max(arr[1:, 0].astype('int'))
gastos = np.sum(arr[1:, 6].astype('float'))

print(f'Numero de missoes:  {num_missoes}')
print(f'Total gasto: {gastos}')
print(f'Média de Gastos: {gastos/num_missoes}')

#Exercicio3
total_paises = arr[1:, 2]
estados_unidos = np.char.endswith(total_paises, "USA")
num_EUA = np.sum(estados_unidos)

print(f'Missões realizadas nos EUA: {num_EUA}')

#Exercicio4
missaoX = arr[1:, (1, 6)]
custos = arr[1:, 6]
valor_maior = np.max(custos[missaoX[0:, 0] == "SpaceX"].astype('float'))

print(f'Missao de maior custo da SpaceX: {valor_maior}')

#Exercicio5
companhias = np.unique(arr[1:, 1])

for companhia in companhias:
    aux = np.char.find(arr[1:, 1], companhia)
    missoes = np.sum(aux) + arr[1:, 1].size
    print(f'Companhia:{companhia} \n Total de missoes: {missoes}')