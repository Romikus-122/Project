import os
import random
import sys

import pygame

WIDTH = 1920
HEIGHT = 1080
CELL = 40
BWIDTH = 10
BHEIGHT = 18
LEFT = 750
TOP = 250


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

def draw_background(screen, grid_pos):
    screen.fill((10, 0, 20))
    for i in range(20):
        # первая сетка (движется вправо)
        # основные линии
        pygame.draw.line(screen, (20, 0, 40), (-1080 + 300 * i + grid_pos, 1080), (0 + 300 * i + grid_pos, 0), 8)
        pygame.draw.line(screen, (20, 0, 40), (3000 - 300 * i + grid_pos, 1080), (1920 - 300 * i + grid_pos, 0), 8)

        # дополнительные линии
        pygame.draw.line(screen, (20, 0, 40), (-1080 + 150 * i + grid_pos + 20, 1080), (0 + 150 * i + grid_pos + 20, 0),
                         2)
        pygame.draw.line(screen, (20, 0, 40), (3000 - 150 * i + grid_pos + 20, 1080),
                         (1920 - 150 * i + grid_pos + 20, 0), 2)

        pygame.draw.line(screen, (20, 0, 40), (-1080 + 150 * i + grid_pos - 20, 1080), (0 + 150 * i + grid_pos - 20, 0),
                         2)
        pygame.draw.line(screen, (20, 0, 40), (3000 - 150 * i + grid_pos - 20, 1080),
                         (1920 - 150 * i + grid_pos - 20, 0), 2)

        # вторая сетка (движется влево)
        # основные линии
        pygame.draw.line(screen, (20, 0, 40), (-1080 + 300 * i - grid_pos, 1080), (0 + 300 * i - grid_pos, 0), 8)
        pygame.draw.line(screen, (20, 0, 40), (3000 - 300 * i - grid_pos, 1080), (1920 - 300 * i - grid_pos, 0), 8)

        # дополнительные линии
        pygame.draw.line(screen, (20, 0, 40), (-1080 + 150 * i - grid_pos - 20, 1080), (0 + 150 * i - grid_pos - 20, 0),
                         2)
        pygame.draw.line(screen, (20, 0, 40), (3000 - 150 * i - grid_pos - 20, 1080),
                         (1920 - 150 * i - grid_pos - 20, 0), 2)

        pygame.draw.line(screen, (20, 0, 40), (-1080 + 150 * i - grid_pos + 20, 1080), (0 + 150 * i - grid_pos + 20, 0),
                         2)
        pygame.draw.line(screen, (20, 0, 40), (3000 - 150 * i - grid_pos + 20, 1080),
                         (1920 - 150 * i - grid_pos + 20, 0), 2)



def draw_board(screen, board):
    pygame.draw.rect(screen, (5, 0, 10), ((LEFT, TOP), (CELL * 10, CELL * 18)))
    [pygame.draw.rect(screen, (10, 0, 20), rectangle, 1) for rectangle in board]
    #for i in range(BHEIGHT):
        #for j in range(BWIDTH):
            #pygame.draw.rect(screen, (10, 0, 20),
                            # ((left + CELL * j, top + CELL * i), (CELL, CELL)), 1)
    pygame.draw.rect(screen, "white", ((LEFT - 3, TOP - 3), (CELL * 10 + 6, CELL * 18 + 6)), 2)
    pygame.draw.rect(screen, "white", ((LEFT - 15, TOP - 15), (CELL * 10 + 30, CELL * 18 + 30)), 5)


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

#def draw_shape(screen):
    #for i in range(4):
        #shape_rect.x =

def check_borders_x(x, y, field):
    if x < 0:
        return 1
    elif x > BWIDTH - 1:
        return -1
    else:
        return 0

def check_borders_y(x, y, field):
    if y > BHEIGHT - 1 or field[y][x]:
        return -1
    else:
        return 0



def tetris():
    pygame.init()
    pygame.display.set_caption('Тетрис')
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 60
    # поле для отрисовки
    board = [pygame.Rect(LEFT + x * CELL, TOP + y * CELL, CELL, CELL) for x in range(BWIDTH) for y in range(BHEIGHT)]
    # поле для хранения информации о фигурах
    field = [[0 for i in range(BHEIGHT)] for j in range(BHEIGHT)]

    shapes_coords = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
                      [(0, -1), (-1, -1), (-1, 0), (0, 0)],
                      [(-1, 0), (-1, 1), (0, 0), (0, -1)],
                      [(0, 0), (-1, 0), (0, 1), (-1, -1)],
                      [(0, 0), (0, -1), (0, 1), (-1, -1)],
                      [(0, 0), (0, -1), (0, 1), (1, -1)],
                      [(0, 0), (0, -1), (0, 1), (-1, 0)]]

    shapes = [[pygame.Rect(x + BWIDTH // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in shapes_coords]
    shape_rect = pygame.Rect(0, 0, CELL - 2, CELL - 2)

    shape = shapes[random.choice(range(7))]

    anim_count, anim_speed, anim_limit = 0, 60, 2000

    score = 0
    best = 0
    grid_pos = 0

    running = True
    while running:
        # передвижение по x
        movex = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movex = -1
                elif event.key == pygame.K_RIGHT:
                    movex = 1
                elif event.key == pygame.K_DOWN:
                    anim_limit = 500
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    anim_limit = 2000
        for i in range(4):
            shape[i].x += movex
            check_result = check_borders_x(shape[i].x, shape[i].x, field)
            if check_result:
                for j in range(4):
                    shape[j].x += check_result
        # передвижение по y
        anim_count += anim_speed
        if anim_count > anim_limit:
            anim_count = 0
            for i in range(4):
                shape[i].y += 1
                if check_borders_y(shape[i].y, shape[i].x, field):
                    for j in range(4):
                        field[shape[j].y, shape[j].x] = 'white'
                    shape = shapes[random.choice(range(7))]
                    anim_limit = 2000
                    break

        grid_pos += 1
        if grid_pos >= 300:
            grid_pos = 0

        draw_background(screen, grid_pos)
        draw_board(screen, board)
        draw_text(screen, best, score)

        for i in range(4):
            shape_rect.x = LEFT + 1 + shape[i].x * CELL
            shape_rect.y = TOP + 1 + shape[i].y * CELL
            pygame.draw.rect(screen, 'white', shape_rect)
        # рисуем поле
        for y, row in enumerate(field):
            for x, col in enumerate(row):
                if col:
                    shape_rect.x = LEFT + 1 + shape[i].x * CELL
                    shape_rect.y = TOP + 1 + shape[i].y * CELL
                    pygame.draw.rect(screen, 'white', shape_rect)

        pygame.display.flip()
        clock.tick(fps)
        # bieber
