import pygame
from pygame import mixer
pygame.init()

buzina = mixer.Sound('../audio/buzina_intro.wav')
motor = mixer.Sound('../audio/motor_abertura.wav')
musica_infantil = mixer.music.load('../audio/signal_8bit.wav')
musica_adulto = mixer.music.load('../audio/whatislove_8bit.wav')