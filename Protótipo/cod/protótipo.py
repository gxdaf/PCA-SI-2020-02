import pygame, math, random, time

pygame.init()
pygame.font.init()

janela = pygame.display.set_mode((600,600))
nome = pygame.display.set_caption(('City Driving Guide'))
icone = pygame.image.load('../img/img_jog_car/carro-am.png')
pygame.display.set_icon(icone)

fonte_tit = pygame.font.Font('../font/PressStart2P-vaV7.ttf', 26)
fonte_botao = pygame.font.Font('../font/PressStart2P-vaV7.ttf', 12)
menu_titulo = fonte_tit.render('CITY DRIVING GUIDE', True, (255,255,255))

escolha = ''
fundo_jogo = pygame.image.load('../img/pistas/fundo.jpg')
fundo_menu = pygame.image.load('../img/pistas/fundo-intro.png')

jogadores = ['Amarelo', 'Azul']

carro_img_am = pygame.image.load('../img/img_jog_car/carro-am.png')
coord_x_am = [90, 120,  110, 60, 50, 110, 170, 190, 220, 280, 330, 390, 450, 510, 510, 510,510, 500, 450, 390, 350, 370, 410, 350, 280, 240, 190, 120, 55, 60, 90]
coord_y_am = [280, 220, 160, 110, 50, 30, 60, 130, 190, 210, 160, 120, 125, 180, 250, 320, 390, 450, 500, 490, 430, 370, 310, 290, 330, 380, 420, 440, 410, 340, 280]
pontos_am = 0

carteira_x = [30, 440]
carteira_y = [490, 30]

cart_amarela = pygame.image.load('../img/img_jog_car/cart-amarela.png')
cart_azul = pygame.image.load('../img/img_jog_car/cart-azul.png')

carro_img_az = pygame.image.load('../img/img_jog_car/carro-az.png')
coord_x_az = [90, 120,  110, 60, 50, 110, 170, 190, 220, 280, 330, 390, 450, 510, 510, 510,510, 500, 450, 390, 350, 370, 410, 350, 280, 240, 190, 120, 55, 60, 90]
coord_y_az = [280, 220, 160, 110, 50, 30, 60, 130, 190, 210, 160, 120, 125, 180, 250, 320, 390, 450, 500, 490, 430, 370, 310, 290, 330, 380, 420, 440, 410, 340, 280]
pontos_az = 0

guarda_regras = pygame.image.load('../img/img_jog_car/guarda_regras.png')
mens_menu = pygame.image.load('../img/img_jog_car/mens_box.png')
mens_box_sorteio = pygame.image.load('../img/img_jog_car/guarda_mens.png')
mens_box_buraco = pygame.image.load('../img/img_jog_car/mens_box_buraco.png')
mens_box_perg = pygame.image.load('../img/img_jog_car/mens_box_perg.png')
mens_box_am_prim = pygame.image.load('../img/img_jog_car/mens_box_am_prim.png')
mens_box_az_prim = pygame.image.load('../img/img_jog_car/mens_box_az_prim.png')

mens_box_x = 150
mens_box_y = 170

ponteiro_am = 0
ponteiro_az = 0

cart_pb = pygame.image.load('../img/img_jog_car/cart-bw.png')

menu = True
conf_audio = False
conf_tam = False
regra1 = False
regra2 = False
regra3 = False
regra4 = False
regra5 = False
regra6 = False
sorteio = False
jogo = False


mens_pos = ['Pergunta', 'Pergunta', 'Buraco!', 'Pergunta', 'Pergunta', 'Pergunta', 'Pergunta', 'Buraco!', 'Pergunta', 'Pergunta', 'Buraco!', 'Pergunta', 'Pergunta', 'Pergunta', 'Buraco!', 'Pergunta', 'Pergunta', 'Buraco!', 'Buraco!', 'Pergunta', 'Pergunta', 'Pergunta', 'Pergunta', 'Pergunta', 'Pergunta', 'Pergunta', 'Pergunta', 'Pergunta', 'Pergunta', 'Buraco!']
resp_pos = ['Resposta', 'Resposta', 'Buraco!', 'Resposta', 'Resposta', 'Resposta', 'Resposta', 'Buraco!', 'Resposta', 'Resposta', 'Buraco!', 'Resposta', 'Resposta', 'Resposta', 'Buraco!', 'Resposta', 'Resposta', 'Buraco','Buraco', 'Resposta','Resposta', 'Resposta', 'Resposta', 'Resposta', 'Resposta', 'Resposta', 'Resposta', 'Resposta', 'Resposta', 'Buraco!']

dado_am = ['../img/dados/dado-am-1.png', '../img/dados/dado-am-2.png', '../img/dados/dado-am-3.png', '../img/dados/dado-am-4.png', '../img/dados/dado-am-5.png', '../img/dados/dado-am-6.png']
dado_az = ['../img/dados/dado-az-1.png', '../img/dados/dado-az-2.png', '../img/dados/dado-az-3.png', '../img/dados/dado-az-4.png', '../img/dados/dado-az-5.png', '../img/dados/dado-az-6.png']
dado_x = 255
dado_y = 25

def dado_regra():
        dado_regra = pygame.image.load(dado_am[0])
        janela.blit(dado_regra,(dado_x, dado_y))

casas = ['uma', 'duas', 'três', 'quatro', 'cinco', 'seis']

def menu_opc():
    mouse = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pos()
    opc_jog = pygame.draw.rect(janela, (255, 255, 255), (60, 150, 200, 50))
    menu_botao1 = fonte_botao.render('COMEÇAR JOGO', True, (0, 0, 0))
    janela.blit(menu_botao1, (90, 170))
    opc_aud = pygame.draw.rect(janela, (255, 255, 255), (60, 250, 200, 50))
    menu_botao2 = fonte_botao.render('ÁUDIO', True, (0, 0, 0))
    janela.blit(menu_botao2, (130, 270))
    opc_tam = pygame.draw.rect(janela, (255, 255, 255), (60, 350, 200, 50))
    menu_botao3 = fonte_botao.render('TELA', True, (0, 0, 0))
    janela.blit(menu_botao3, (140, 370))
    opc_sair = pygame.draw.rect(janela, (255, 255, 255), (60, 450, 200, 50))
    menu_botao4 = fonte_botao.render('SAIR DO JOGO', True, (0, 0, 0))
    janela.blit(menu_botao4, (90, 470))
    if 260 > mouse[0] > 60 and 200 > mouse[1] > 150:
        opc_jog = pygame.draw.rect(janela, (0, 0, 0), (60, 150, 200, 50))
        menu_botao1 = fonte_botao.render('COMEÇAR JOGO', True, (255, 255, 255))
        janela.blit(menu_botao1, (90, 170))
    if 260 > mouse[0] > 60 and 300 > mouse[1] > 250:
        opc_aud = pygame.draw.rect(janela, (0, 0, 0), (60, 250, 200, 50))
        menu_botao2 = fonte_botao.render('ÁUDIO', True, (255, 255, 255))
        janela.blit(menu_botao2, (130, 270))
    if 260 > mouse[0] > 60 and 400 > mouse[1] > 350:
        opc_tam = pygame.draw.rect(janela, (0, 0, 0), (60, 350, 200, 50))
        menu_botao3 = fonte_botao.render('TELA', True, (255, 255, 255))
        janela.blit(menu_botao3, (140, 370))
    if 260 > mouse[0] > 60 and 500 > mouse[1] > 450:
        opc_sair = pygame.draw.rect(janela, (0, 0, 0), (60, 450, 200, 50))
        menu_botao4 = fonte_botao.render('SAIR DO JOGO', True, (255, 255, 255))
        janela.blit(menu_botao4, (90, 470))

def regra_1():
    janela.blit(guarda_regras, (0, 0))
    regra_linha1 = (fonte_botao.render('Um dado determina o número de casas', True, (0, 0, 0)))
    regra_linha2 = (fonte_botao.render('que o jogador deve percorrer a', True, (0, 0, 0)))
    regra_linha3 = (fonte_botao.render('cada jogada.', True, (0, 0, 0)))
    espaco = fonte_botao.render('Aperte espaço para continuar', True, (0,0,0))
    janela.blit(regra_linha1, (50, 400))
    janela.blit(regra_linha2, (50, 425))
    janela.blit(regra_linha3, (50, 450))
    janela.blit(espaco, (80, 490))

def regra_2():
    janela.blit(guarda_regras, (0, 0))
    regra_linha1 = (fonte_botao.render('Limite de 40 pontos na habilitação.', True, (0, 0, 0)))
    regra_linha2 = (fonte_botao.render('O jogador que chegar a essa', True, (0, 0, 0)))
    regra_linha3 = (fonte_botao.render('quantidade automaticamente perde.', True, (0, 0, 0)))
    espaco = fonte_botao.render('Aperte espaço para continuar', True, (0,0,0))
    janela.blit(regra_linha1, (50, 400))
    janela.blit(regra_linha2, (50, 425))
    janela.blit(regra_linha3, (50, 450))
    janela.blit(espaco, (80, 490))

def regra_3():
    janela.blit(guarda_regras, (0, 0))
    regra_linha1 = (fonte_botao.render('Ganha o jogador que percorrer todo', True, (0, 0, 0)))
    regra_linha2 = (fonte_botao.render('o tabuleiro e garantir a menor', True, (0, 0, 0)))
    regra_linha3 = (fonte_botao.render('pontuação de infrações.', True, (0, 0, 0)))
    regra_linha4 = (fonte_botao.render('Ou seja, acertar mais perguntas.', True, (0, 0, 0)))
    espaco = fonte_botao.render('Aperte espaço para continuar', True, (0, 0, 0))
    janela.blit(regra_linha1, (50, 395))
    janela.blit(regra_linha2, (50, 420))
    janela.blit(regra_linha3, (50, 445))
    janela.blit(regra_linha4, (50, 470))
    janela.blit(espaco, (80, 500))

def regra_4():
    janela.blit(guarda_regras, (0, 0))
    regra_linha1 = (fonte_botao.render('As pontes permitem que o jogador', True, (0, 0, 0)))
    regra_linha2 = (fonte_botao.render('avance no tabuleiro', True, (0, 0, 0)))
    regra_linha3 = (fonte_botao.render('cortando caminho. Ou seja,', True, (0, 0, 0)))
    regra_linha4 = (fonte_botao.render('acertar mais perguntas.', True, (0, 0, 0)))
    espaco = fonte_botao.render('Aperte espaço para continuar', True, (0, 0, 0))
    janela.blit(regra_linha1, (50, 400))
    janela.blit(regra_linha2, (50, 425))
    janela.blit(regra_linha3, (50, 450))
    janela.blit(regra_linha4, (50, 475))
    janela.blit(espaco, (80, 500))

def regra_5():
    janela.blit(guarda_regras, (0, 0))
    regra_linha1 = (fonte_botao.render('O jogador que cair no buraco na', True, (0, 0, 0)))
    regra_linha2 = (fonte_botao.render('estrada deverá ficar uma', True, (0, 0, 0)))
    regra_linha3 = (fonte_botao.render('rodada sem jogar.', True, (0, 0, 0)))
    espaco = fonte_botao.render('Aperte espaço para continuar', True, (0, 0, 0))
    janela.blit(regra_linha1, (50, 400))
    janela.blit(regra_linha2, (50, 425))
    janela.blit(regra_linha3, (50, 450))
    janela.blit(espaco, (80, 500))

def regra_6():
    janela.blit(guarda_regras, (0, 0))
    regra_linha1 = (fonte_botao.render('O tabuleiro conta com uma série de ', True, (0, 0, 0)))
    regra_linha2 = (fonte_botao.render('perguntas sobre regras de', True, (0, 0, 0)))
    regra_linha3 = (fonte_botao.render('trânsito, divididas em 4 níveis', True, (0, 0, 0)))
    regra_linha4 = (fonte_botao.render('e infrações, marcadas pelas', True, (0, 0, 0)))
    regra_linha5 = (fonte_botao.render('cores das placas.', True, (0, 0, 0)))
    espaco = fonte_botao.render('Aperte espaço para continuar', True, (0, 0, 0))
    janela.blit(regra_linha1, (50, 390))
    janela.blit(regra_linha2, (50, 415))
    janela.blit(regra_linha3, (50, 440))
    janela.blit(regra_linha4, (50, 465))
    janela.blit(regra_linha5, (50, 490))
    janela.blit(espaco, (80, 500))

def menu_txt():
    janela.blit(menu_titulo, (70,70))

def placas():
    placaazul = pygame.image.load('../img/img_jog_car/placaazul.png')
    placaverde = pygame.image.load('../img/img_jog_car/placaverde.png')
    placaamarela = pygame.image.load('../img/img_jog_car/placaamarela.png')
    placavermelha = pygame.image.load('../img/img_jog_car/placavermelha.png')
    janela.blit(placaazul, (100,100))
    janela.blit(placaverde, (250, 100))
    janela.blit(placaamarela, (100, 200))
    janela.blit(placavermelha, (250, 200))

def carro_jog_az():
    janela.blit(carro_img_az, (coord_x_az[ponteiro_az], coord_y_az[ponteiro_az]))

def carro_jog_am():
    janela.blit(carro_img_am, (coord_x_am[ponteiro_am], coord_y_am[ponteiro_am]))

def carteira_amarela():
    janela.blit(cart_amarela, (carteira_x[0],carteira_y[0]))

def carteira_azul():
    janela.blit(cart_azul, (carteira_x[1], carteira_y[1]))

def carteira_cinza():
    janela.blit(cart_pb, (carteira_x[x],carteira_y[y]))

def mens_txt_sort():
    janela.blit(mens_box_sorteio,(0,0))

def mens_txt_buraco():
    janela.blit(mens_box_buraco, (mens_box_x, mens_box_y))

def mens_txt_perg():
    janela.blit(mens_box_perg, (mens_box_x, mens_box_y))

def mens_txt_am_prim():
    janela.blit(mens_box_am_prim,(mens_box_x,mens_box_y))

def mens_txt_az_prim():
    janela.blit(mens_box_az_prim, (mens_box_x,mens_box_y))

pygame.display.flip()

while True:

    escolha = random.choice(jogadores)

    while menu:
        janela.blit(fundo_menu, (0, 0))
        menu_txt()
        menu_opc()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if event.button == pygame.BUTTON_LEFT and 260 > mouse[0] > 60 and 200 > mouse[1] > 150:
                    menu = False
                    regra1 = True
                if event.button == pygame.BUTTON_LEFT and 260 > mouse[0] > 60 and 300 > mouse[1] > 250:
                    janela.blit(mens_menu, (250, 200))
                if event.button == pygame.BUTTON_LEFT and 260 > mouse[0] > 60 and 400 > mouse[1] > 350:
                    janela.blit(mens_menu, (250, 200))
                if event.button == pygame.BUTTON_LEFT and 260 > mouse[0] > 60 and 500 > mouse[1] > 450:
                    pygame.quit()

        pygame.display.update()

    while regra1:
        janela.blit(fundo_jogo, (0, 0))
        pygame.draw.rect(janela, (255, 0, 0), (253, dado_y, 50, 50))
        dado_regra()
        regra_1()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    regra1 = False
                    regra2 = True

        pygame.display.update()

    while regra2:
        janela.blit(fundo_jogo, (0, 0))
        dado_regra()
        pygame.draw.rect(janela, (255, 0, 0), (carteira_x[1], carteira_y[1], 127, 90))
        carteira_azul()
        regra_2()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    regra2 = False
                    regra3 = True

        pygame.display.update()

    while regra3:
        janela.blit(fundo_jogo, (0, 0))
        dado_regra()
        carteira_azul()
        regra_3()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    regra3 = False
                    regra4 = True

        pygame.display.update()

    while regra4:
        janela.blit(fundo_jogo, (0, 0))
        dado_regra()
        carteira_azul()
        regra_4()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    regra4 = False
                    regra5 = True

        pygame.display.update()

    while regra5:
        janela.blit(fundo_jogo, (0, 0))
        dado_regra()
        carteira_azul()
        regra_5()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    regra5 = False
                    regra6 = True

        pygame.display.update()

    while regra6:
        janela.blit(fundo_jogo, (0, 0))
        dado_regra()
        carteira_azul()
        placas()
        regra_6()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    regra6 = False

        pygame.display.flip()


    mens_txt_sort()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sorteio = True
                print('O primeiro a jogar será o: {}! Aperte espaço para jogar o dado.'.format(escolha))

    pygame.display.flip()

    while sorteio:

        janela.blit(fundo_jogo, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
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
                    dado_am_vez = pygame.image.load(dado_am[dado - 1])
                    janela.blit(dado_am_vez, (dado_x, dado_y))
                    pygame.display.update()
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
                    dado_az_vez = pygame.image.load(dado_az[dado - 1])
                    janela.blit(dado_az_vez, (dado_x, dado_y))
                    pygame.display.flip()
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

        pygame.display.flip()
