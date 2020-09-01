import pygame, math, random

pygame.init()
pygame.font.init()

janela = pygame.display.set_mode((600,600))
nome = pygame.display.set_caption(('City Driving Guide'))
icone = pygame.image.load('../img/img_jog_car/carro-am.png')
pygame.display.set_icon(icone)

fundo = pygame.image.load('../img/pistas/fundo.jpg')

carro_img_am = pygame.image.load('../img/img_jog_car/carro-am.png')
coord_x_am = [90, 120,  110, 60, 50, 110, 170, 190, 220, 280, 330, 390, 450, 510, 510, 510,510, 500, 450, 390, 350, 370, 410, 350, 280, 240, 190, 120, 55, 60, 90]
coord_y_am = [280, 220, 160, 110, 50, 30, 60, 130, 190, 210, 160, 120, 125, 180, 250, 320, 390, 450, 500, 490, 430, 370, 310, 290, 330, 380, 420, 440, 410, 340, 280]
pontos_am = 0

carro_img_az = pygame.image.load('../img/img_jog_car/carro-az.png')
coord_x_az = [90, 120,  110, 60, 50, 110, 170, 190, 220, 280, 330, 390, 450, 510, 510, 510,510, 500, 450, 390, 350, 370, 410, 350, 280, 240, 190, 120, 55, 60, 90]
coord_y_az = [280, 220, 160, 110, 50, 30, 60, 130, 190, 210, 160, 120, 125, 180, 250, 320, 390, 450, 500, 490, 430, 370, 310, 290, 330, 380, 420, 440, 410, 340, 280]
pontos_az = 0

ponteiro_am = 0
ponteiro_az = 0

perg_pos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '@', '!', '?', '*']
resp_pos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '@', '!', '?', '*']

dado_am = ['../img/dados/dado-am-1.png', '../img/dados/dado-am-2.png', '../img/dados/dado-am-3.png', '../img/dados/dado-am-4.png', '../img/dados/dado-am-5.png', '../img/dados/dado-am-6.png']
dado_az = ['../img/dados/dado-az-1.png', '../img/dados/dado-az-2.png', '../img/dados/dado-az-3.png', '../img/dados/dado-az-4.png', '../img/dados/dado-az-5.png', '../img/dados/dado-az-6.png']
dado_x = 255
dado_y = 25

casas = ['uma', 'duas', 'três', 'quatro', 'cinco', 'seis']

def carro_jog_am():
    janela.blit(carro_img_am, (coord_x_am[int(ponteiro_am)], coord_y_am[int(ponteiro_am)]))

def carro_jog_az():
    janela.blit(carro_img_az, (coord_x_az[int(ponteiro_az)], coord_y_az[int(ponteiro_az)]))

pygame.display.flip()

while True:

    janela.blit(fundo, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dado = random.randint(1, 6)
                ponteiro_am  += dado
                coord_x_am[ponteiro_am]
                coord_y_am[ponteiro_am]
                dado_am_vez = pygame.image.load(dado_am[dado - 1])
                janela.blit(dado_am_vez, (dado_x, dado_y))
                if dado == 1:
                    print('Você andou uma casa!')
                else:
                    print('Você andou {} casas!'.format(casas[dado-1]))
            if event.key == pygame.K_TAB:
                dado = random.randint(1,6)
                ponteiro_az += dado
                coord_x_az[ponteiro_az]
                coord_y_az[ponteiro_az]
                dado_az_vez = pygame.image.load(dado_az[dado - 1])
                janela.blit(dado_az_vez, (dado_x, dado_y))
                if dado == 1:
                    print('Você andou uma casa!')
                else:
                    print('Você andou {} casas!'.format(casas[dado-1]))

        carro_jog_am()
        carro_jog_az()


        pygame.display.update()