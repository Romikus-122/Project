import os
import sys

import pygame


def draw_background(screen, grid_pos):
    screen.fill((10, 0, 20))
    for i in range(20):
        # первая сетка (движется вправо)
        pygame.draw.line(screen, (20, 0, 40), (-1080 + 300 * i + grid_pos, 1080), (0 + 300 * i + grid_pos, 0), 4)
        pygame.draw.line(screen, (20, 0, 40), (3000 - 300 * i + grid_pos, 1080), (1920 - 300 * i + grid_pos, 0), 4)
        pygame.draw.line(screen, (20, 0, 40), (-1080 + 150 * i + grid_pos + 40, 1080), (0 + 150 * i + grid_pos + 40, 0), 2)
        pygame.draw.line(screen, (20, 0, 40), (3000 - 150 * i + grid_pos + 40, 1080), (1920 - 150 * i + grid_pos + 40, 0), 2)

        # вторая сетка (движется влево)
        pygame.draw.line(screen, (20, 0, 40), (-1080 + 300 * i - grid_pos, 1080), (0 + 300 * i - grid_pos, 0), 4)
        pygame.draw.line(screen, (20, 0, 40), (3000 - 300 * i - grid_pos, 1080), (1920 - 300 * i - grid_pos, 0), 4)
        pygame.draw.line(screen, (20, 0, 40), (-1080 + 150 * i - grid_pos - 40, 1080), (0 + 150 * i - grid_pos - 40, 0), 2)
        pygame.draw.line(screen, (20, 0, 40), (3000 - 150 * i - grid_pos - 40, 1080), (1920 - 150 * i - grid_pos - 40, 0), 2)


def draw_board(screen):
    left = 750
    top = 250
    cell = 40
    pygame.draw.rect(screen, (5, 0, 10), ((left, top), (cell * 10, cell * 18)))
    for i in range(18):
        for j in range(10):
            pygame.draw.rect(screen, (10, 0, 20),
                             ((left + cell * j, top + cell * i), (cell, cell)), 1)
            pygame.draw.rect(screen, "white", ((left - 3, top - 3), (cell * 10 + 6, cell * 18 + 6)), 2)
            pygame.draw.rect(screen, "white", ((left - 15, top - 15), (cell * 10 + 30, cell * 18 + 30)), 5)


def draw_text(screen, best, score):
# инициализация текста
    left = 800
    right = 1220
    f1 = pygame.font.Font(None, 135)
    f2 = pygame.font.Font(None, 40)

    header = f1.render('Тетрис', 0, "white")
    best_score = f2.render(f'Лучший результат: {best}', 0, "white")
    now_score = f2.render(f'Текущий результат: {score}', 0, "white")
    next_shape = f2.render('Следующая фигура:', 0, "white")
    pause_text1 = f2.render('Чтобы поставить на паузу,', 0, "white")
    pause_text2 = f2.render('нажмите кнопку P', 0, "white")

# перекрывающий фон холст для текста
    pygame.draw.rect(screen, (5, 0, 10), ((1200, 250), (400, 500)))
    pygame.draw.rect(screen, "white", ((1200, 250), (400, 500)), 2)

# отрисовка текста
    screen.blit(header, (left, 125))
    screen.blit(best_score, (right, 270))
    screen.blit(now_score, (right, 330))
    screen.blit(next_shape, (right, 390))
    screen.blit(pause_text1, (right, 650))
    screen.blit(pause_text2, (right, 700))


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
    grid_pos = 0
    fps = 60

    score = 0
    best = 0

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        grid_pos += 1
        if grid_pos >= 300:
            grid_pos = 0
        draw_background(screen, grid_pos)

        draw_board(screen)
        draw_text(screen, best, score)
        pygame.display.flip()
