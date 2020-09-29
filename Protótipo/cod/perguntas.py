import pygame, questions

mens_box = pygame.image.load('../img/img_jog_car/mens_box.png')
fonte_pergunta = pygame.font.Font('../font/PressStart2P-vaV7.ttf', 12)
fonte_resposta = pygame.font.Font('../font/PressStart2P-vaV7.ttf', 10)


def pergunta():
    janela.blit(mens_box, (150,150))
    questao = (fonte_pergunta.render(question[], True, (0, 0, 0)))
