import pygame
pygame.init()
pygame.mixer.music.load('stay.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('Pressione enter para parar a música.')

