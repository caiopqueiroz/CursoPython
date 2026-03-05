conj = []
pare = []
impa = []
for cont in range(1, 8):
    valo = int(input(f'{cont}º valor: '))
    if valo % 2 == 0:
        pare.append(valo)
    else:
        impa.append(valo)
conj.append(pare[:])
conj.append(impa[:])
print(f'\n{conj}')
conj[0].sort()
conj[1].sort()
print(f'\nVALORES PARES EM ORDEM CRESCENTE:\n\n {conj[0]}'
      f'\nVALORES ÍMPARES EM ORDEM CRESCENTE:\n {conj[1]}')