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
                texto_digitado += '\n'
            elif evento.unicode:
                texto_digitado += evento.unicode
    
    # lógica

    # desenho
    tela.fill(preto)
    imagem_texto = fonte.render(texto_digitado, True, branco)
    tela.blit(imagem_texto, (50, 200))

    # atualizações
    pygame.display.update()

    # travar fps 
    clock.tick(60)