import pygame, math, random, time
from pygame import mixer
from questions import Data
from imagens import *
from audio import *
from eventos import *
from textos import *

pygame.init()
pygame.font.init()

#Configurações da janela
janela = pygame.display.set_mode((600,600))
nome = pygame.display.set_caption(('Manual das Ruas'))
pygame.display.set_icon(icone)
x = 55
y = [180, 240, 300, 360]
largura = 480
altura = 50

#Introdução do jogo
mut = 0
titulo_intro_x = 120
titulo_intro_y = 300
carro_intro_x = 0
carro_intro_y = 460
menu_titulo = fonte_tit.render('MANUAL DAS RUAS', True, (255, 255, 255))

escolha = ''
vencedor = ''
perdedor = ''
jogadores = ['Jogador 1', 'Jogador 2']
customizacao_1_adulto = ''
customizacao_2_adulto = ''

#Coordenadas da carteira
carteira_x = [30, 440]
carteira_y = [490, 30]

#Jogador 1
carro_img_1 = ''
coord_x_1 = [40, 40,  40, 40, 40, 110, 170, 260, 310, 330, 390, 440, 490, 500, 500, 500,500, 490, 440, 430, 425, 360, 300, 240, 220, 150, 100, 45, 40, 40]
coord_y_1 = [250, 200, 150, 100, 40, 15, 20, 40, 50, 100, 110, 110, 110, 175, 230, 285, 340, 395, 410, 465, 520, 510, 500, 490, 440, 430, 430, 415, 360, 310]
pontos_1 = 0
cart_1 = ''

#Jogador 2
carro_img_2 = ''
coord_x_2 = [40, 40,  40, 40, 40, 110, 170, 260, 310, 330, 390, 440, 490, 500, 500, 500,500, 490, 440, 430, 425, 360, 300, 240, 220, 150, 100, 45, 40, 40]
coord_y_2 = [250, 200, 150, 100, 40, 15, 20, 40, 50, 100, 110, 110, 110, 175, 230, 285, 340, 395, 410, 465, 520, 510, 500, 490, 440, 430, 430, 415, 360, 310]
pontos_2 = 0
cart_2 = ''

#Coordenadas da caixa de texto
mens_box_x = 150
mens_box_y = 170

#Ponteiro das casas guiadas a dado
ponteiro_1 = 0
ponteiro_2 = 0
ponteiro_1_perg = 0
ponteiro_2_perg = 0

#Configuração das casas
perguntas = [2, 3, 4, 5, 7, 9, 10, 11, 12, 14, 15, 16, 19, 21, 22, 24, 25, 28, 29, 30]
pontes = [6, 8, 17, 18, 21]
buracos = [1, 13, 20, 26, 27]

#Coordenadas dos dados
dado_1 = ''
dado_2 = ''
dado_x = 255
dado_y = 5

#Coordenadas dos nomes
x_nomes = [75, 85, 95, 70, 100]
y_nomes = [430, 470, 510, 550, 590]

def dado_regra():
    dado_regra = pygame.image.load(dado_am[0])
    janela.blit(dado_regra,(dado_x, dado_y))

#Opções do menu
def menu_opc():
    mouse = pygame.mouse.get_pos()
    opc_jog = pygame.draw.rect(janela, (255, 255, 255), (60, 150, 200, 50))
    menu_botao1 = fonte_botao.render('COMEÇAR JOGO', True, (0, 0, 0))
    janela.blit(menu_botao1, (90, 170))
    opc_aud = pygame.draw.rect(janela, (255, 255, 255), (60, 250, 200, 50))
    menu_botao2 = fonte_botao.render('ÁUDIO', True, (0, 0, 0))
    janela.blit(menu_botao2, (130, 270))
    opc_tam = pygame.draw.rect(janela, (255, 255, 255), (60, 350, 200, 50))
    menu_botao3 = fonte_botao.render('CRÉDITOS', True, (0, 0, 0))
    janela.blit(menu_botao3, (120, 370))
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
        menu_botao3 = fonte_botao.render('CRÉDITOS', True, (255, 255, 255))
        janela.blit(menu_botao3, (120, 370))
    if 260 > mouse[0] > 60 and 500 > mouse[1] > 450:
        opc_sair = pygame.draw.rect(janela, (0, 0, 0), (60, 450, 200, 50))
        menu_botao4 = fonte_botao.render('SAIR DO JOGO', True, (255, 255, 255))
        janela.blit(menu_botao4, (90, 470))

#Texto da introdução
def intro_txt():
    janela.blit(menu_titulo, (titulo_intro_x, titulo_intro_y))

#Modos do jogo
def modos_jogo():
    escolha_txt = fonte_botao.render('ESCOLHA UM DOS MODOS', True, (255, 255, 255))
    janela.blit(escolha_txt, (190, 150))
    mouse = pygame.mouse.get_pos()
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

#Escolha do número dos jogadores
def num_jogadores():
    escolha_txt = fonte_botao.render('SELECIONE O NÚMERO DE JOGADORES', True, (255, 255, 255))
    janela.blit(escolha_txt, (120, 150))
    mouse = pygame.mouse.get_pos()
    jog_1 = pygame.draw.rect(janela, (255, 255, 255), (90, 300, 200, 50))
    opc_1 = fonte_botao.render('UM JOGADOR', True, (0, 0, 0))
    janela.blit(opc_1, (130, 320))
    jog_2 = pygame.draw.rect(janela, (255, 255, 255), (320, 300, 200, 50))
    opc_2 = fonte_botao.render('DOIS JOGADORES', True, (0, 0, 0))
    janela.blit(opc_2, (340, 320))
    if 290 > mouse [0] > 90 and 350 > mouse [1] > 300:
        jog_1 = pygame.draw.rect(janela, (0, 0, 0), (90, 300, 200, 50))
        opc_1 = fonte_botao.render('UM JOGADOR', True, (255, 255, 255))
        janela.blit(opc_1, (130, 320))
    elif 520 > mouse [0] > 320 and 350 > mouse[1] > 300:
        jog_2 = pygame.draw.rect(janela, (0, 0, 0), (320, 300, 200, 50))
        opc_2 = fonte_botao.render('DOIS JOGADORES', True, (255, 255, 255))
        janela.blit(opc_2, (340, 320))

#Configurações de áudio
def opc_mutar():
    mouse = pygame.mouse.get_pos()
    aud_mute = pygame.image.load('../img/img_jog_car/mutar_branco.png')
    janela.blit(aud_mute, (340, 236))
    if 530 > mouse[0] > 340 and 300 > mouse[1] > 250:
        aud_mute = pygame.image.load('../img/img_jog_car/mutar_branco.png')
        janela.blit(aud_mute, (340, 236))

#Escolha das cores dos carros
def custom():
    escolha_txt = fonte_botao.render('JOGADOR 1, ESCOLHA UMA COR!', True, (255, 255, 255))
    janela.blit(escolha_txt, (130, 150))
    if carro_img_1 == carro_azul or carro_img_1 == carro_amarelo or carro_img_1 == carro_rosa or carro_img_1 == carro_verde or carro_img_1 == carro_cinza:
        escolha_txt = fonte_botao.render('JOGADOR 2, ESCOLHA UMA COR!', True, (255, 255, 255))
        janela.blit(escolha_txt, (130, 150))
    janela.blit(carro_box, (80, 220))
    janela.blit(carro_box, (240, 220))
    janela.blit(carro_box, (400, 220))
    janela.blit(carro_box, (160, 350))
    janela.blit(carro_box, (320, 350))
    janela.blit(carro_amarelo, (110, 250))
    janela.blit(carro_azul, (270, 250))
    janela.blit(carro_rosa, (430, 250))
    janela.blit(carro_verde, (190, 380))
    janela.blit(carro_cinza, (350, 380))


def botao_mutar():
    mouse = pygame.mouse.get_pos()
    janela.blit(mutar, (205, 257))
    if 285 > mouse[0] > 205 and 337 > mouse[1] > 257:
        janela.blit(mutar_mouse, (205, 257))

def botao_voltar():
    if escolha_modo == True:
        janela.blit(botao_volta, (400, 332))
    elif opcoes == True:
        janela.blit(botao_volta, (200, 60))

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
    janela.blit(menu_titulo, (120,70))

#Placas
def placas():
    janela.blit(placaazul, (100,100))
    janela.blit(placaverde, (250, 100))
    janela.blit(placaamarela, (100, 200))
    janela.blit(placavermelha, (250, 200))

#Imagens dos jogadores
def carro_jog_2():
    janela.blit(carro_img_2, (coord_x_2[ponteiro_2], coord_y_2[ponteiro_2]))

def carro_jog_1():
    janela.blit(carro_img_1, (coord_x_1[ponteiro_1], coord_y_1[ponteiro_1]))

#Imagens do sistema de pontos
def carteira_1():
    janela.blit(cart_1, (10, 500))

def carteira_2():
    janela.blit(cart_2, (120, 500))

#Imagens do sorteio
def mens_txt_sort_inf():
    janela.blit(mens_box_sorteio,(0,0))

def mens_txt_sort_ad():
    janela.blit(fundo_adulto,(0,0))
    janela.blit(mens_box,(150,150))

def show_text(txt, x, y, width, color):
    sys_font = pygame.font.SysFont('None', width)
    wrap = txt.find('  ')

    if wrap > 0:
        top_text = sys_font.render(txt[:wrap - 5], True, color)
        bottom_text = sys_font.render(txt[wrap:], True, color)
        janela.blit(top_text, (x, y - 9))
        janela.blit(bottom_text, (x, y + 9))
    else:
        text = sys_font.render(txt, True, color)
        janela.blit(text, (x, y))


def ask_1 (number):
    for key, value in Data.items():
        # Informa a chave da pergunta e o seu valor
        if ponteiro_1_perg in perguntas:

            if carro_img_1 == carro_azul:
                pygame.draw.rect(janela, (50, 137, 168), (x, y[0], largura, altura))
                pygame.draw.rect(janela, (50, 137, 168), (x, y[1], largura, altura))
                pygame.draw.rect(janela, (50, 137, 168), (x, y[2], largura, altura))
                pygame.draw.rect(janela, (50, 137, 168), (x, y[3], largura, altura))
            elif carro_img_1 == carro_amarelo:
                pygame.draw.rect(janela, (222, 188, 0), (x, y[0], largura, altura))
                pygame.draw.rect(janela, (222, 188, 0), (x, y[1], largura, altura))
                pygame.draw.rect(janela, (222, 188, 0), (x, y[2], largura, altura))
                pygame.draw.rect(janela, (222, 188, 0), (x, y[3], largura, altura))
            elif carro_img_1 == carro_rosa:
                pygame.draw.rect(janela, (189, 1, 69), (x, y[0], largura, altura))
                pygame.draw.rect(janela, (189, 1, 69), (x, y[1], largura, altura))
                pygame.draw.rect(janela, (189, 1, 69), (x, y[2], largura, altura))
                pygame.draw.rect(janela, (189, 1, 69), (x, y[3], largura, altura))
            elif carro_img_1 == carro_verde:
                pygame.draw.rect(janela, (0, 116, 1), (x, y[0], largura, altura))
                pygame.draw.rect(janela, (0, 116, 1), (x, y[1], largura, altura))
                pygame.draw.rect(janela, (0, 116, 1), (x, y[2], largura, altura))
                pygame.draw.rect(janela, (0, 116, 1), (x, y[3], largura, altura))
            elif carro_img_1 == carro_cinza:
                pygame.draw.rect(janela, (0, 0, 0), (x, y[0], largura, altura))
                pygame.draw.rect(janela, (0, 0, 0), (x, y[1], largura, altura))
                pygame.draw.rect(janela, (0, 0, 0), (x, y[2], largura, altura))
                pygame.draw.rect(janela, (0, 0, 0), (x, y[3], largura, altura))

            if key == number:
                question = '{0}: {1}'.format(key, value['question'])
                show_text(question, 90, 100, 20, (0, 0, 0))

                # Show options
                show_text(('[A]: {}'.format(value["options"]["A"])), (x + 10), (y[0] + 18), 20, (255, 255, 255))
                show_text(('[B]: {}'.format(value["options"]["B"])), (x + 10), (y[1] + 18), 20, (255, 255, 255))
                show_text(('[C]: {}'.format(value["options"]["C"])), (x + 10), (y[2] + 18), 20, (255, 255, 255))
                show_text(('[D]: {}'.format(value["options"]["D"])), (x + 10), (y[3] + 18), 20, (255, 255, 255))

                return value

def ask_2 (number):
    for key, value in Data.items():
        # Informa a chave da pergunta e o seu valor
        if ponteiro_2_perg in perguntas:
            if carro_img_2 == carro_azul:
                pygame.draw.rect(janela, (50, 137, 168), (x, y[0], largura, altura))
                pygame.draw.rect(janela, (50, 137, 168), (x, y[1], largura, altura))
                pygame.draw.rect(janela, (50, 137, 168), (x, y[2], largura, altura))
                pygame.draw.rect(janela, (50, 137, 168), (x, y[3], largura, altura))
            elif carro_img_2 == carro_amarelo:
                pygame.draw.rect(janela, (222, 188, 0), (x, y[0], largura, altura))
                pygame.draw.rect(janela, (222, 188, 0), (x, y[1], largura, altura))
                pygame.draw.rect(janela, (222, 188, 0), (x, y[2], largura, altura))
                pygame.draw.rect(janela, (222, 188, 0), (x, y[3], largura, altura))
            elif carro_img_2 == carro_rosa:
                pygame.draw.rect(janela, (189, 1, 69), (x, y[0], largura, altura))
                pygame.draw.rect(janela, (189, 1, 69), (x, y[1], largura, altura))
                pygame.draw.rect(janela, (189, 1, 69), (x, y[2], largura, altura))
                pygame.draw.rect(janela, (189, 1, 69), (x, y[3], largura, altura))
            elif carro_img_2 == carro_verde:
                pygame.draw.rect(janela, (0, 116, 1), (x, y[0], largura, altura))
                pygame.draw.rect(janela, (0, 116, 1), (x, y[1], largura, altura))
                pygame.draw.rect(janela, (0, 116, 1), (x, y[2], largura, altura))
                pygame.draw.rect(janela, (0, 116, 1), (x, y[3], largura, altura))
            elif carro_img_2 == carro_cinza:
                pygame.draw.rect(janela, (0, 0, 0), (x, y[0], largura, altura))
                pygame.draw.rect(janela, (0, 0, 0), (x, y[1], largura, altura))
                pygame.draw.rect(janela, (0, 0, 0), (x, y[2], largura, altura))
                pygame.draw.rect(janela, (0, 0, 0), (x, y[3], largura, altura))

            if key == number:
                question = '{0}: {1}'.format(key, value['question'])
                show_text(question, 90, 100, 20, (0, 0, 0))

                # Show options
                show_text(('[A]: {}'.format(value["options"]["A"])), (x + 10), (y[0] + 18), 20, (255, 255, 255))
                show_text(('[B]: {}'.format(value["options"]["B"])), (x + 10), (y[1] + 18), 20, (255, 255, 255))
                show_text(('[C]: {}'.format(value["options"]["C"])), (x + 10), (y[2] + 18), 20, (255, 255, 255))
                show_text(('[D]: {}'.format(value["options"]["D"])), (x + 10), (y[3] + 18), 20, (255, 255, 255))

                return value

def placas_dif():
    if difficulty == "Fácil":
        janela.blit(placaazul, (240, 410))
    elif difficulty == "Médio":
        janela.blit(placaverde, (240, 410))
    elif difficulty == "Difícil":
        janela.blit(placaamarela, (240, 410))
    elif difficulty == "Muito difícil":
        janela.blit(placavermelha, (240, 410))

def menu_acesso():
    mouse = pygame.mouse.get_pos()
    janela.blit(menu_acesso_img, (510, 20))
    if 585 > mouse[0] > 510 and 47 > mouse[1] > 20:
        janela.blit(menu_acesso_img_m, (500, 15))

def menu_peq():
    mouse = pygame.mouse.get_pos()
    janela.blit(menu_opcoes_img, (175, 217))
def ponte():
    janela.blit(mens_box, (150, 150))
    janela.blit(ponte1, (235, 200))
    janela.blit(ponte2, (190, 225))
    janela.blit(pulo1, (200, 300))
    janela.blit(pulo2, (210, 325))
    janela.blit(espaco_1, (235, 350))
    janela.blit(espaco_2, (230, 375))

def buraco():
    if num_jog == '2':
        vez1 = (fonte_botao.render('A vez é do {}!'.format(escolha), True, (0, 0, 0)))
        janela.blit(vez1, (200, 300))
        janela.blit(vez2, (210, 325))
    janela.blit(mens_box, (150, 150))
    janela.blit(buraco1, (250, 200))
    janela.blit(buraco2, (190, 225))
    janela.blit(espaco_1, (235, 350))
    janela.blit(espaco_2, (230, 375))

def acerto():
    if num_jog == '2':
        vez1 = (fonte_botao.render('A vez é do {}!'.format(escolha), True, (0, 0, 0)))
        janela.blit(vez1, (200, 270))
        janela.blit(vez2, (210, 295))
    janela.blit(mens_box, (150, 150))
    janela.blit(acerto1, (225, 220))
    janela.blit(acerto2, (260, 245))
    janela.blit(espaco_1, (235, 350))
    janela.blit(espaco_2, (230, 375))


def erro():
    if num_jog == '2':
        vez1 = (fonte_botao.render('A vez é do {}!'.format(escolha), True, (0, 0, 0)))
    if escolha == 'Jogador 2':
        pontos = pontos_1
    elif escolha == 'Jogador 1':
        pontos = pontos_2
    pontos2 = (fonte_botao.render('{} pontos na carteira.'.format(pontos), True, (0, 0, 0)))
    janela.blit(mens_box, (150, 150))
    janela.blit(erro1, (230, 200))
    janela.blit(erro2, (200, 225))
    janela.blit(pontos1, (210, 250))
    janela.blit(pontos2, (185, 275))
    if num_jog == '2':
        janela.blit(vez1, (190, 300))
        janela.blit(vez2, (210, 325))
    janela.blit(espaco_1, (235, 350))
    janela.blit(espaco_2, (230, 375))

def fim():
    fim1 = (fonte_botao.render('O {} alcançou o número máximo de'.format(perdedor), True, (0, 0, 0)))
    fim2 = (fonte_botao.render('infrações.', True, (0, 0, 0)))
    if num_jog == '2':
        fim3 = (fonte_botao.render('O {} é o vencedor da partida!'.format(vencedor), True, (0, 0, 0)))
    janela.blit(guarda_regras, (0, 0))
    janela.blit(fim1, (50, 390))
    janela.blit(fim2, (50, 415))
    if num_jog == '2':
        janela.blit(fim3, (50, 440))
    janela.blit(espaco, (70, 490))

def creditos():
    gabriela = (fonte_botao.render('GABRIELA XAVIER DE A. FONTES - 5306709', True, (255, 255, 255)))
    leonardo = (fonte_botao.render('LEONARDO GOULART RODRIGUES - 5306685', True, (255, 255, 255)))
    lucas = (fonte_botao.render('LUCAS GABRIEL LEITE FARIA - 5306701', True, (255, 255, 255)))
    maria = (fonte_botao.render('MARIA FERNANDA DE MAIA XAVIER - 5405665', True, (255, 255, 255)))
    marlon = (fonte_botao.render('MARLON VICTOR R. COIMBRA - 5405689', True, (255, 255, 255)))
    janela.blit(gabriela, (x_nomes[0], y_nomes[0]))
    janela.blit(leonardo, (x_nomes[1], y_nomes[1]))
    janela.blit(lucas, (x_nomes[2], y_nomes[2]))
    janela.blit(maria, (x_nomes[3], y_nomes[3]))
    janela.blit(marlon, (x_nomes[4], y_nomes[4]))

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

            pygame.display.flip()

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
        audio = True
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
                    menu = False
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
                if event.button == pygame.BUTTON_LEFT and 260 > mouse[0] > 60 and 500 > mouse[1] > 450:
                    pygame.quit()

        pygame.display.flip()


    while escolha_modo:
        janela.blit(fundo_menu, (0, 0))
        modos_jogo()
        menu_txt()
        botao_voltar()
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
                    esc_num_jog = True
                    esc_modo += 1
                elif event.button == pygame.BUTTON_LEFT and 520 > mouse[0] > 320 and 350 > mouse[1] > 300:
                    escolha_modo = False
                    esc_num_jog = True
                    esc_modo += 2

        pygame.display.update()

    while esc_num_jog:
        janela.blit(fundo_menu, (0, 0))
        num_jogadores()
        menu_txt()
        botao_voltar()
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT and 600 > mouse[0] > 80 and 603 > mouse[1] > 523:
                    escolha_modo = False
                    menu = True
                if event.button == pygame.BUTTON_LEFT and 290 > mouse[0] > 90 and 350 > mouse[1] > 300 and (esc_modo % 2) != 0:
                    escolha_modo = False
                    esc_num_jog = False
                    num_jog = '1'
                    customizacao_1 = True
                elif event.button == pygame.BUTTON_LEFT and 520 > mouse[0] > 320 and 350 > mouse[1] > 300 and (esc_modo % 2) != 0:
                    escolha_modo = False
                    esc_num_jog = False
                    num_jog = '2'
                    customizacao_1 = True
                elif event.button == pygame.BUTTON_LEFT and 290 > mouse[0] > 90 and 350 > mouse[1] > 300 and (esc_modo % 2) == 0:
                    escolha_modo = False
                    esc_num_jog = False
                    num_jog = '1'
                    customizacao_1_adulto = True
                elif event.button == pygame.BUTTON_LEFT and 520 > mouse[0] > 320 and 350 > mouse[1] > 300 and (esc_modo % 2) == 0:
                    escolha_modo = False
                    esc_num_jog = False
                    num_jog = '2'
                    customizacao_1_adulto = True

        pygame.display.update()

    while customizacao_1:
        janela.blit(fundo_menu, (0, 0))
        menu_txt()
        custom()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if event.button == pygame.BUTTON_LEFT and 180 > mouse[0] > 80 and 320 > mouse[1] > 220:
                    carro_img_1 = carro_amarelo
                    cart_1 = cart_amarela
                    dado_1 = dado_am
                    customizacao_1 = False
                    if num_jog == '1':
                        escolha = 'Jogador 1'
                        modo_infantil = True
                        regra1 = True
                    elif num_jog == '2':
                        customizacao_2 = True
                elif event.button == pygame.BUTTON_LEFT and 340 > mouse[0] > 240 and 320 > mouse[1] > 220:
                    carro_img_1 = carro_azul
                    cart_1 = cart_azul
                    dado_1 = dado_az
                    customizacao_1 = False
                    if num_jog == '1':
                        modo_infantil = True
                        regra1 = True
                    elif num_jog == '2':
                        customizacao_2 = True
                elif event.button == pygame.BUTTON_LEFT and 500 > mouse[0] > 400 and 320 > mouse[1] > 220:
                    carro_img_1 = carro_rosa
                    cart_1 = cart_rosa
                    dado_1 = dado_rosa
                    customizacao_1 = False
                    if num_jog == '1':
                        modo_infantil = True
                        regra1 = True
                    elif num_jog == '2':
                        customizacao_2 = True
                elif event.button == pygame.BUTTON_LEFT and 260 > mouse[0] > 160 and 450 > mouse[1] > 350:
                    carro_img_1 = carro_verde
                    cart_1 = cart_verde
                    dado_1 = dado_verde
                    customizacao_1 = False
                    if num_jog == '1':
                        modo_infantil = True
                        regra1 = True
                    elif num_jog == '2':
                        customizacao_2 = True
                elif event.button == pygame.BUTTON_LEFT and 420 > mouse[0] > 320 and 450 > mouse[1] > 350:
                    carro_img_1 = carro_cinza
                    cart_1 = cart_cinza
                    dado_1 = dado_cinza
                    customizacao_1 = False
                    if num_jog == '1':
                        modo_infantil = True
                        regra1 = True
                    elif num_jog == '2':
                        customizacao_2 = True

        pygame.display.update()

    while customizacao_2:
        janela.blit(fundo_menu, (0, 0))
        menu_txt()
        custom()
        if carro_img_1 == carro_amarelo:
            janela.blit(x_vermelho, (90,230))
        elif carro_img_1 == carro_azul:
            janela.blit(x_vermelho, (250,230))
        elif carro_img_1 == carro_rosa:
            janela.blit(x_vermelho, (410,230))
        elif carro_img_1 == carro_verde:
            janela.blit(x_vermelho, (170,360))
        elif carro_img_1 == carro_cinza:
            janela.blit(x_vermelho, (330,360))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if event.button == pygame.BUTTON_LEFT and 180 > mouse[0] > 80 and 320 > mouse[1] > 220:
                    carro_img_2 = carro_amarelo
                    cart_2 = cart_amarela
                    dado_2 = dado_am
                    customizacao_2 = False
                    modo_infantil = True
                    regra1 = True
                elif event.button == pygame.BUTTON_LEFT and 340 > mouse[0] > 240 and 320 > mouse[1] > 220:
                    carro_img_2 = carro_azul
                    cart_2 = cart_azul
                    dado_2 = dado_az
                    customizacao_2 = False
                    modo_infantil = True
                    regra1 = True
                elif event.button == pygame.BUTTON_LEFT and 500 > mouse[0] > 400 and 320 > mouse[1] > 220:
                    carro_img_2 = carro_rosa
                    cart_2 = cart_rosa
                    dado_2 = dado_rosa
                    customizacao_2 = False
                    modo_infantil = True
                    regra1 = True
                elif event.button == pygame.BUTTON_LEFT and 260 > mouse[0] > 160 and 450 > mouse[1] > 350:
                    carro_img_2 = carro_verde
                    cart_2 = cart_verde
                    dado_2 = dado_verde
                    customizacao_2 = False
                    modo_infantil = True
                    regra1 = True
                elif event.button == pygame.BUTTON_LEFT and 420 > mouse[0] > 320 and 450 > mouse[1] > 350:
                    carro_img_2 = carro_cinza
                    cart_2 = cart_cinza
                    dado_2 = dado_cinza
                    customizacao_2 = False
                    modo_infantil = True
                    regra1 = True

        pygame.display.update()

    while modo_infantil:

        mouse = pygame.mouse.get_pos()
        janela.blit(mutar, (520, 10))
        botao_voltar()
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
            placas()
            regra_infantil_6()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        regra6 = False
                        if num_jog == '1':
                            jogo_infantil = True
                        elif num_jog == '2':
                            sorteio = True

            pygame.display.update()

        while sorteio:

            janela.blit(fundo_infantil, (0, 0))
            mens_txt_sort_inf()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        escolha = random.choice(jogadores)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        sorteio = False
                        sorteado = True

            pygame.display.update()

        while sorteado:
            janela.blit(fundo_infantil, (0, 0))
            janela.blit(guarda_regras, (0, 0))
            sorteio1 = (fonte_botao.render('O primeiro a jogar será o {}!'.format(escolha), True, (0, 0, 0)))
            sorteio2 = (fonte_botao.render('Preste bastante atenção, tenha', True, (0, 0, 0)))
            sorteio3 = (fonte_botao.render('calma e boa sorte!', True, (0, 0, 0)))
            espaco = fonte_botao.render('Aperte espaço para continuar', True, (0, 0, 0))
            janela.blit(sorteio1, (50, 390))
            janela.blit(sorteio2, (50, 415))
            janela.blit(sorteio3, (50, 440))
            janela.blit(espaco, (80, 490))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        sorteado = False
                        jogo_infantil = True

            pygame.display.flip()

        while jogo_infantil:

            janela.blit(fundo_infantil, (0, 0))
            carro_jog_1()
            if num_jog == '2':
                carro_jog_2()
            menu_acesso()
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and escolha == 'Jogador 1':
                        dado = random.randint(1, 6)
                        ponteiro_1_perg += dado
                        ponteiro_1 += dado
                        dado_1_vez = pygame.image.load(dado_1[dado - 1])
                        janela.blit(dado_1_vez, (dado_x, dado_y))
                        pygame.display.update()
                        if ponteiro_1_perg in buracos:
                            if num_jog == '2':
                                escolha = 'Jogador 2'
                            buraco_casa = True
                        elif ponteiro_1_perg in perguntas:
                            pergunta_1 = True
                        elif ponteiro_1_perg in pontes:
                            ponteiro_1 += 4
                            ponteiro_1_perg += 4
                            pontes_casa = True
                    if num_jog == '2':
                        if event.key == pygame.K_SPACE and escolha == 'Jogador 2':
                            dado = random.randint(1, 6)
                            ponteiro_2_perg += dado
                            ponteiro_2 += dado
                            dado_2_vez = pygame.image.load(dado_2[dado - 1])
                            janela.blit(dado_2_vez, (dado_x, dado_y))
                            pygame.display.update()
                            if ponteiro_2_perg in buracos:
                                escolha = 'Jogador 1'
                                buraco_casa = True
                            elif ponteiro_2_perg in perguntas:
                                pergunta_2 = True
                            elif ponteiro_2_perg in pontes:
                                ponteiro_2 += 4
                                ponteiro_2_perg += 4
                                pontes_casa = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT and 585 > mouse [0] > 510 and 47 > mouse[1] > 20:
                        opcoes = True

            if pontos_1 >= 40:
                perdedor = 'Jogador 1'
                vencedor = 'Jogador 2'
                jogo_infantil = False
                fim_jogo = True
                pygame.quit()
            if num_jog == '2':
                if pontos_2 >= 40:
                    perdedor = 'Jogador 2'
                    vencedor = 'Jogador 1'
                    jogo_infantil = False
                    fim_jogo = True

            if ponteiro_1_perg > 30 and pontos_2 < 40 and pontos_1 < 40:
                ponteiro_1_perg = 0
                ponteiro_1_perg += dado
            if num_jog == '2':
                if ponteiro_2_perg > 30 and pontos_2 < 40 and pontos_1 < 40:
                    ponteiro_2_perg = 0
                    ponteiro_2_perg += dado


            if ponteiro_1 >= 30:
                ponteiro_1 = 0
                ponteiro_1 += dado
            if num_jog == '2':
                if ponteiro_2 >= 30:
                    ponteiro_2 = 0
                    ponteiro_2 += dado

                # Placar de pontos
            show_points_1 = str(pontos_1)
            carteira_1()
            show_text(show_points_1, 45, 525, 30, (0, 0, 0))
            if num_jog == '2':
                show_points_2 = str(pontos_2)
                carteira_2()
                show_text(show_points_2, 155, 525, 30, (0, 0, 0))

            pygame.display.update()

            while opcoes:
                janela.blit(fundo_infantil, (0, 0))
                menu_peq()
                botao_mutar()
                botao_voltar()
                carro_jog_1()
                if num_jog == '2':
                    carro_jog_2()
                mouse = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == pygame.BUTTON_LEFT and 405 > mouse[0] > 390 and 235 > mouse[1] > 225:
                            opcoes = False
                        elif event.button == pygame.BUTTON_LEFT and 285 > mouse[0] > 205 and 337 > mouse[1] > 257 and (mut % 2) == 0:
                            pygame.mixer_music.pause()
                            mut += 1
                        elif event.button == pygame.BUTTON_LEFT and 285 > mouse[0] > 205 and 337 > mouse[1] > 257 and (mut % 2) != 0:
                            pygame.mixer_music.unpause()
                            mut += 1
                        elif event.button == pygame.BUTTON_LEFT and 395 > mouse[0] > 315 and 337 > mouse[1] > 257:
                            if audio == True:
                                pygame.mixer_music.stop()
                            opcoes = False
                            modo_infantil = False
                            jogo_infantil = False
                            ponteiro_1 = 0
                            ponteiro_1_perg = 0
                            pontos_1 = 0
                            escolha_modo = True
                            num_jog = ''
                            esc_modo = 0
                            if num_jog == '2':
                                ponteiro_2 = 0
                                ponteiro_2_perg = 0
                                pontos_2 = 0


                        pygame.display.flip()
                    pygame.display.update()
                pygame.display.update()


            while pergunta_1:
                choice = ''
                janela.blit(fundo_infantil, (0, 0))
                janela.blit(perg_box, (0, 0))
                janela.blit(dado_1_vez, (dado_x, dado_y))
                ask_values = ask_1(ponteiro_1_perg)
                answer = ask_values["answer"]  # Resposta
                difficulty = ask_values["difficulty"]  # Dificuldade
                placas_dif()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()
                        # Posição dos botões
                        if event.button == pygame.BUTTON_LEFT and (x < mouse[0] < x + largura and y[0] < mouse[1] < y[0] + altura):
                            choice = 'A'
                        elif event.button == pygame.BUTTON_LEFT and (x < mouse[0] < x + largura and y[1] < mouse[1] < y[1] + altura):
                            choice = 'B'
                        elif event.button == pygame.BUTTON_LEFT and (x < mouse[0] < x + largura and y[2] < mouse[1] < y[2] + altura):
                            choice = 'C'
                        elif event.button == pygame.BUTTON_LEFT and (x < mouse[0] < x + largura and y[3] < mouse[1] < y[3] + altura):
                            choice = 'D'
                        if choice == answer:
                            pergunta_1 = False
                            acerto_1 = True
                        else:
                            if difficulty == "Fácil":
                                pontos_1 += 3
                                pergunta_1 = False
                                erro_1_f = True
                            elif difficulty == "Médio":
                                pontos_1 += 4
                                pergunta_1 = False
                                erro_1_m = True
                            elif difficulty == "Difícil":
                                pontos_1 += 5
                                pergunta_1 = False
                                erro_1_d = True
                            elif difficulty == 'Muito difícil':
                                pontos_1 += 7
                                pergunta_1 = False
                                erro_1_md = True

                        ask_1(ponteiro_1_perg)

                        pygame.display.flip()
                    pygame.display.update()
                pygame.display.update()

            while pergunta_2:
                choice = ''
                janela.blit(fundo_infantil, (0, 0))
                janela.blit(perg_box, (0, 0))
                janela.blit(dado_2_vez, (dado_x, dado_y))
                ask_values = ask_2(ponteiro_2_perg)
                answer = ask_values["answer"]  # Resposta
                difficulty = ask_values["difficulty"]  # Dificuldade
                placas_dif()
                for event in pygame.event.get():
                    # Quit game
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()
                        # Posição dos botões
                        if event.button == pygame.BUTTON_LEFT and (x < mouse[0] < x + largura and y[0] < mouse[1] < y[0] + altura):
                            choice = 'A'
                        elif event.button == pygame.BUTTON_LEFT and (x < mouse[0] < x + largura and y[1] < mouse[1] < y[1] + altura):
                            choice = 'B'
                        elif event.button == pygame.BUTTON_LEFT and (x < mouse[0] < x + largura and y[2] < mouse[1] < y[2] + altura):
                            choice = 'C'
                        elif event.button == pygame.BUTTON_LEFT and (x < mouse[0] < x + largura and y[3] < mouse[1] < y[3] + altura):
                            choice = 'D'
                        if choice == answer:
                            pergunta_2 = False
                            acerto_2 = True
                        else:
                            if difficulty == "Fácil":
                                pontos_2 += 3
                                pergunta_2 = False
                                erro_2_f = True
                            elif difficulty == "Médio":
                                pontos_2 += 4
                                pergunta_2 = False
                                erro_2_m = True
                            elif difficulty == "Difícil":
                                pontos_2 += 5
                                pergunta_2 = False
                                erro_2_d = True
                            elif difficulty == 'Muito difícil':
                                pontos_2 += 7
                                pergunta_2 = False
                                erro_2_md = True

                            pygame.display.flip()
                        ask_2(ponteiro_2_perg)

                        pygame.display.flip()
                    pygame.display.update()

            while acerto_1:
                escolha = 'Jogador 1'
                janela.blit(fundo_infantil, (0, 0))
                acerto()
                carro_jog_1()
                if num_jog == '2':
                    carro_jog_2()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            acerto_1 = False
                            jogo_infantil = True

                pygame.display.update()

            while acerto_2:
                escolha = 'Jogador 2'
                janela.blit(fundo_infantil, (0, 0))
                acerto()
                carro_jog_1()
                carro_jog_2()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            acerto_2 = False
                            jogo_infantil = True

                pygame.display.update()

            while erro_1_f:
                if num_jog == '1':
                    escolha = 'Jogador 1'
                elif num_jog == '2':
                    carro_jog_2()
                    escolha = 'Jogador 2'
                janela.blit(fundo_infantil, (0, 0))
                erro()
                carro_jog_1()
                if num_jog == '2':
                    carro_jog_2()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            erro_1_f = False
                            jogo_infantil = True

                pygame.display.update()

            while erro_1_m:
                if num_jog == '1':
                    escolha = 'Jogador 1'
                elif num_jog == '2':
                    carro_jog_2()
                    escolha = 'Jogador 2'
                janela.blit(fundo_infantil, (0, 0))
                erro()
                carro_jog_1()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            erro_1_m = False
                            jogo_infantil = True

                pygame.display.update()

            while erro_1_d:
                if num_jog == '1':
                    escolha = 'Jogador 1'
                elif num_jog == '2':
                    carro_jog_2()
                    escolha = 'Jogador 2'
                janela.blit(fundo_infantil, (0, 0))
                erro()
                carro_jog_1()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            erro_1_d = False
                            jogo_infantil = True

                pygame.display.update()

            while erro_1_md:
                if num_jog == '1':
                    escolha = 'Jogador 1'
                elif num_jog == '2':
                    escolha = 'Jogador 2'
                    carro_jog_2()
                janela.blit(fundo_infantil, (0, 0))
                erro()
                carro_jog_1()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            erro_1_md = False
                            jogo_infantil = True

                pygame.display.update()

            while erro_2_f:
                escolha = 'Jogador 1'
                janela.blit(fundo_infantil, (0, 0))
                erro()
                carro_jog_1()
                carro_jog_2()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            erro_2_f = False
                            jogo_infantil = True

                pygame.display.update()

            while erro_2_m:
                escolha = 'Jogador 1'
                janela.blit(fundo_infantil, (0, 0))
                erro()
                carro_jog_1()
                carro_jog_2()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            erro_2_m = False
                            jogo_infantil = True

                pygame.display.update()

            while erro_2_d:
                escolha = 'Jogador 1'
                janela.blit(fundo_infantil, (0, 0))
                erro()
                carro_jog_1()
                carro_jog_2()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            erro_2_d = False
                            jogo_infantil = True

                pygame.display.update()

            while erro_2_md:
                escolha = 'Jogador 1'
                janela.blit(fundo_infantil, (0, 0))
                janela.blit(mens_box, (150, 150))
                erro()
                carro_jog_1()
                carro_jog_2()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            erro_2_md = False
                            jogo_infantil = True

                pygame.display.update()

            while buraco_casa:
                janela.blit(fundo_infantil, (0, 0))
                janela.blit(mens_box, (150, 150))
                if num_jog == '2':
                    carro_jog_2()
                    if escolha == 'Jogador 2':
                        janela.blit(dado_1_vez, (dado_x, dado_y))
                    elif escolha == 'Jogador 1':
                        janela.blit(dado_2_vez, (dado_x, dado_y))
                buraco()
                carro_jog_1()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            buraco_casa = False
                            jogo_infantil = True

                pygame.display.update()

            while pontes_casa:
                janela.blit(fundo_infantil, (0, 0))
                janela.blit(mens_box, (150, 150))
                ponte()
                carro_jog_1()
                if num_jog == '2':
                    carro_jog_2()
                if escolha == 'Jogador 1':
                    janela.blit(dado_1_vez, (dado_x, dado_y))
                elif escolha == 'Jogador 2':
                    janela.blit(dado_2_vez, (dado_x, dado_y))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            pontes_casa = False
                            jogo_infantil = True

                pygame.display.update()

        while fim_jogo:
            janela.blit(fundo_infantil, (0, 0))
            fim()
            if audio == True:
                pygame.mixer.stop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        jogo_infantil = False
                        modo_infantil = False
                        fim_jogo = False
                        menu = True

            pygame.display.flip()

   #test_inicio
    while customizacao_1_adulto:
        janela.blit(fundo_menu, (0, 0))
        menu_txt()
        custom()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if event.button == pygame.BUTTON_LEFT and 180 > mouse[0] > 80 and 320 > mouse[1] > 220:
                    carro_img_1 = carro_amarelo
                    cart_1 = cart_amarela
                    dado_1 = dado_am
                    customizacao_1_adulto = False
                    if num_jog == '1':
                        escolha = 'Jogador 1'
                        modo_adulto = True
                        regra1 = True
                    elif num_jog == '2':
                        customizacao_2_adulto = True
                elif event.button == pygame.BUTTON_LEFT and 340 > mouse[0] > 240 and 320 > mouse[1] > 220:
                    carro_img_1 = carro_azul
                    cart_1 = cart_azul
                    dado_1 = dado_az
                    customizacao_1_adulto = False
                    if num_jog == '1':
                        modo_adulto = True
                        regra1 = True
                    elif num_jog == '2':
                        customizacao_2_adulto = True
                elif event.button == pygame.BUTTON_LEFT and 500 > mouse[0] > 400 and 320 > mouse[1] > 220:
                    carro_img_1 = carro_rosa
                    cart_1 = cart_rosa
                    dado_1 = dado_rosa
                    customizacao_1_adulto = False
                    if num_jog == '1':
                        modo_adulto = True
                        regra1 = True
                    elif num_jog == '2':
                        customizacao_2_adulto = True
                elif event.button == pygame.BUTTON_LEFT and 260 > mouse[0] > 160 and 450 > mouse[1] > 350:
                    carro_img_1 = carro_verde
                    cart_1 = cart_verde
                    dado_1 = dado_verde
                    customizacao_1_adulto = False
                    if num_jog == '1':
                        modo_adulto = True
                        regra1 = True
                    elif num_jog == '2':
                        customizacao_2_adulto = True
                elif event.button == pygame.BUTTON_LEFT and 420 > mouse[0] > 320 and 450 > mouse[1] > 350:
                    carro_img_1 = carro_cinza
                    cart_1 = cart_cinza
                    dado_1 = dado_cinza
                    customizacao_1_adulto = False
                    if num_jog == '1':
                        modo_adulto = True
                        regra1 = True
                    elif num_jog == '2':
                        customizacao_2_adulto = True

        pygame.display.update()

    while customizacao_2_adulto:
        janela.blit(fundo_menu, (0, 0))
        menu_txt()
        custom()
        if carro_img_1 == carro_amarelo:
            janela.blit(x_vermelho, (90, 230))
        elif carro_img_1 == carro_azul:
            janela.blit(x_vermelho, (250, 230))
        elif carro_img_1 == carro_rosa:
            janela.blit(x_vermelho, (410, 230))
        elif carro_img_1 == carro_verde:
            janela.blit(x_vermelho, (170, 360))
        elif carro_img_1 == carro_cinza:
            janela.blit(x_vermelho, (330, 360))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if event.button == pygame.BUTTON_LEFT and 180 > mouse[0] > 80 and 320 > mouse[1] > 220:
                    carro_img_2 = carro_amarelo
                    cart_2 = cart_amarela
                    dado_2 = dado_am
                    customizacao_2_adulto = False
                    modo_adulto = True
                    regra1 = True
                elif event.button == pygame.BUTTON_LEFT and 340 > mouse[0] > 240 and 320 > mouse[1] > 220:
                    carro_img_2 = carro_azul
                    cart_2 = cart_azul
                    dado_2 = dado_az
                    customizacao_2_adulto = False
                    modo_adulto = True
                    regra1 = True
                elif event.button == pygame.BUTTON_LEFT and 500 > mouse[0] > 400 and 320 > mouse[1] > 220:
                    carro_img_2 = carro_rosa
                    cart_2 = cart_rosa
                    dado_2 = dado_rosa
                    customizacao_2_adulto = False
                    modo_adulto = True
                    regra1 = True
                elif event.button == pygame.BUTTON_LEFT and 260 > mouse[0] > 160 and 450 > mouse[1] > 350:
                    carro_img_2 = carro_verde
                    cart_2 = cart_verde
                    dado_2 = dado_verde
                    customizacao_2_adulto = False
                    modo_adulto = True
                    regra1 = True
                elif event.button == pygame.BUTTON_LEFT and 420 > mouse[0] > 320 and 450 > mouse[1] > 350:
                    carro_img_2 = carro_cinza
                    cart_2 = cart_cinza
                    dado_2 = dado_cinza
                    customizacao_2_adulto = False
                    modo_adulto = True
                    regra1 = True


    while modo_adulto:

        mouse = pygame.mouse.get_pos()
        janela.blit(fundo_adulto, (0, 0))
        botao_mutar()

        if audio == True:
            musica_adulto = mixer.music.load('../audio/whatislove_8bit.wav')
            mixer.music.play(-1)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT and 600 > mouse[0] > 520 and 90 > mouse[1] > 10:
                        audio = False
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
            regra_adulto_6()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        regra6 = False
                        if num_jog == '1':
                            jogo_adulto = True
                        elif num_jog == '2':
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
                        escolha = random.choice(jogadores)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        sorteio = False
                        sorteado = True

                pygame.display.update()

        while sorteado:
            janela.blit(fundo_adulto, (0, 0))
            janela.blit(guarda_regras, (0, 0))
            sorteio1 = (fonte_botao.render('O primeiro a jogar será o {}!'.format(escolha), True, (0, 0, 0)))
            sorteio2 = (fonte_botao.render('Preste bastante atenção, tenha', True, (0, 0, 0)))
            sorteio3 = (fonte_botao.render('calma e boa sorte!', True, (0, 0, 0)))
            espaco = fonte_botao.render('Aperte espaço para continuar', True, (0, 0, 0))
            janela.blit(sorteio1, (50, 390))
            janela.blit(sorteio2, (50, 415))
            janela.blit(sorteio3, (50, 440))
            janela.blit(espaco, (80, 490))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        sorteado = False
                        jogo_adulto = True

            pygame.display.flip()

        while jogo_adulto:
            janela.blit(fundo_adulto, (0, 0))
            carro_jog_1()
            if num_jog == '2':
                carro_jog_2()
            menu_acesso()
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and escolha == 'Jogador 1':
                        dado = random.randint(1, 6)
                        ponteiro_1_perg += dado
                        ponteiro_1 += dado
                        dado_1_vez = pygame.image.load(dado_1[dado - 1])
                        janela.blit(dado_1_vez, (dado_x, dado_y))
                        pygame.display.update()
                        if ponteiro_1_perg in buracos:
                            if num_jog == '2':
                                escolha = 'Jogador 2'
                            buraco_casa = True
                        elif ponteiro_1_perg in perguntas:
                            pergunta_1 = True
                        elif ponteiro_1_perg in pontes:
                            ponteiro_1 += 4
                            ponteiro_1_perg += 4
                            pontes_casa = True
                    if num_jog == '2':
                        if event.key == pygame.K_SPACE and escolha == 'Jogador 2':
                            dado = random.randint(1, 6)
                            ponteiro_2_perg += dado
                            ponteiro_2 += dado
                            dado_2_vez = pygame.image.load(dado_2[dado - 1])
                            janela.blit(dado_2_vez, (dado_x, dado_y))
                            pygame.display.update()
                            if ponteiro_2_perg in buracos:
                                escolha = 'Jogador 1'
                                buraco_casa = True
                            elif ponteiro_2_perg in perguntas:
                                pergunta_2 = True
                            elif ponteiro_2_perg in pontes:
                                ponteiro_2 += 4
                                ponteiro_2_perg += 4
                                pontes_casa = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT and 585 > mouse[0] > 510 and 47 > mouse[1] > 20:
                        opcoes = True

            if pontos_1 >= 40:
                perdedor = 'Jogador 1'
                vencedor = 'Jogador 2'
                jogo_adulto = False
                fim_jogo = True
                pygame.quit()
            if num_jog == '2':
                if pontos_2 >= 40:
                    perdedor = 'Jogador 2'
                    vencedor = 'Jogador 1'
                    jogo_adulto = False
                    fim_jogo = True

            if ponteiro_1_perg > 30 and pontos_2 < 40 and pontos_1 < 40:
                ponteiro_1_perg = 0
                ponteiro_1_perg += dado
            if num_jog == '2':
                if ponteiro_2_perg > 30 and pontos_2 < 40 and pontos_1 < 40:
                    ponteiro_2_perg = 0
                    ponteiro_2_perg += dado

            if ponteiro_1 >= 30:
                ponteiro_1 = 0
                ponteiro_1 += dado
            if num_jog == '2':
                if ponteiro_2 >= 30:
                    ponteiro_2 = 0
                    ponteiro_2 += dado

                # Placar de pontos
            show_points_1 = str(pontos_1)
            carteira_1()
            show_text(show_points_1, 45, 525, 30, (0, 0, 0))
            if num_jog == '2':
                show_points_2 = str(pontos_2)
                carteira_2()
                show_text(show_points_2, 155, 525, 30, (0, 0, 0))

            pygame.display.update()

            while opcoes:
                janela.blit(fundo_adulto, (0, 0))
                menu_peq()
                botao_mutar()
                botao_voltar()
                carro_jog_1()
                if num_jog == '2':
                    carro_jog_2()
                mouse = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == pygame.BUTTON_LEFT and 405 > mouse[0] > 390 and 235 > mouse[1] > 225:
                            opcoes = False
                        elif event.button == pygame.BUTTON_LEFT and 285 > mouse[0] > 205 and 337 > mouse[1] > 257 and (
                                mut % 2) == 0:
                            pygame.mixer_music.pause()
                            mut += 1
                        elif event.button == pygame.BUTTON_LEFT and 285 > mouse[0] > 205 and 337 > mouse[1] > 257 and (
                                mut % 2) != 0:
                            pygame.mixer_music.unpause()
                            mut += 1
                        elif event.button == pygame.BUTTON_LEFT and 395 > mouse[0] > 315 and 337 > mouse[1] > 257:
                            if audio == True:
                                pygame.mixer_music.stop()
                            opcoes = False
                            modo_adulto = False
                            jogo_adulto = False
                            ponteiro_1 = 0
                            ponteiro_1_perg = 0
                            pontos_1 = 0
                            escolha_modo = True
                            num_jog = ''
                            esc_modo = 0
                            if num_jog == '2':
                                ponteiro_2 = 0
                                ponteiro_2_perg = 0
                                pontos_2 = 0

                        pygame.display.flip()
                    pygame.display.update()
                pygame.display.update()

            while pergunta_1:
                choice = ''
                janela.blit(fundo_adulto, (0, 0))
                janela.blit(perg_box, (0, 0))
                janela.blit(dado_1_vez, (dado_x, dado_y))
                ask_values = ask_1(ponteiro_1_perg)
                answer = ask_values["answer"]  # Resposta
                difficulty = ask_values["difficulty"]  # Dificuldade
                placas_dif()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()
                        # Posição dos botões
                        if event.button == pygame.BUTTON_LEFT and (
                                x < mouse[0] < x + largura and y[0] < mouse[1] < y[0] + altura):
                            choice = 'A'
                        elif event.button == pygame.BUTTON_LEFT and (
                                x < mouse[0] < x + largura and y[1] < mouse[1] < y[1] + altura):
                            choice = 'B'
                        elif event.button == pygame.BUTTON_LEFT and (
                                x < mouse[0] < x + largura and y[2] < mouse[1] < y[2] + altura):
                            choice = 'C'
                        elif event.button == pygame.BUTTON_LEFT and (
                                x < mouse[0] < x + largura and y[3] < mouse[1] < y[3] + altura):
                            choice = 'D'
                        if choice == answer:
                            pergunta_1 = False
                            acerto_1 = True
                        else:
                            if difficulty == "Fácil":
                                pontos_1 += 3
                                pergunta_1 = False
                                erro_1_f = True
                            elif difficulty == "Médio":
                                pontos_1 += 4
                                pergunta_1 = False
                                erro_1_m = True
                            elif difficulty == "Difícil":
                                pontos_1 += 5
                                pergunta_1 = False
                                erro_1_d = True
                            elif difficulty == 'Muito difícil':
                                pontos_1 += 7
                                pergunta_1 = False
                                erro_1_md = True

                        ask_1(ponteiro_1_perg)

                        pygame.display.flip()
                    pygame.display.update()
                pygame.display.update()

            while pergunta_2:
                choice = ''
                janela.blit(fundo_adulto, (0, 0))
                janela.blit(perg_box, (0, 0))
                janela.blit(dado_2_vez, (dado_x, dado_y))
                ask_values = ask_2(ponteiro_2_perg)
                answer = ask_values["answer"]  # Resposta
                difficulty = ask_values["difficulty"]  # Dificuldade
                placas_dif()
                for event in pygame.event.get():
                    # Quit game
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()
                        # Posição dos botões
                        if event.button == pygame.BUTTON_LEFT and (
                                x < mouse[0] < x + largura and y[0] < mouse[1] < y[0] + altura):
                            choice = 'A'
                        elif event.button == pygame.BUTTON_LEFT and (
                                x < mouse[0] < x + largura and y[1] < mouse[1] < y[1] + altura):
                            choice = 'B'
                        elif event.button == pygame.BUTTON_LEFT and (
                                x < mouse[0] < x + largura and y[2] < mouse[1] < y[2] + altura):
                            choice = 'C'
                        elif event.button == pygame.BUTTON_LEFT and (
                                x < mouse[0] < x + largura and y[3] < mouse[1] < y[3] + altura):
                            choice = 'D'
                        if choice == answer:
                            pergunta_2 = False
                            acerto_2 = True
                        else:
                            if difficulty == "Fácil":
                                pontos_2 += 3
                                pergunta_2 = False
                                erro_2_f = True
                            elif difficulty == "Médio":
                                pontos_2 += 4
                                pergunta_2 = False
                                erro_2_m = True
                            elif difficulty == "Difícil":
                                pontos_2 += 5
                                pergunta_2 = False
                                erro_2_d = True
                            elif difficulty == 'Muito difícil':
                                pontos_2 += 7
                                pergunta_2 = False
                                erro_2_md = True

                            pygame.display.flip()
                        ask_2(ponteiro_2_perg)

                        pygame.display.flip()
                    pygame.display.update()

            while acerto_1:
                escolha = 'Jogador 1'
                janela.blit(fundo_adulto, (0, 0))
                acerto()
                carro_jog_1()
                if num_jog == '2':
                    carro_jog_2()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            acerto_1 = False
                            jogo_adulto = True

                pygame.display.update()

            while acerto_2:
                escolha = 'Jogador 2'
                janela.blit(fundo_adulto, (0, 0))
                acerto()
                carro_jog_1()
                carro_jog_2()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            acerto_2 = False
                            jogo_adulto = True

                pygame.display.update()

            while erro_1_f:
                if num_jog == '1':
                    escolha = 'Jogador 1'
                elif num_jog == '2':
                    carro_jog_2()
                    escolha = 'Jogador 2'
                janela.blit(fundo_adulto, (0, 0))
                erro()
                carro_jog_1()
                if num_jog == '2':
                    carro_jog_2()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            erro_1_f = False
                            jogo_adulto = True

                pygame.display.update()

            while erro_1_m:
                if num_jog == '1':
                    escolha = 'Jogador 1'
                elif num_jog == '2':
                    carro_jog_2()
                    escolha = 'Jogador 2'
                janela.blit(fundo_adulto, (0, 0))
                erro()
                carro_jog_1()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            erro_1_m = False
                            jogo_adulto = True

                pygame.display.update()

            while erro_1_d:
                if num_jog == '1':
                    escolha = 'Jogador 1'
                elif num_jog == '2':
                    carro_jog_2()
                    escolha = 'Jogador 2'
                janela.blit(fundo_adulto, (0, 0))
                erro()
                carro_jog_1()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            erro_1_d = False
                            jogo_adulto = True

                pygame.display.update()

            while erro_1_md:
                if num_jog == '1':
                    escolha = 'Jogador 1'
                elif num_jog == '2':
                    escolha = 'Jogador 2'
                    carro_jog_2()
                janela.blit(fundo_adulto, (0, 0))
                erro()
                carro_jog_1()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            erro_1_md = False
                            jogo_adulto = True

                pygame.display.update()

            while erro_2_f:
                escolha = 'Jogador 1'
                janela.blit(fundo_adulto, (0, 0))
                erro()
                carro_jog_1()
                carro_jog_2()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            erro_2_f = False
                            jogo_adulto = True

                pygame.display.update()

            while erro_2_m:
                escolha = 'Jogador 1'
                janela.blit(fundo_adulto, (0, 0))
                erro()
                carro_jog_1()
                carro_jog_2()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            erro_2_m = False
                            jogo_adulto = True

                pygame.display.update()

            while erro_2_d:
                escolha = 'Jogador 1'
                janela.blit(fundo_adulto, (0, 0))
                erro()
                carro_jog_1()
                carro_jog_2()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            erro_2_d = False
                            jogo_adulto = True

                pygame.display.update()

            while erro_2_md:
                escolha = 'Jogador 1'
                janela.blit(fundo_adulto, (0, 0))
                janela.blit(mens_box, (150, 150))
                erro()
                carro_jog_1()
                carro_jog_2()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            erro_2_md = False
                            jogo_adulto = True

                pygame.display.update()

            while buraco_casa:
                janela.blit(fundo_adulto, (0, 0))
                janela.blit(mens_box, (150, 150))
                if num_jog == '2':
                    carro_jog_2()
                    if escolha == 'Jogador 2':
                        janela.blit(dado_1_vez, (dado_x, dado_y))
                    elif escolha == 'Jogador 1':
                        janela.blit(dado_2_vez, (dado_x, dado_y))
                buraco()
                carro_jog_1()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            buraco_casa = False
                            jogo_adulto = True

                pygame.display.update()

            while pontes_casa:
                janela.blit(fundo_adulto, (0, 0))
                janela.blit(mens_box, (150, 150))
                ponte()
                carro_jog_1()
                if num_jog == '2':
                    carro_jog_2()
                if escolha == 'Jogador 1':
                    janela.blit(dado_1_vez, (dado_x, dado_y))
                elif escolha == 'Jogador 2':
                    janela.blit(dado_2_vez, (dado_x, dado_y))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            pontes_casa = False
                            jogo_adulto = True

                pygame.display.update()

        while fim_jogo:
            janela.blit(fundo_adulto, (0, 0))
            fim()
            if audio == True:
                pygame.mixer.stop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        jogo_adulto = False
                        modo_adulto = False
                        fim_jogo = False
                        menu = True

            pygame.display.flip()