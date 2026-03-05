expr = str(input('Digite uma expressão numérica (com parênteses)\n'
                 '\033[33mExemplo: ((a + b) * c)\033[m\n\n'
                 ' ')).strip().lower() #LENDO A EXPRESSÃO
aber = expr.count('(') #LENDO QUANTIDADE DE PARÊNTESES ABERTOS
fech = expr.count(')') #O MESMO COM OS PARÊNTESES FECHADOS
inicaber = expr.find('(') #VERIFICANDO A POSIÇÃO DE INÍCIO DO PRIMEIRO PARÊNTESE ABERTO
inicfech = expr.find(')') #O MESMO COM O PRIMEIRO PARÊNTESE FECHADO
if aber == fech and inicaber < inicfech: #VALIDANDO A EXPRESSÃO
	print('\n\033[32;7;1m Sua expressão está CORRETA! \033[m') #RESPOSTA POSITIVA
else:
	print('\n\033[31;7;1m Sua expressão está ERRADA! \033[m') #RESPOSTA NEGATIVA