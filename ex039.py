nasc = int(input('Ano de nascimento: '))
sexo = str(input('Sexo (masculino ou feminino): ')).strip().title()
from datetime import date
atua = date.today().year
idad = atua - nasc
if sexo == 'Feminino':
    print('Você \033[31mnão\033[m deve se \033[32malistar no exército brasileiro\033[m.')
elif sexo == 'Masculino':
    if idad == 18:
        print(f'É hora de se \033[32malistar no exército brasileiro\033[m! Você já tem 18 anos.')
    elif idad < 18:
        temp = 18 - idad
        print(f'\033[32mEntendi\033[m! Daqui {temp} ano(s), em {atua + temp}, você deverá se \033[32malistar no exército brasileiro\033[m.')
    else:
        temp = idad - 18
        print(f'\033[31mAtenção\033[m! Você já deveria ter feito seu \033[32malistamento no exército brasileiro\033[m em {atua - temp}, há {temp} ano(s) atrás')