import pygame

pygame.init()#inicia o pygame
pygame.mixer.music.load('Quando_a_chuva_passar.m4a')#carrega a música
pygame.mixer.music.play()
pygame.event.wait()
