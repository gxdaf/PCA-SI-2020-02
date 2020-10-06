import pygame

pygame.init()

janela = pygame.display.set_mode((600,600))
nome = pygame.display.set_caption(('Manual das Ruas'))
icone = pygame.image.load('../img/img_jog_car/carro-am.png')
pygame.display.set_icon(icone)

fundo_infantil = pygame.image.load('../img/pistas/pista-pca.png')

carro_img_am = pygame.image.load('../img/img_jog_car/carro-am.png')
coord_x_am = [40, 40,  40, 40, 40, 110, 170, 260, 310, 330, 390, 440, 490, 500, 500, 500,500, 490, 440, 430, 425, 360, 300, 240, 220, 150, 100, 45, 40, 40]
coord_y_am = [250, 200, 150, 100, 40, 15, 20, 40, 50, 100, 110, 110, 110, 175, 230, 285, 340, 395, 410, 465, 520, 510, 500, 490, 440, 430, 430, 415, 360, 310]
pontos_am = 0


while True:

    janela.blit(fundo_infantil, (0, 0))

    janela.blit(carro_img_am, (coord_x_am[29], coord_y_am[29]))

    pygame.display.flip()