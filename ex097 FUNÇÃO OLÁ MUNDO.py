def escr(text):
    if text == 'JÚLIA':
        print('~' * 22)
        print(f'  \033[35m{text}, EU TE AMO!!\033[m')
        print('~' * 22)
    else:
        print('~' * (len(text) + 4))
        print(f'  {text}')
        print('~' * (len(text) + 4))


text = str(input('Escreva uma frase para ser exibida no painel: ')).strip().upper()
escr(text)
segu = int(input('== PROGRAMA ENCERRADO =='))
