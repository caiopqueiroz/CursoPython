n = int(input('Número de 0 a 9999: '))
u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Analisando o número: \n {u} unidade(s) \n {d} dezena(s) \n {c} centena(s) \n {m} milhar(es)')
