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
        pygame.draw.line(screen, (20, 0, 40), (-1080 + 150 * i + grid_pos + 20, 1080), (0 + 150 * i + grid_pos + 20, 0), 2)
        pygame.draw.line(screen, (20, 0, 40), (3000 - 150 * i + grid_pos + 20, 1080), (1920 - 150 * i + grid_pos + 20, 0), 2)

        pygame.draw.line(screen, (20, 0, 40), (-1080 + 150 * i + grid_pos - 20, 1080), (0 + 150 * i + grid_pos - 20, 0), 2)
        pygame.draw.line(screen, (20, 0, 40), (3000 - 150 * i + grid_pos - 20, 1080), (1920 - 150 * i + grid_pos - 20, 0), 2)

        # вторая сетка (движется влево)
        # основные линии
        pygame.draw.line(screen, (20, 0, 40), (-1080 + 300 * i - grid_pos, 1080), (0 + 300 * i - grid_pos, 0), 8)
        pygame.draw.line(screen, (20, 0, 40), (3000 - 300 * i - grid_pos, 1080), (1920 - 300 * i - grid_pos, 0), 8)

        # дополнительные линии
        pygame.draw.line(screen, (20, 0, 40), (-1080 + 150 * i - grid_pos - 20, 1080), (0 + 150 * i - grid_pos - 20, 0), 2)
        pygame.draw.line(screen, (20, 0, 40), (3000 - 150 * i - grid_pos - 20, 1080), (1920 - 150 * i - grid_pos - 20, 0), 2)

        pygame.draw.line(screen, (20, 0, 40), (-1080 + 150 * i - grid_pos + 20, 1080), (0 + 150 * i - grid_pos + 20, 0), 2)
        pygame.draw.line(screen, (20, 0, 40), (3000 - 150 * i - grid_pos + 20, 1080), (1920 - 150 * i - grid_pos + 20, 0), 2)


def draw_board(screen, board):
    pygame.draw.rect(screen, (5, 0, 10), ((LEFT, TOP), (CELL * 10, CELL * 18)))
    [pygame.draw.rect(screen, (10, 0, 20), rectangle, 1) for rectangle in board]
    pygame.draw.rect(screen, "white", ((LEFT - 3, TOP - 3), (CELL * 10 + 6, CELL * 18 + 6)), 2)
    pygame.draw.rect(screen, "white", ((LEFT - 15, TOP - 15), (CELL * 10 + 30, CELL * 18 + 30)), 5)


def draw_text(screen, best, score):
    left = 800
    right = 1220
    f1 = pygame.font.Font('data/LCD5x8HRU.ttf', 100)
    f2 = pygame.font.Font('data/long_pixel-7.ttf', 25)

    header = f1.render('Тетрис', True, "white")
    best_score = f2.render(f'Лучший результат: {best}', True, "white")
    now_score = f2.render(f'Текущий результат: {score}', True, "white")
    next_shape = f2.render('Следующая фигура:', True, "white")
    pause_text1 = f2.render('Чтобы поставить на паузу,', True, "white")
    pause_text2 = f2.render('нажмите кнопку P (англ.)', True, "white")
    exit_text1 = f2.render('Чтобы выйти из игры', True, "white")
    exit_text2 = f2.render('нажмите кнопку X (англ.)', True, "white")

    pygame.draw.rect(screen, (5, 0, 10), ((1200, 250), (400, 600)))
    pygame.draw.rect(screen, "white", ((1200, 250), (400, 600)), 2)

    screen.blit(header, (left - 50, 125))
    screen.blit(best_score, (right, 270))
    screen.blit(now_score, (right, 330))
    screen.blit(next_shape, (right, 390))
    screen.blit(pause_text1, (right, 650))
    screen.blit(pause_text2, (right, 700))
    screen.blit(exit_text1, (right, 760))
    screen.blit(exit_text2, (right, 810))


def draw_pause(screen):
    pygame.draw.rect(screen, (5, 0, 10), ((LEFT, TOP), (CELL * 10, CELL * 18)))
    f3 = pygame.font.Font('data/long_pixel-7.ttf', 80)
    pause_text = f3.render('ИГРА НА', True, 'white')
    pause_text2 = f3.render('ПАУЗЕ', True, 'white')
    screen.blit(pause_text, (LEFT + 20, TOP + 20))
    screen.blit(pause_text2, (LEFT + 20, TOP + 120))

def draw_gameover(screen):
    pygame.draw.rect(screen, (5, 0, 10), ((LEFT, TOP), (CELL * 10, CELL * 18)))
    f3 = pygame.font.Font('data/long_pixel-7.ttf', 80)
    pause_text = f3.render('ИГРА ', True, 'white')
    pause_text2 = f3.render('ОКОНЧЕНА', True, 'white')
    screen.blit(pause_text, (LEFT + 20, TOP + 20))
    screen.blit(pause_text2, (LEFT + 20, TOP + 120))


def tetris():
    pygame.init()
    pygame.display.set_caption('Тетрис')
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 60

    # поле для отрисовки
    board = [pygame.Rect(LEFT + x * CELL, TOP + y * CELL, CELL, CELL) for x in range(BWIDTH) for y in range(BHEIGHT)]
    # поле для хранения занятых клеток (0 - пусто, иначе цвет)
    field = [[0 for _ in range(BWIDTH)] for _ in range(BHEIGHT)]

    # координаты фигур (относительно центра вращения)
    shapes_coords = [
        [(-1, 0), (-2, 0), (0, 0), (1, 0)],         # I-образная
        [(0, -1), (-1, -1), (-1, 0), (0, 0)],         # квадрат
        [(-1, 0), (-1, 1), (0, 0), (0, -1)],           # S-образная
        [(0, 0), (-1, 0), (0, 1), (-1, -1)],           # обратная S
        [(0, 0), (0, -1), (0, 1), (-1, -1)],           # Г-образная
        [(0, 0), (0, -1), (0, 1), (1, -1)],            # обратная Г
        [(0, 0), (0, -1), (0, 1), (-1, 0)]             # T-образная
    ]

    # функция для создания новой фигуры
    def new_shape():
        coords = random.choice(shapes_coords)
        return [pygame.Rect(x + BWIDTH // 2, y - 2, 1, 1) for x, y in coords]

    # начальные фигура и следующая фигура
    shape = new_shape()
    shape_color = (random.choice(range(100, 200)), 0, random.choice(range(100, 200)))
    next_shape = new_shape()
    next_shape_color = (random.choice(range(100, 200)), 0, random.choice(range(100, 200)))

    shape_rect = pygame.Rect(0, 0, CELL - 2, CELL - 2)

    anim_count, anim_speed, anim_limit = 0, 60, 2000

    score = 0
    best = 0
    grid_pos = 0
    paused = False
    gameover = False
    normal_anim_speed = anim_speed

    running = True
    while running:
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
                    anim_limit = 500  # ускоряем падение
                elif event.key == pygame.K_p:
                    if not paused:
                        normal_anim_speed = anim_speed
                        anim_speed = 0
                        paused = True
                    else:
                        anim_speed = normal_anim_speed
                        paused = False
                elif event.key == pygame.K_x:
                    return
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    anim_limit = 2000

        # горизонтальное перемещение
        if movex:
            # сначала делаем копию для проверки
            moved = [block.copy() for block in shape]
            for block in moved:
                block.x += movex
            valid = True
            for block in moved:
                # проверяем наа выход за границы
                if block.x < 0 or block.x >= BWIDTH:
                    valid = False
                    break
                # проверяем на контакт с другими фигурами
                if block.y >= 0 and field[block.y][block.x]:
                    valid = False
                    break
            if valid:
                for block in shape:
                    block.x += movex

        # вертикальное перемещение
        anim_count += anim_speed
        if anim_count > anim_limit:
            anim_count = 0
            # сдвиг фигуры вниз
            for block in shape:
                block.y += 1

            collision = False
            for block in shape:
                # если блок выходит за нижнюю границу или попадает в занятую клетку
                if block.y >= BHEIGHT or (block.y >= 0 and field[block.y][block.x]):
                    collision = True
                    break

            if collision:
                # Отменяем сдвиг вниз
                for block in shape:
                    block.y -= 1
                # Фиксируем фигуру в поле
                for block in shape:
                    if block.y < 0:
                        # Если фигура зафиксировалась вне поля – игра окончена
                        gameover = True
                        anim_speed = 0
                    else:
                        field[block.y][block.x] = shape_color

                # генерируем следующую фигуру
                shape = next_shape
                shape_color = next_shape_color
                next_shape = new_shape()
                next_shape_color = (random.choice(range(100, 200)), 0, random.choice(range(100, 200)))
                anim_limit = 2000

        grid_pos += 1
        if grid_pos >= 300:
            grid_pos = 0

        draw_background(screen, grid_pos)
        draw_board(screen, board)
        draw_text(screen, best, score)

        # рисуем следующую фигуру
        for block in next_shape:
            shape_rect.x = LEFT + 1 + block.x * CELL + 1170 - LEFT
            shape_rect.y = TOP + 1 + block.y * CELL + 320
            pygame.draw.rect(screen, next_shape_color, shape_rect)

        # рисуем текущую фигуру
        for block in shape:
            shape_rect.x = LEFT + 1 + block.x * CELL
            shape_rect.y = TOP + 1 + block.y * CELL
            if block.y >= 0:
                pygame.draw.rect(screen, shape_color, shape_rect)

        # рисуем установленные в поле блоки
        for y, row in enumerate(field):
            for x, col in enumerate(row):
                if col:
                    pygame.draw.rect(screen, col, ((LEFT + CELL * x + 1, TOP + CELL * y + 1), (CELL - 2, CELL - 2)))

        for y, row in enumerate(field):
            flag = True
            for cell in row:
                if cell == 0:
                    flag = False
                    break
            if flag:
                field.remove(field[y])
                field.insert(0, [0] * BWIDTH)


        if paused:
            draw_pause(screen)
        if gameover:
            draw_gameover(screen)

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
