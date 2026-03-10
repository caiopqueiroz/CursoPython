print('Matriz A')
print('-' * 30)
numelinhasA = int(input('Número de linhas da matriz A: '))
print()
numecolunasA = int(input('Número de colunas da matriz A: '))
print()
matriz = list()
linha = list()
for contador in range(0, numelinhasA):
    for contador2 in range(0, numecolunasA):
        linha.append(int(input(f'Elemento a{contador + 1}{contador2 + 1}: ')))
        contador2 += 1
    matriz.append(linha[:])
    linha.clear()
    print()
    contador += 1
for linha in matriz:
    contador3 = 0
    for numero in linha:
        print(f'   {linha[contador3]}', end='')
        contador3 += 1
    print()
print('-' * 30)
print()
# multiplicador = int(input('Número para multiplicar todos os elementos da matriz: '))
# for linha in matriz:
#     contador3 = 0
#     for numero in linha:
#         print(f'   {linha[contador3] * multiplicador}', end='')
#         contador3 += 1
#     print()
print('Matriz B')
print('-' * 30)
numelinhasB = int(input('Número de linhas da matriz B: '))
print()
numecolunasB = int(input('Número de colunas da matriz B: '))
print()
matrizB = list()
linhaB = list()
for contador in range(0, numelinhasB):
    for contador2 in range(0, numecolunasB):
        linhaB.append(int(input(f'Elemento b{contador + 1}{contador2 + 1}: ')))
        contador2 += 1
    matrizB.append(linhaB[:])
    linhaB.clear()
    print()
    contador += 1
for linhaB in matrizB:
    contador3 = 0
    for numero in linhaB:
        print(f'   {linhaB[contador3]}', end='')
        contador3 += 1
    print()
print('-' * 30)
print()
if numecolunasA == numelinhasB:
    
else:
    print('NÃO É POSSÍVEL DEFINIR O PRODUTO ENTRE AS MATRIZES')
