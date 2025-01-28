import os
import sys
import random

import pygame


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class obv(pygame.sprite.Sprite):
    image = load_image('обводка.png')

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = obv.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, mem):
        self.rect.y = mem


def tanks():
    # загрузка
    pygame.init()
    pygame.display.set_caption('Денди танчики')
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    fps = 60

    clock = pygame.time.Clock()
    screen.fill((0, 0, 0))
    ini = 0
    while ini <= 1080:
        screen.fill((82, 82, 82))
        pygame.draw.rect(screen, (0, 0, 0), ((0, 0), (width, ini)))
        ini += 1000 / fps
        clock.tick(fps)
        pygame.display.flip()

    # выбор танка
    sg = pygame.sprite.Group()
    r = random.randint(0, 7)
    r = str(r)
    n = 'Танчики игрок' + r + '.png'
    s = pygame.sprite.Sprite()
    s.image = load_image(n)
    s.rect = s.image.get_rect()
    s.rect.x = 400
    s.rect.y = 180
    sg.add(s)
    fpoints = open('points')
    point = fpoints.readlines()
    f1 = pygame.font.Font(None, 50)
    ttext1 = f1.render(str(point[0][:6]), 0, (100, 100, 100))
    f2 = pygame.font.Font(None, 50)
    ttext2 = f2.render(str(point[1][:6]), 0, (100, 100, 100))
    f3 = pygame.font.Font(None, 50)
    ttext3 = f3.render(str(point[2][:6]), 0, (100, 100, 100))
    f4 = pygame.font.Font(None, 50)
    ttext4 = f4.render(str(point[3][:6]), 0, (100, 100, 100))
    f5 = pygame.font.Font(None, 50)
    ttext5 = f5.render(str(point[4][:6]), 0, (100, 100, 100))
    f6 = pygame.font.Font(None, 50)
    ttext6 = f6.render(str(point[5][:6]), 0, (100, 100, 100))
    f7 = pygame.font.Font(None, 50)
    ttext7 = f7.render(str(point[6][:6]), 0, (100, 100, 100))
    f8 = pygame.font.Font(None, 50)
    ttext8 = f8.render(str(point[7][:6]), 0, (100, 100, 100))

    p = pygame.sprite.Sprite()
    p.image = load_image('Танчики игрок0.png')
    p.rect = s.image.get_rect()
    p.rect.x = 500
    p.rect.y = 350
    sg.add(p)
    p1 = pygame.sprite.Sprite()
    p1.image = load_image('Танчики игрок1.png')
    p1.rect = s.image.get_rect()
    p1.rect.x = 500
    p1.rect.y = 425
    sg.add(p1)
    p2 = pygame.sprite.Sprite()
    p2.image = load_image('Танчики игрок2.png')
    p2.rect = s.image.get_rect()
    p2.rect.x = 500
    p2.rect.y = 500
    sg.add(p2)
    p3 = pygame.sprite.Sprite()
    p3.image = load_image('Танчики игрок3.png')
    p3.rect = s.image.get_rect()
    p3.rect.x = 500
    p3.rect.y = 575
    sg.add(p3)
    p4 = pygame.sprite.Sprite()
    p4.image = load_image('Танчики игрок4.png')
    p4.rect = s.image.get_rect()
    p4.rect.x = 500
    p4.rect.y = 650
    sg.add(p4)
    p5 = pygame.sprite.Sprite()
    p5.image = load_image('Танчики игрок5.png')
    p5.rect = s.image.get_rect()
    p5.rect.x = 500
    p5.rect.y = 725
    sg.add(p5)
    p6 = pygame.sprite.Sprite()
    p6.image = load_image('Танчики игрок6.png')
    p6.rect = s.image.get_rect()
    p6.rect.x = 500
    p6.rect.y = 800
    sg.add(p6)
    p7 = pygame.sprite.Sprite()
    p7.image = load_image('Танчики игрок7.png')
    p7.rect = s.image.get_rect()
    p7.rect.x = 500
    p7.rect.y = 875
    sg.add(p7)
    g = pygame.sprite.Group()
    obv(490, 340, g)


    f1 = pygame.font.Font(None, 60)
    text1 = f1.render('Денди Танчики', 0, (255, 0, 0))
    f2 = pygame.font.Font(None, 60)
    text2 = f2.render('Выберите танк', 0, (100, 100, 100))
    v = True
    player = ''
    mem = 0
    while v:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_s:
                    if mem < 7:
                        mem += 1
                if event.key == pygame.K_w:
                    if mem > 0:
                        mem -= 1
                g.update(mem * 75 + 340)
                if event.key == pygame.K_e:
                    player = str(mem)
                    v = False
        clock.tick(fps)
        screen.blit(text1, (500, 200))
        screen.blit(text2, (500, 300))
        screen.blit(ttext1, (600, 350))
        screen.blit(ttext2, (600, 425))
        screen.blit(ttext3, (600, 500))
        screen.blit(ttext4, (600, 575))
        screen.blit(ttext5, (600, 650))
        screen.blit(ttext6, (600, 725))
        screen.blit(ttext7, (600, 800))
        screen.blit(ttext8, (600, 875))
        g.draw(screen)
        sg.draw(screen)
        pygame.display.flip()

    # главное меню
    f1 = pygame.font.Font(None, 60)
    text1 = f1.render('Компания', 0, (255, 0, 0))
    f2 = pygame.font.Font(None, 60)
    text2 = f2.render('Создать свой уровень', 0, (255, 0, 0))
    f3 = pygame.font.Font(None, 100)
    text3 = f3.render('Денди танчики', 0, (255, 0, 0))
    f4 = pygame.font.Font(None, 60)
    text4 = f4.render('Открыть свой уровень', 0, (255, 0, 0))
    f5 = pygame.font.Font(None, 50)
    text5 = f5.render(str(point[int(player)][:6]), 0, (100, 100, 100))
    ga = True
    gamep = pygame.sprite.Group()
    p.image = load_image('Танчики игрок' + player + '.png')
    pl = 'Танчики игрок' + player + '.png'
    p.rect = s.image.get_rect()
    p.rect.x = 0
    p.rect.y = 0
    gamep.add(p)
    mem = 0
    g = pygame.sprite.Group()
    obv(490, 275, g)
    while ga:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    if event.key == pygame.K_s:
                        if mem < 2:
                            mem += 1
                    if event.key == pygame.K_w:
                        if mem > 0:
                            mem -= 1
                    g.update(mem * 100 + 275)
                    if event.key == pygame.K_e and mem == 0: #проверка выбора режима (только компания) !!! доработать
                        ga = False
        clock.tick(fps)
        g.draw(screen)
        screen.blit(text1, (500, 300))
        screen.blit(text2, (500, 400))
        screen.blit(text3, (500, 200))
        screen.blit(text4, (500, 500))
        screen.blit(text5, (100, 0))
        gamep.draw(screen)
        pygame.display.flip()
    if mem == 0:
        print(1)
    if mem == 1:
        print(2)
    if mem == 2:
        print(3)

    # лвл1
    f1 = pygame.font.Font(None, 100)
    lives = 3
    lvlpoints = 0
    li = pygame.sprite.Group()
    p = pygame.sprite.Sprite()
    p.image = load_image(pl)
    p.rect = s.image.get_rect()
    p.rect.x = 10
    p.rect.y = 100
    li.add(p)
    p1 = pygame.sprite.Sprite()
    p1.image = load_image(pl)
    p1.rect = s.image.get_rect()
    p1.rect.x = 10
    p1.rect.y = 200
    li.add(p1)
    p2 = pygame.sprite.Sprite()
    p2.image = load_image(pl)
    p2.rect = s.image.get_rect()
    p2.rect.x = 10
    p2.rect.y = 300
    li.add(p2)
    text1 = f1.render('Уровень: 1', 0, (255, 0, 0))
    tgame = True
    while tgame:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
        li.draw(screen)
        clock.tick(fps)
        screen.blit(text1, (0, 0))
        pygame.display.flip()