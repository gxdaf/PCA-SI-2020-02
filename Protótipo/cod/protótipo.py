import pygame, math, random

pygame.init()
pygame.font.init()

janela = pygame.display.set_mode((600,600))
nome = pygame.display.set_caption(('City Driving Guide'))
icone = pygame.image.load('../img/img_jog_car/carro-am.png')
pygame.display.set_icon(icone)

fundo_jogo = pygame.image.load('../img/pistas/fundo.jpg')
fundo_sorteio = pygame.image.load('../img/pistas/fundo-intro.png')

jogadores = ['Amarelo', 'Azul']

carro_img_am = pygame.image.load('../img/img_jog_car/carro-am.png')
coord_x_am = [90, 120,  110, 60, 50, 110, 170, 190, 220, 280, 330, 390, 450, 510, 510, 510,510, 500, 450, 390, 350, 370, 410, 350, 280, 240, 190, 120, 55, 60, 90]
coord_y_am = [280, 220, 160, 110, 50, 30, 60, 130, 190, 210, 160, 120, 125, 180, 250, 320, 390, 450, 500, 490, 430, 370, 310, 290, 330, 380, 420, 440, 410, 340, 280]
pontos_am = 0

cart_amarela = pygame.image.load('../img/img_jog_car/cart-amarela.png')
cart_am_x = 30
cart_am_y = 490

carro_img_az = pygame.image.load('../img/img_jog_car/carro-az.png')
coord_x_az = [90, 120,  110, 60, 50, 110, 170, 190, 220, 280, 330, 390, 450, 510, 510, 510,510, 500, 450, 390, 350, 370, 410, 350, 280, 240, 190, 120, 55, 60, 90]
coord_y_az = [280, 220, 160, 110, 50, 30, 60, 130, 190, 210, 160, 120, 125, 180, 250, 320, 390, 450, 500, 490, 430, 370, 310, 290, 330, 380, 420, 440, 410, 340, 280]
pontos_az = 0

cart_azul = pygame.image.load('../img/img_jog_car/cart-azul.png')
cart_az_x = 440
cart_az_y = 30

ponteiro_am = 0
ponteiro_az = 0

sorteio = True
jogo = False

mens_pos = ['Pergunta', 'Pergunta', 'Buraco!', 'Pergunta', 'Pergunta', 'Pergunta', 'Pergunta', 'Buraco!', 'Pergunta', 'Pergunta', 'Buraco!', 'Pergunta', 'Pergunta', 'Pergunta', 'Buraco!', 'Pergunta', 'Pergunta', 'Buraco!', 'Buraco!', 'Pergunta', 'Pergunta', 'Pergunta', 'Pergunta', 'Pergunta', 'Pergunta', 'Pergunta', 'Pergunta', 'Pergunta', 'Pergunta', 'Buraco!']
resp_pos = ['Resposta', 'Resposta', 'Buraco!', 'Resposta', 'Resposta', 'Resposta', 'Resposta', 'Buraco!', 'Resposta', 'Resposta', 'Buraco!', 'Resposta', 'Resposta', 'Resposta', 'Buraco!', 'Resposta', 'Resposta', 'Buraco','Buraco', 'Resposta','Resposta', 'Resposta', 'Resposta', 'Resposta', 'Resposta', 'Resposta', 'Resposta', 'Resposta', 'Resposta', 'Buraco!']

dado_am = ['../img/dados/dado-am-1.png', '../img/dados/dado-am-2.png', '../img/dados/dado-am-3.png', '../img/dados/dado-am-4.png', '../img/dados/dado-am-5.png', '../img/dados/dado-am-6.png']
dado_az = ['../img/dados/dado-az-1.png', '../img/dados/dado-az-2.png', '../img/dados/dado-az-3.png', '../img/dados/dado-az-4.png', '../img/dados/dado-az-5.png', '../img/dados/dado-az-6.png']
dado_x = 255
dado_y = 25

casas = ['uma', 'duas', 'três', 'quatro', 'cinco', 'seis']

def carro_jog_az():
    janela.blit(carro_img_az, (coord_x_az[ponteiro_az], coord_y_az[ponteiro_az]))

def carro_jog_am():
    janela.blit(carro_img_am, (coord_x_am[ponteiro_am], coord_y_am[ponteiro_am]))

def carteira_amarela ():
    janela.blit(cart_amarela, (cart_am_x,cart_am_y))

def carteira_azul():
    janela.blit(cart_azul, (cart_az_x, cart_az_y))

pygame.display.flip()

while True:

    while sorteio:
        janela.blit(fundo_sorteio, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.VIDEOEXPOSE:
                print('Aperte espaço para sortear!')
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    escolha = random.choice(jogadores)
                    print('O primeiro a jogar será o: {}! Aperte espaço para jogar o dado.'.format(escolha))
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    sorteio = False
                    jogo = True

        pygame.display.update()

    while jogo:

        janela.blit(fundo_jogo, (0, 0))
        carro_jog_am()
        carro_jog_az()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and escolha == 'Amarelo':
                    dado = random.randint(1, 6)
                    ponteiro_am += dado
                    coord_x_am[(ponteiro_am)]
                    coord_y_am[(ponteiro_am)]
                    dado_am_vez = pygame.image.load(dado_am[dado - 1])
                    janela.blit(dado_am_vez, (dado_x, dado_y))
                    status_casa = mens_pos[ponteiro_am]
                    if dado == 1:
                        print('Você andou uma casa!')
                    else:
                        print('Você andou {} casas!'.format(casas[dado - 1]))

                    if 'Buraco!' in status_casa:
                        print('Você caiu no buraco! Vez do Azul.')
                        escolha = 'Azul'
                    else:
                        print(mens_pos[ponteiro_am])
                        resposta = input('Digite aqui a resposta:')
                        resposta = resposta.title()
                        if resposta in resp_pos[ponteiro_am]:
                            prox_part = print('Você acertou! Jogue novamente.')
                            escolha = 'Amarelo'
                        else:
                            pontos_am += 1
                            print('Você errou e agora tem {} pontos na carteira! Vez do Azul.'.format(pontos_am))
                            escolha = 'Azul'
                elif event.key == pygame.K_SPACE and escolha == 'Azul':
                    dado = random.randint(1, 6)
                    ponteiro_az += dado
                    coord_x_az[(ponteiro_az)]
                    coord_y_az[(ponteiro_az)]
                    dado_az_vez = pygame.image.load(dado_az[dado - 1])
                    janela.blit(dado_az_vez, (dado_x, dado_y))
                    status_casa = mens_pos[ponteiro_az]
                    if dado == 1:
                        print('Você andou uma casa!')
                    else:
                        print('Você andou {} casas!'.format(casas[dado - 1]))
                    if 'Buraco' in status_casa:
                        print('Você caiu no buraco! Vez do Amarelo.')
                        escolha = 'Amarelo'
                    else:
                        print(mens_pos[ponteiro_az])
                        resposta = input('Digite aqui a resposta:')
                        resposta = resposta.title()
                        if resposta in resp_pos[ponteiro_az]:
                            print('Você acertou!')
                            escolha = 'Azul'
                        else:
                            pontos_az += 1
                            print('Você errou e agora tem {} pontos na carteira! Vez do Amarelo.'.format(pontos_az))
                            escolha = 'Amarelo'


        carteira_amarela()
        carteira_azul()

        pygame.display.update()
