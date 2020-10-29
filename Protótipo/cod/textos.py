import pygame
pygame.init()

#Fontes
fonte_tit = pygame.font.Font('../font/PressStart2P-vaV7.ttf', 26)
fonte_botao = pygame.font.Font('../font/PressStart2P-vaV7.ttf', 12)

#Textos
acerto1 = (fonte_botao.render('Parabéns! Você', True, (0, 0, 0)))
acerto2 = (fonte_botao.render('acertou!', True, (0, 0, 0)))
pontos = ''
erro1 = (fonte_botao.render('Você cometeu', True, (0, 0, 0)))
erro2 = (fonte_botao.render('uma infração leve!', True, (0, 0, 0)))
pontos1 = (fonte_botao.render('Agora você possui', True, (0, 0, 0)))
buraco1 = (fonte_botao.render('Que pena!', True, (0, 0, 0)))
buraco2 = (fonte_botao.render('Você caiu no buraco!', True, (0, 0, 0)))
ponte1 = (fonte_botao.render('Olhe só! Você', True, (0, 0, 0)))
ponte2 = (fonte_botao.render('encontrou uma ponte!', True, (0, 0, 0)))
pulo1 = (fonte_botao.render('Por isso, você pode', True, (0, 0, 0)))
pulo2 = (fonte_botao.render('avançar 4 casas!', True, (0, 0, 0)))
vez2 = (fonte_botao.render('Pode jogar o dado.', True, (0, 0, 0)))
espaco = fonte_botao.render('Aperte espaço para voltar ao menu.', True, (0, 0, 0))
espaco_1 = fonte_botao.render('Aperte espaço', True, (0, 0, 0))
espaco_2 = fonte_botao.render('para continuar', True, (0, 0, 0))
