import pygame, random
from questions import Data

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((600, 600))
name = pygame.display.set_caption(('Manual das Ruas'))
runing = True
sorteio = True
texto_sorteio = 'Aperte TAB em seu teclado para efetuar o sorteio!'
jogo = False


x = 50
y = [70, 130, 190, 250]
largura = 500
altura = 50

perguntas = [2, 3, 4, 5, 7, 9, 10, 11, 12, 14, 15, 16, 19, 21, 22, 24, 25, 28, 29, 30]
buracos = [1, 6, 8, 13, 17, 18, 20, 23, 26, 27]
# Só mudar o valor de "case" para escolher a pergunta
case = 0
choice = ''
points_am = 0
points_az = 0
escolha = ''
jogadores = ['Amarelo', 'Azul']
###########################################################################################

def show_text(txt, x, y, width, color):
    sys_font = pygame.font.SysFont('None', width)
    wrap = txt.find('  ')

    if wrap > 0:
        top_text = sys_font.render(txt[:wrap], True, color)
        bottom_text = sys_font.render(txt[wrap:], True, color)
        screen.blit(top_text, (x, y - 9))
        screen.blit(bottom_text, (x, y + 9))
    else:
        text = sys_font.render(txt, True, color)
        screen.blit(text, (x, y))


def ask(number):
    for key, value in Data.items():
        # Informa a chave da pergunta e o seu valor
        if case in perguntas:

            pygame.draw.rect(screen, (50, 137, 168), (x, y[0], largura, altura))
            pygame.draw.rect(screen, (50, 137, 168), (x, y[1], largura, altura))
            pygame.draw.rect(screen, (50, 137, 168), (x, y[2], largura, altura))
            pygame.draw.rect(screen, (50, 137, 168), (x, y[3], largura, altura))

            if key == number:
                question = '{0}: {1}'.format(key, value['question'])
                show_text(question, 10, 15, 20, (0, 0, 0))

                # Show options
                show_text(('[A]: {}'.format(value["options"]["A"])), (x + 10), (y[0] + 18), 20, (255, 255, 255))
                show_text(('[B]: {}'.format(value["options"]["B"])), (x + 10), (y[1] + 18), 20, (255, 255, 255))
                show_text(('[C]: {}'.format(value["options"]["C"])), (x + 10), (y[2] + 18), 20, (255, 255, 255))
                show_text(('[D]: {}'.format(value["options"]["D"])), (x + 10), (y[3] + 18), 20, (255, 255, 255))

                return value

###########################################################################################

while runing:

        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            # Quit game
            if event.type == pygame.QUIT:
                runing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB and escolha == '':
                    escolha = random.choice(jogadores)
                    print('O primeiro a jogar será o: {}!'.format(escolha))
                if event.key == pygame.K_SPACE and escolha == 'Amarelo':
                    dado = random.randint(1, 6)
                    case += dado
                    pygame.display.update()
                elif event.key == pygame.K_SPACE and escolha == 'Azul':
                    dado = random.randint(1, 6)
                    case += dado
                    pygame.display.flip()
            # Evento de Click
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                # Posição dos botões
                if (x < mouse[0] < x + largura and y[0] < mouse[1] < y[0] + altura):
                    choice = 'A'
                elif (x < mouse[0] < x + largura and y[1] < mouse[1] < y[1] + altura):
                    choice = 'B'
                elif (x < mouse[0] < x + largura and y[2] < mouse[1] < y[2] + altura):
                    choice = 'C'
                elif (x < mouse[0] < x + largura and y[3] < mouse[1] < y[3] + altura):
                    choice = 'D'

                # Pegando os valores da função
                ask_values = ask(case)
                answer = ask_values["answer"]  # Resposta
                difficulty = ask_values["difficulty"]  # Dificuldade

                # Conferindo a resposta
                if escolha == 'Amarelo':
                    if case in perguntas:
                        if choice == answer:
                            print("Certa resposta! Amarelo joga novamente")
                        else:
                            if difficulty == "Fácil":
                                points_am += 3
                                escolha = 'Azul'
                            elif difficulty == "Médio":
                                points_am += 4
                                escolha = 'Azul'
                            elif difficulty == "Difícil":
                                points_am += 5
                                escolha = 'Azul'
                            elif difficulty == 'Muito difícil':
                                points_am += 7
                                escolha = 'Azul'
                            print("Você errou, a resposta correta era [{}]".format(answer))
                            print('Vez do Azul! Por favor, jogue o dado.')
                    elif case in buracos:
                        escolha = 'Azul'
                        print('Buraco! Vez do {}'.format(escolha))
                elif escolha == 'Azul':
                    if case in perguntas:
                        if choice == answer:
                            print("Certa resposta! Azul joga novamente")
                        else:
                            if difficulty == "Fácil":
                                points_az += 3
                                escolha = 'Amarelo'
                            elif difficulty == "Médio":
                                points_az += 4
                                escolha = 'Amarelo'
                            elif difficulty == "Difícil":
                                points_az += 5
                                escolha = 'Amarelo'
                            elif difficulty == 'Muito difícil':
                                points_az += 7
                                escolha = 'Amarelo'
                            print("Você errou, a resposta correta era [{}]".format(answer))
                            print('Vez do Amarelo! Por favor, jogue o dado.')
                    elif case in buracos:
                        print(case)
                        escolha = 'Amarelo'
                        print('Buraco! Vez do {}'.format(escolha))

        if points_am >= 40:
            print('Fim de jogo. Vitória do azul!')
            pygame.quit()
        elif points_az >= 40:
            print('Fim de jogo. Vitória do amarelo!')

        if case > 30 and points_az < 40 and points_am < 40:
            case = 0


            # Placar de pontos
        show_points_am = "Carteira amarela: " + str(points_am)
        show_points_az = "Carteira azul: " + str(points_az)
        show_text(show_points_am, 10, 580, 25, (0, 0, 0))
        show_text(show_points_az, 460, 580, 25, (0, 0, 0))
        # Chamando a função e atualizando o display a cada lopping
        ask(case)
        pygame.display.update()

