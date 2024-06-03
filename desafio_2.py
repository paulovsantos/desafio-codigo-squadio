ativos = []

#Entrada da quantidade de ativos
quantidadeAtivos = int(input("informe a qtd de ativos: "))

#Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input("Informe os respectivos ativos: ")
    ativos.append(codigoAtivo) #adiciona elementos na lista
    
ativos.sort()

for ativo in ativos:
    print(ativo)

 #Ordenar os ativos em ordem alfabética.

 #Imprimir a lista de ativos ordenada, um abaixo do outro