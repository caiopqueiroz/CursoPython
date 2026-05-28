import pygame 
import sys

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Buscador de arquivos')
clock = pygame.time.Clock()
preto = (0, 0, 0)
branco = (255, 255, 255)
fonte = pygame.font.SysFont(None, 48)

texto_digitado = ''
aparecer_texto = False
caminhos = ['buscador_arquivos/teste.txt', 'buscador_arquivos/outro_teste.txt', '../VisualizaçãoDados/Linguagem R.txt', '../../Caio/Ideias/Buscador de arquivos.txt']
encontrou = False
escrever_frase = False
fim_linha = True
ultima_linha = False
linhas_arquivos = list()
contador = 0
contador_arquivo = -1

while True:
    # eventos 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                texto_digitado = texto_digitado[:-1]
            # enter não quebra a linha 
            elif evento.key == pygame.K_RETURN:
                comando = texto_digitado
                texto_digitado = ''
                aparecer_texto = True
            elif evento.unicode:
                texto_digitado += evento.unicode
    
    # lógica

    # desenho
    tela.fill(preto)
    imagem_texto = fonte.render(texto_digitado, True, branco)
    tela.blit(imagem_texto, (50, 200))
    if aparecer_texto:
        for elemento in caminhos:
            caminho = elemento
            arquivo = open(caminho, 'rt', encoding='utf-8')
            titulo = caminho.split('/')
            
            for elemento in titulo:
                if comando in elemento:
                    #print(f'\nExiste um arquivo com esse nome - \033[34m{caminho}\033[m')
                    pass

        for elemento in caminhos:
            caminho = elemento
            arquivo = open(caminho, 'rt', encoding='utf-8')
            contador_linhas = 0
            linha_atual = 0

            for linha in arquivo:
                contador_linhas += 1

            linhas_arquivos.append(contador_linhas)

        for elemento in caminhos:
            caminho = elemento
            arquivo = open(caminho, 'rt', encoding='utf-8')
            contador_arquivo += 1
            linha_atual = 0

            for linha in arquivo:
                linha_atual += 1
                if linha_atual == linhas_arquivos[contador_arquivo]:
                    ultima_linha = True
                else:
                    ultima_linha = False
                palavras = linha.split(' ')
                contador_palavras = 0

                for palavra in palavras:
                    if palavra == '\n':
                        palavras.remove(palavra)

                    if '\n' in palavra:
                        if palavra in palavras:
                            palavra_corrigida = palavra.split('\n')
                            palavras.remove(palavra)
                            palavras.append(palavra_corrigida[0])        
                
                for palavra in palavras:
                    contador_palavras += 1

                    if comando in palavra:
                        frase = list()
                        contador = 0
                        escrever_frase = True
                        encontrou = True
                        fim_linha = False
                        local = caminho
                        #print(f'\nEncontrei essa palavra no arquivo \033[32m{caminho}\033[m')
                    
                    if not fim_linha:
                        if escrever_frase:
                            if contador <= 5:
                                frase.append(palavra)
                                contador += 1

                    if contador_palavras == len(palavras):
                        if ultima_linha == True:
                            fim_linha = True
                            if escrever_frase:
                                for elemento in frase:
                                    previa = fonte.render(elemento, True, branco)
                                    mostrar_previa = tela.blit(previa, (50, 250))
                                #print('Prévia: ', end='')
                                #for elemento in frase:
                                    # escrever frase
                                escrever_frase = False
                    if contador > 5:
                        fim_linha = True
                        if escrever_frase:
                            frase_procurada = ''
                            for elemento in frase:
                                frase_procurada += f' {elemento}'
                            previa = fonte.render(frase_procurada, True, branco)
                            mostrar_previa = tela.blit(previa, (50, 250))
                            #print('Prévia: ', end='')
                            #for elemento in frase:
                                # escrever frase
                            escrever_frase = False

        if not encontrou:
            print('\n\033[31mNão encontrei essa palavra em nenhum arquivo\033[m')

    # atualizações
    pygame.display.update()

    # travar fps 
    clock.tick(60)