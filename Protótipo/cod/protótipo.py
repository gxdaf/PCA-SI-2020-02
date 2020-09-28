import pygame, math, random, time
from pygame import mixer


pygame.init()
pygame.font.init()


#Configurações da janela
janela = pygame.display.set_mode((600,600))
nome = pygame.display.set_caption(('Manual das Ruas'))
icone = pygame.image.load('../img/img_jog_car/carro-am.png')
pygame.display.set_icon(icone)

#Imagens de fundo
fundo_menu = pygame.image.load('../img/pistas/fundo-intro.png')
fundo_infantil = pygame.image.load('../img/pistas/fundo.jpg')
fundo_adulto = pygame.image.load('../img/pistas/pista_dois.jpg')
fundo_intro = pygame.image.load('../img/img_jog_car/fundo_estradinha.png')

#Imagens complementares
mutar = pygame.image.load('../img/img_jog_car/mutar.png')
mutar_mouse = pygame.image.load('../img/img_jog_car/mutar_branco.png')
botao_volta = pygame.image.load('../img/img_jog_car/botao_volta.png')

#Fontes
fonte_tit = pygame.font.Font('../font/PressStart2P-vaV7.ttf', 26)
fonte_botao = pygame.font.Font('../font/PressStart2P-vaV7.ttf', 12)

#Introdução do jogo
buzina = mixer.Sound('../audio/buzina_intro.wav')
motor = mixer.Sound('../audio/motor_abertura.wav')
musica_infantil = mixer.music.load('../audio/signal_8bit.wav')
musica_adulto = mixer.music.load('../audio/whatislove_8bit.wav')
titulo_intro_x = 70
titulo_intro_y = 300
carro_intro = pygame.image.load('../img/img_jog_car/carro_intro.png')
carro_intro_x = 0
carro_intro_y = 460
menu_titulo = fonte_tit.render('MANUAL DAS RUAS', True, (255, 255, 255))


escolha = ''

jogadores = ['Amarelo', 'Azul']

#Coordenadas da carteira
carteira_x = [30, 440]
carteira_y = [490, 30]

#Jogador amarelo
carro_img_am = pygame.image.load('../img/img_jog_car/carro-am.png')
coord_x_am = [90, 120,  110, 60, 50, 110, 170, 190, 220, 280, 330, 390, 450, 510, 510, 510,510, 500, 450, 390, 350, 370, 410, 350, 280, 240, 190, 120, 55, 60, 90]
coord_y_am = [280, 220, 160, 110, 50, 30, 60, 130, 190, 210, 160, 120, 125, 180, 250, 320, 390, 450, 500, 490, 430, 370, 310, 290, 330, 380, 420, 440, 410, 340, 280]
pontos_am = 0
cart_amarela = pygame.image.load('../img/img_jog_car/cart-amarela.png')

#Jogador azul
carro_img_az = pygame.image.load('../img/img_jog_car/carro-az.png')
coord_x_az = [90, 120,  110, 60, 50, 110, 170, 190, 220, 280, 330, 390, 450, 510, 510, 510,510, 500, 450, 390, 350, 370, 410, 350, 280, 240, 190, 120, 55, 60, 90]
coord_y_az = [280, 220, 160, 110, 50, 30, 60, 130, 190, 210, 160, 120, 125, 180, 250, 320, 390, 450, 500, 490, 430, 370, 310, 290, 330, 380, 420, 440, 410, 340, 280]
pontos_az = 0
cart_azul = pygame.image.load('../img/img_jog_car/cart-azul.png')

#Caixas de testo
mens_box = pygame.image.load('../img/img_jog_car/mens_box.png')
mens_box_sorteio = pygame.image.load('../img/img_jog_car/guarda_mens.png')
mens_box_buraco = pygame.image.load('../img/img_jog_car/mens_box_buraco.png')
guarda_regras = pygame.image.load('../img/img_jog_car/guarda_regras.png')

#Coordenadas da caixa de texto
mens_box_x = 150
mens_box_y = 170

#Ponteiro das casas guiadas a dado
ponteiro_am = 0
ponteiro_az = 0

#Etapas do programa

creditos = False
abertura = True
intro = False
menu = False
audio = True
escolha_modo = False
modo_infantil = False
modo_adulto = False
conf_audio = False
conf_tam = False
regra1 = False
regra2 = False
regra3 = False
regra4 = False
regra5 = False
regra6 = False
sorteio = False
jogo_infantil = False
jogo_adulto = False

#Configuração das casas
mens_pos = ['Pergunta', 'Pergunta', 'Buraco!', 'Ponte', 'Pergunta', 'Pergunta', 'Pergunta', 'Buraco!', 'Pergunta', 'Pergunta', 'Buraco!', 'Pergunta', 'Pergunta', 'Pergunta', 'Buraco!', 'Pergunta', 'Ponte', 'Buraco!', 'Buraco!', 'Pergunta', 'Ponte', 'Pergunta', 'Ponte', 'Pergunta', 'Pergunta', 'Pergunta', 'Pergunta', 'Pergunta', 'Pergunta', 'Buraco!']
resp_pos = ['Resposta', 'Resposta', 'Buraco!', 'Resposta', 'Resposta', 'Resposta', 'Resposta', 'Buraco!', 'Resposta', 'Resposta', 'Buraco!', 'Resposta', 'Resposta', 'Resposta', 'Buraco!', 'Resposta', 'Resposta', 'Buraco','Buraco', 'Resposta','Resposta', 'Resposta', 'Resposta', 'Resposta', 'Resposta', 'Resposta', 'Resposta', 'Resposta', 'Resposta', 'Buraco!']

#Dado
dado_am = ['../img/dados/dado-am-1.png', '../img/dados/dado-am-2.png', '../img/dados/dado-am-3.png', '../img/dados/dado-am-4.png', '../img/dados/dado-am-5.png', '../img/dados/dado-am-6.png']
dado_az = ['../img/dados/dado-az-1.png', '../img/dados/dado-az-2.png', '../img/dados/dado-az-3.png', '../img/dados/dado-az-4.png', '../img/dados/dado-az-5.png', '../img/dados/dado-az-6.png']
dado_x = 255
dado_y = 25

#Número de casas percorridas
casas = ['uma', 'duas', 'três', 'quatro', 'cinco', 'seis']

def dado_regra():
    dado_regra = pygame.image.load(dado_am[0])
    janela.blit(dado_regra,(dado_x, dado_y))


#Opções do menu
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

#Escolha dos modos
def escolha_txt():
    escolha_txt = fonte_botao.render('ESCOLHA UM DOS MODOS', True, (255, 255, 255))
    janela.blit(escolha_txt, (190, 150))

#Texto da introdução
def intro_txt():
    janela.blit(menu_titulo, (titulo_intro_x, titulo_intro_y))

#Modos do jogo
def modos_jogo():
    mouse = pygame.mouse.get_pos()
    janela.blit(botao_volta, (520, 523))
    jog_modo_inf = pygame.draw.rect(janela, (255, 255, 255), (90, 300, 200, 50))
    opc_inf = fonte_botao.render('INFANTIL', True, (0, 0, 0))
    janela.blit(opc_inf, (145, 320))
    jog_modo_ad = pygame.draw.rect(janela, (255, 255, 255), (320, 300, 200, 50))
    opc_ad = fonte_botao.render('ADULTO', True, (0, 0, 0))
    janela.blit(opc_ad, (390, 320))
    if 290 > mouse [0] > 90 and 350 > mouse [1] > 300:
        jog_modo_inf = pygame.draw.rect(janela, (0, 0, 0), (90, 300, 200, 50))
        opc_inf = fonte_botao.render('INFANTIL', True, (255, 255, 255))
        janela.blit(opc_inf, (145, 320))
    elif 520 > mouse [0] > 320 and 350 > mouse[1] > 300:
        jog_modo_ad = pygame.draw.rect(janela, (0, 0, 0), (320, 300, 200, 50))
        opc_ad = fonte_botao.render('ADULTO', True, (255, 255, 255))
        janela.blit(opc_ad, (390, 320))

#Configurações de áudio
def opc_mutar():
    mouse = pygame.mouse.get_pos()
    borda = pygame.draw.rect(janela, (0,0,0), (335,245,200,60))
    config_aud = pygame.draw.rect(janela, (255, 255, 255), (340, 250, 190, 50))
    aud_mute = fonte_botao.render('MUTAR', False, (0, 0, 0))
    janela.blit(aud_mute, (400, 270))
    if 530 > mouse[0] > 340 and 300 > mouse[1] > 250:
        borda = pygame.draw.rect(janela, (255, 255, 255), (335, 245, 200, 60))
        config_aud = pygame.draw.rect(janela, (0, 0, 0), (340, 250, 190, 50))
        aud_mute = fonte_botao.render('MUTAR', True, (255, 255, 255))
        janela.blit(aud_mute, (400, 270))

def botao_mutar():
    mouse = pygame.mouse.get_pos()
    janela.blit(mutar, (520,10))
    if 600 > mouse[0] > 520 and 90 > mouse[1] > 10:
        janela.blit(mutar_mouse, (520, 10))

#Regras do modo infantil
def regra_infantil_1():
    janela.blit(guarda_regras, (0, 0))
    regra_linha1 = (fonte_botao.render('Um dado determina o número de casas', True, (0, 0, 0)))
    regra_linha2 = (fonte_botao.render('que o jogador deve percorrer a', True, (0, 0, 0)))
    regra_linha3 = (fonte_botao.render('cada jogada.', True, (0, 0, 0)))
    espaco = fonte_botao.render('Aperte espaço para continuar', True, (0,0,0))
    janela.blit(regra_linha1, (50, 400))
    janela.blit(regra_linha2, (50, 425))
    janela.blit(regra_linha3, (50, 450))
    janela.blit(espaco, (80, 490))

def regra_infantil_2():
    janela.blit(guarda_regras, (0, 0))
    regra_linha1 = (fonte_botao.render('Limite de 40 pontos na habilitação.', True, (0, 0, 0)))
    regra_linha2 = (fonte_botao.render('O jogador que chegar a essa', True, (0, 0, 0)))
    regra_linha3 = (fonte_botao.render('quantidade automaticamente perde.', True, (0, 0, 0)))
    espaco = fonte_botao.render('Aperte espaço para continuar', True, (0,0,0))
    janela.blit(regra_linha1, (50, 400))
    janela.blit(regra_linha2, (50, 425))
    janela.blit(regra_linha3, (50, 450))
    janela.blit(espaco, (80, 490))

def regra_infantil_3():
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

def regra_infantil_4():
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

def regra_infantil_5():
    janela.blit(guarda_regras, (0, 0))
    regra_linha1 = (fonte_botao.render('O jogador que cair no buraco na', True, (0, 0, 0)))
    regra_linha2 = (fonte_botao.render('estrada deverá ficar uma', True, (0, 0, 0)))
    regra_linha3 = (fonte_botao.render('rodada sem jogar.', True, (0, 0, 0)))
    espaco = fonte_botao.render('Aperte espaço para continuar', True, (0, 0, 0))
    janela.blit(regra_linha1, (50, 400))
    janela.blit(regra_linha2, (50, 425))
    janela.blit(regra_linha3, (50, 450))
    janela.blit(espaco, (80, 500))

def regra_infantil_6():
    janela.blit(guarda_regras, (0, 0))
    regra_linha1 = (fonte_botao.render('O tabuleiro conta com uma série de', True, (0, 0, 0)))
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

#Regras do modo adulto
def regra_adulto_1():
    janela.blit(mens_box, (150, 150))
    regra_linha1 = (fonte_botao.render('Um dado determina', True, (0, 0, 0)))
    regra_linha2 = (fonte_botao.render('o número de casas', True, (0, 0, 0)))
    regra_linha3 = (fonte_botao.render('que o jogador', True, (0, 0, 0)))
    regra_linha4 = (fonte_botao.render('deve percorrer a', True, (0, 0, 0)))
    regra_linha5 = (fonte_botao.render('cada jogada.', True, (0, 0, 0)))
    espaco = fonte_botao.render('Aperte espaço', True, (0, 0, 0))
    espaco_2 = fonte_botao.render('para continuar', True, (0, 0, 0))
    janela.blit(regra_linha1, (205, 215))
    janela.blit(regra_linha2, (205, 240))
    janela.blit(regra_linha3, (235, 265))
    janela.blit(regra_linha4, (210, 290))
    janela.blit(regra_linha5, (240, 315))
    janela.blit(espaco, (235, 350))
    janela.blit(espaco_2, (230, 375))

def regra_adulto_2():
    janela.blit(mens_box, (150, 150))
    regra_linha1 = (fonte_botao.render('Limite de 40 pontos', True, (0, 0, 0)))
    regra_linha2 = (fonte_botao.render('na habilitação. O jo-', True, (0, 0, 0)))
    regra_linha3 = (fonte_botao.render('gador que chegar a', True, (0, 0, 0)))
    regra_linha4 = (fonte_botao.render('essa quantidade perde', True, (0, 0, 0)))
    regra_linha5 = (fonte_botao.render('automaticamente.', True, (0, 0, 0)))
    espaco = fonte_botao.render('Aperte espaço', True, (0, 0, 0))
    espaco_2 = fonte_botao.render('para continuar', True, (0, 0, 0))
    janela.blit(regra_linha1, (200, 215))
    janela.blit(regra_linha2, (190, 240))
    janela.blit(regra_linha3, (200, 265))
    janela.blit(regra_linha4, (185, 290))
    janela.blit(regra_linha5, (225, 315))
    janela.blit(espaco, (235, 350))
    janela.blit(espaco_2, (230, 375))

def regra_adulto_3():
    janela.blit(mens_box, (150, 150))
    regra_linha1 = (fonte_botao.render('Ganha o jogador que', True, (0, 0, 0)))
    regra_linha2 = (fonte_botao.render('percorrer todo o ta-', True, (0, 0, 0)))
    regra_linha3 = (fonte_botao.render('buleiro e garantir a', True, (0, 0, 0)))
    regra_linha4 = (fonte_botao.render('menor pontuação de in-', True, (0, 0, 0)))
    regra_linha5 = (fonte_botao.render('frações. Ou seja, a-', True, (0, 0, 0)))
    regra_linha6 = (fonte_botao.render('certar mais perguntas.', True, (0, 0, 0)))
    espaco = fonte_botao.render('Aperte espaço', True, (0, 0, 0))
    espaco_2 = fonte_botao.render('para continuar', True, (0, 0, 0))
    janela.blit(regra_linha1, (200, 200))
    janela.blit(regra_linha2, (190, 225))
    janela.blit(regra_linha3, (200, 250))
    janela.blit(regra_linha4, (185, 275))
    janela.blit(regra_linha5, (195, 300))
    janela.blit(regra_linha6, (185, 325))
    janela.blit(espaco, (235, 350))
    janela.blit(espaco_2, (230, 375))

def regra_adulto_4():
    janela.blit(mens_box, (150, 150))
    regra_linha1 = (fonte_botao.render('As pontes permitem', True, (0, 0, 0)))
    regra_linha2 = (fonte_botao.render('que o jogador', True, (0, 0, 0)))
    regra_linha3 = (fonte_botao.render('avance no tabuleiro', True, (0, 0, 0)))
    regra_linha4 = (fonte_botao.render('cortando caminho.', True, (0, 0, 0)))
    espaco = fonte_botao.render('Aperte espaço', True, (0, 0, 0))
    espaco_2 = fonte_botao.render('para continuar', True, (0, 0, 0))
    janela.blit(regra_linha1, (200, 225))
    janela.blit(regra_linha2, (230, 250))
    janela.blit(regra_linha3, (200, 275))
    janela.blit(regra_linha4, (210, 300))
    janela.blit(espaco, (235, 350))
    janela.blit(espaco_2, (230, 375))

def regra_adulto_5():
    janela.blit(mens_box, (150, 150))
    regra_linha1 = (fonte_botao.render('O jogador que cair', True, (0, 0, 0)))
    regra_linha2 = (fonte_botao.render('no buraco na estra-', True, (0, 0, 0)))
    regra_linha3 = (fonte_botao.render('da deverá ficar uma', True, (0, 0, 0)))
    regra_linha4 = (fonte_botao.render('rodada sem jogar.', True, (0, 0, 0)))
    espaco = fonte_botao.render('Aperte espaço', True, (0, 0, 0))
    espaco_2 = fonte_botao.render('para continuar', True, (0, 0, 0))
    janela.blit(regra_linha1, (200, 225))
    janela.blit(regra_linha2, (200, 250))
    janela.blit(regra_linha3, (195, 275))
    janela.blit(regra_linha4, (205, 300))
    janela.blit(espaco, (235, 350))
    janela.blit(espaco_2, (230, 375))

def regra_adulto_6():
    janela.blit(mens_box, (150, 150))
    regra_linha1 = (fonte_botao.render('O tabuleiro conta', True, (0, 0, 0)))
    regra_linha2 = (fonte_botao.render('com uma série de per-', True, (0, 0, 0)))
    regra_linha3 = (fonte_botao.render('guntas sobre regras de', True, (0, 0, 0)))
    regra_linha4 = (fonte_botao.render('trânsito, divididas', True, (0, 0, 0)))
    regra_linha5 = (fonte_botao.render('em 4 níveis marcados', True, (0, 0, 0)))
    regra_linha6 = (fonte_botao.render('pelas cores das placas', True, (0, 0, 0)))
    espaco = fonte_botao.render('Aperte espaço', True, (0, 0, 0))
    espaco_2 = fonte_botao.render('para continuar', True, (0, 0, 0))
    janela.blit(regra_linha1, (200, 200))
    janela.blit(regra_linha2, (190, 225))
    janela.blit(regra_linha3, (190, 250))
    janela.blit(regra_linha4, (185, 275))
    janela.blit(regra_linha5, (195, 300))
    janela.blit(regra_linha6, (185, 325))
    janela.blit(espaco, (235, 350))
    janela.blit(espaco_2, (230, 375))

#Título do menu
def menu_txt():
    janela.blit(menu_titulo, (70,70))

#Placas
def placas():
    placaazul = pygame.image.load('../img/img_jog_car/placaazul.png')
    placaverde = pygame.image.load('../img/img_jog_car/placaverde.png')
    placaamarela = pygame.image.load('../img/img_jog_car/placaamarela.png')
    placavermelha = pygame.image.load('../img/img_jog_car/placavermelha.png')
    janela.blit(placaazul, (100,100))
    janela.blit(placaverde, (250, 100))
    janela.blit(placaamarela, (100, 200))
    janela.blit(placavermelha, (250, 200))

#Imagens dos jogadores
def carro_jog_az():
    janela.blit(carro_img_az, (coord_x_az[ponteiro_az], coord_y_az[ponteiro_az]))

def carro_jog_am():
    janela.blit(carro_img_am, (coord_x_am[ponteiro_am], coord_y_am[ponteiro_am]))

#Imagens do sistema de pontos
def carteira_amarela():
    janela.blit(cart_amarela, (carteira_x[0],carteira_y[0]))

def carteira_azul():
    janela.blit(cart_azul, (carteira_x[1], carteira_y[1]))

def carteira_cinza():
    janela.blit(cart_pb, (carteira_x[x],carteira_y[y]))

#Imagens do sorteio
def mens_txt_sort_inf():
    janela.blit(mens_box_sorteio,(0,0))

def mens_txt_sort_ad():
    janela.blit(fundo_adulto,(0,0))
    janela.blit(mens_box,(150,150))

#Imagem buraco
def mens_txt_buraco():
    janela.blit(mens_box_buraco, (mens_box_x, mens_box_y))


pygame.display.flip()

while True:

    escolha = random.choice(jogadores)

    while abertura:
        motor.play()
        janela.fill((255,255,255))
        dim_linha = [310, 5]
        tempo = pygame.time.get_ticks()
        grupo = fonte_tit.render('GRUPO', True, (0, 0, 0))
        horus = fonte_tit.render('HÓRUS', True, (0, 0, 0))
        apresenta = fonte_botao.render('apresenta', True, (0, 0, 0))
        print(tempo)
        if tempo <= 1200:
            janela.blit(grupo, (170, 250))
        if 1201 <= tempo <= 1300:
            janela.blit(grupo, (170, 250))
            janela.blit(horus, (340, 250))
        if 1301 <= tempo <= 1600:
            janela.blit(grupo, (170, 250))
            janela.blit(horus, (340, 250))
            linha = pygame.draw.rect(janela, (255, 185, 0), (160, 285, dim_linha[0], dim_linha[1]))
        if 1601 <= tempo <= 2500:
            janela.blit(grupo, (170, 250))
            janela.blit(horus, (340, 250))
            linha = pygame.draw.rect(janela, (255, 185, 0), (160, 285, dim_linha[0], dim_linha[1]))
            janela.blit(apresenta, (250,300))
        if 2501 <= tempo <= 3500:
            janela.fill((0,0,0))
        if tempo == 3500:
            abertura = False
            intro = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.flip()

    while intro:
        buzina.play()
        janela.blit(fundo_intro, (0, 0))
        intro_txt()
        titulo_intro_y -= 2
        janela.blit(carro_intro, (carro_intro_x,carro_intro_y))
        carro_intro_x += 5
        if titulo_intro_y == 70:
            intro = False
            menu = True

        pygame.display.flip()

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
                    escolha_modo = True
                if event.button == pygame.BUTTON_LEFT and 260 > mouse[0] > 60 and 300 > mouse[1] > 250:
                    menu = False
                    conf_audio = True
                if event.button == pygame.BUTTON_LEFT and 260 > mouse[0] > 60 and 400 > mouse[1] > 350:
                    janela.blit(mens_menu, (250, 200))
                if event.button == pygame.BUTTON_LEFT and 260 > mouse[0] > 60 and 500 > mouse[1] > 450:
                    pygame.quit()

        pygame.display.flip()

    while conf_audio:
        janela.blit(fundo_menu, (0, 0))
        menu_txt()
        menu_opc()
        opc_mutar()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if event.button == pygame.BUTTON_LEFT and 260 > mouse[0] > 60 and 200 > mouse[1] > 150:
                    menu = False
                    escolha_modo = True
                    conf_audio = False
                if event.button == pygame.BUTTON_LEFT and 530 > mouse[0] > 340 and 300 > mouse[1] > 250:
                    conf_audio = True
                    audio = False
                if event.button == pygame.BUTTON_LEFT and 260 > mouse[0] > 60 and 400 > mouse[1] > 350:
                    conf_audio = False
                    janela.blit(mens_menu, (250, 200))
                if event.button == pygame.BUTTON_LEFT and 260 > mouse[0] > 60 and 500 > mouse[1] > 450:
                    pygame.quit()

        pygame.display.flip()


    while escolha_modo:
        janela.blit(fundo_menu, (0, 0))
        modos_jogo()
        menu_txt()
        escolha_txt()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT and 600 > mouse[0] > 80 and 603 > mouse[1] > 523:
                    escolha_modo = False
                    menu = True
                if event.button == pygame.BUTTON_LEFT and 290 > mouse[0] > 90 and 350 > mouse[1] > 300:
                    escolha_modo = False
                    modo_infantil = True
                    regra1 = True
                elif event.button == pygame.BUTTON_LEFT and 520 > mouse[0] > 320 and 350 > mouse[1] > 300:
                    escolha_modo = False
                    modo_adulto = True
                    regra1 = True

        pygame.display.update()

    while modo_infantil:

        mouse = pygame.mouse.get_pos()
        janela.blit(mutar, (520, 10))
        if audio == True:
            musica_infantil = mixer.music.load('../audio/signal_8bit.wav')
            mixer.music.play(-1)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT and 600 > mouse[0] > 520 and 90 > mouse[1] > 10:
                        audio = False
        elif audio == False:
            pygame.mixer.music.stop()
        while regra1:
            janela.blit(fundo_infantil, (0, 0))
            pygame.draw.rect(janela, (255, 0, 0), (253, dado_y, 50, 50))
            dado_regra()
            regra_infantil_1()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        regra1 = False
                        regra2 = True

            pygame.display.update()

        while regra2:
            janela.blit(fundo_infantil, (0, 0))
            dado_regra()
            pygame.draw.rect(janela, (255, 0, 0), (carteira_x[1], carteira_y[1], 127, 90))
            carteira_azul()
            regra_infantil_2()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        regra2 = False
                        regra3 = True

            pygame.display.update()

        while regra3:
            janela.blit(fundo_infantil, (0, 0))
            dado_regra()
            carteira_azul()
            regra_infantil_3()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        regra3 = False
                        regra4 = True

            pygame.display.update()

        while regra4:
            janela.blit(fundo_infantil, (0, 0))
            dado_regra()
            carteira_azul()
            regra_infantil_4()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        regra4 = False
                        regra5 = True

            pygame.display.update()

        while regra5:
            janela.blit(fundo_infantil, (0, 0))
            dado_regra()
            carteira_azul()
            regra_infantil_5()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        regra5 = False
                        regra6 = True

            pygame.display.update()

        while regra6:
            janela.blit(fundo_infantil, (0, 0))
            dado_regra()
            carteira_azul()
            placas()
            regra_infantil_6()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        regra6 = False
                        sorteio = True

        while sorteio:

            janela.blit(fundo_infantil, (0, 0))
            mens_txt_sort_inf()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print('O primeiro a jogar será o: {}! Aperte espaço para jogar o dado.'.format(escolha))
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        sorteio = False
                        jogo_infantil = True

            pygame.display.flip()



        while jogo_infantil:

            janela.blit(fundo_infantil, (0, 0))
            carro_jog_am()
            carro_jog_az()
            janela.blit(botao_volta, (520, 523))
            botao_mutar()

            mouse = pygame.mouse.get_pos()
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT and 600 > mouse[0] > 80 and 603 > mouse[1] > 523:
                        jogo_infantil = False
                        modo_infantil = False
                        escolha_modo = True
                    if event.button == pygame.BUTTON_LEFT and 600 > mouse[0] > 520 and 90 > mouse[1] > 10:
                        pygame.mixer_music.stop()

            pygame.display.flip()

    while modo_adulto:

        janela.blit(fundo_adulto, (0, 0))
        botao_mutar()

        mouse = pygame.mouse.get_pos()
        if audio == True:
            musica_adulto = mixer.music.load('../audio/whatislove_8bit.wav')
            mixer.music.play(-1)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT and 600 > mouse[0] > 520 and 90 > mouse[1] > 10:
                        pygame.mixer.quit()
        else:
            pygame.event.get()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT and 600 > mouse[0] > 520 and 90 > mouse[1] > 10:
                        pygame.mixer.music.stop()
        while regra1:
            janela.blit(fundo_adulto, (0, 0))
            pygame.draw.rect(janela, (255, 0, 0), (253, dado_y, 50, 50))
            dado_regra()
            regra_adulto_1()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        regra1 = False
                        regra2 = True

            pygame.display.flip()

        while regra2:
            janela.blit(fundo_adulto, (0, 0))
            dado_regra()
            pygame.draw.rect(janela, (255, 0, 0), (carteira_x[1], carteira_y[1], 127, 90))
            carteira_azul()
            regra_adulto_2()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        regra2 = False
                        regra3 = True

            pygame.display.flip()

        while regra3:
            janela.blit(fundo_adulto, (0, 0))
            dado_regra()
            carteira_azul()
            regra_adulto_3()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        regra3 = False
                        regra4 = True

            pygame.display.flip()

        while regra4:
            janela.blit(fundo_adulto, (0, 0))
            dado_regra()
            carteira_azul()
            regra_adulto_4()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        regra4 = False
                        regra5 = True

            pygame.display.flip()

        while regra5:
            janela.blit(fundo_adulto, (0, 0))
            dado_regra()
            carteira_azul()
            regra_adulto_5()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        regra5 = False
                        regra6 = True

            pygame.display.flip()

        while regra6:
            janela.blit(fundo_adulto, (0, 0))
            dado_regra()
            carteira_azul()
            regra_adulto_6()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        regra6 = False
                        sorteio = True

            pygame.display.flip()

        while sorteio:

            janela.blit(fundo_adulto, (0, 0))
            mens_txt_sort_ad()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print('O primeiro a jogar será o: {}! Aperte espaço para jogar o dado.'.format(escolha))
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        sorteio = False
                        jogo_adulto = True


        while jogo_adulto:
            botao_mutar()
            janela.blit(botao_volta, (520, 523))

            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT and 600 > mouse[0] > 80 and 603 > mouse[1] > 523:
                        escolha_modo = True
                        jogo_adulto = False
                        modo_adulto = False

            pygame.display.flip()










