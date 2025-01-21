import os
import sys

import pygame


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def tetris():
    pygame.init()
    pygame.display.set_caption('Тетрис')
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    fps = 60

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
#тестовый коммит !!!
        pygame.display.flip()