nume = list() #DECLARANDO VARIÁVEIS
pare = list()
impa = list()
while True: #INÍCIO DO LOOPING
	valo = int(input('\nDigite um valor: ')) #LEITURA DE VALORES
	nume.append(valo) #VALOR ENTRA NA LISTA
	if valo % 2 == 0: #VERIFICANDO SE O VALOR É PAR
		pare.append(valo) #VALOR ENTRA NA LISTA DOS PARES
	else: #CASO SEJA ÍMPAR
		impa.append(valo) #VALOR ENTRA NA LISTA DOS ÍMPARES
	coma = str(input('\033[31mPARAR?\033[m ')).upper().strip() #COMANDO DE INTERRUPÇÃO DO LOOPING
	if coma == 'S' or coma == 'SIM':
		break #FIM DO LOOPING
print(f'\nLista completa dos valores digitados: \033[33;7;1m {nume} \033[m' #VISUALIZAÇÃO DAS 3 LISTAS
      f'\n\nLista dos valores pares digitados: \033[34;7;1m {pare} \033[m'
      f'\n\nLista dos valores ímpares digitados: \033[35;7;1m {impa} \033[m')