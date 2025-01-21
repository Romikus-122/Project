import os
import sys

import pygame


def draw_board(screen):
    left = 800
    top = 300
    cell = 40
    for i in range(15):
        for j in range(8):
            pygame.draw.rect(screen, (16, 16, 16),
                             ((left + cell * j, top + cell * i), (cell, cell)), 1)
            pygame.draw.rect(screen, "white", ((left - 3, top - 3), (cell * 8 + 6, cell * 15 + 6)), 2)
            pygame.draw.rect(screen, "white", ((left - 15, top - 15), (cell * 8 + 30, cell * 15 + 30)), 5)


def draw_text(screen):
    left = 300
    right = 1220
    f1 = pygame.font.Font(None, 135)
    header = f1.render('Тетрис', 0, "white")
    screen.blit(header, (800, 175))


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
        draw_board(screen)
        draw_text(screen)
        pygame.display.flip()
