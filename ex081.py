nume = list() #DECLARANDO VARIÁVEIS
contvalo = 0
while True: #INÍCIO DO LOOPING
	valo = int(input('\nDigite um valor: ')) #LEITURA DE VALORES
	nume.append(valo) #VALOR ENTRA NA LISTA
	contvalo += 1 #CONTAGEM DE VALORES
	coma = str(input('\033[31mPARAR?\033[m ')).upper().strip() #COMANDO DE INTERRUPÇÃO DO LOOPING
	if coma == 'S' or coma == 'SIM':
		break #FIM DO LOOPING
print(f'\n\033[33;7;1m {nume} \033[m\n') #VISUALIZAÇÃO DA LISTA
print(f'Total de valores digitados: \033[33;7;1m {contvalo} \033[m\n') #VER CONTAGEM DE VALORES
nume.sort(reverse=True) #LISTA EM ORDEM DECRESCENTE (PERMANENTE)
print(f'Listagem dos valores em ordem DEcrescente: \033[33;7;1m {nume} \033[m\n') #VER LISTA EM ORDEM DECRESCENTE
if 5 in nume: #VERIFICANDO SE O VALOR 5 ESTÁ NA LISTA
	print('O valor 5 foi digitado e \033[32mESTÁ\033[m na lista') #CONFIRMANDO 5 NA LISTA
else:
	print('O valor 5 não foi digitado e \033[31mNÃO ESTÁ\033[m na lista') #DESCONFIRMANDO 5 NA LISTA