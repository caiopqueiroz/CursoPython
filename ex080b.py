orde = [0]
cont = 0
while True:
    nume = int(input('Valor: '))
    if nume >= orde[cont]:
        orde.append(nume)
    cont += 1
    if cont == 5:
        break
print(orde)