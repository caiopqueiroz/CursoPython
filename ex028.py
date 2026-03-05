import random
resposta = random.randint(0, 5)
pergunta = int(input('Pensei em um número de 0 a 5. Tente adivinhar qual! '))
if pergunta > 5:
    print('Qual é cara, as instruções eram simples')
if pergunta == resposta:
    print('PARABÉNS! Está certo!')
if pergunta != resposta:
    print('Tente outra vez...')