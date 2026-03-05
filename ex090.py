alun = {}
alun['nome'] = str(input('Nome do aluno: ')).title().strip()
alun['média'] = float(input(f'Média de {alun['nome']}: '))
if alun['média'] >= 7:
    alun['situação'] = '\033[32mAPROVADO\033[m'
elif 5 <= alun['média'] < 7:
    alun['situação'] = '\033[33mRECUPERAÇÃO\033[m'
else:
    alun['situação'] = '\033[31mREPROVADO\033[m'
print()
for chav, valo, in alun.items():
    print(f' {chav} recebeu {valo}')