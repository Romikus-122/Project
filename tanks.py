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

    def __init__(self, *group):
        super().__init__(*group)
        self.image = obv.image
        self.rect = self.image.get_rect()
        self.rect.x = 490
        self.rect.y = 340

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
    obv(g)


    f1 = pygame.font.Font(None, 60)
    text1 = f1.render('Денди Танчики', 0, (100, 0, 0))
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
        g.draw(screen)
        sg.draw(screen)
        pygame.display.flip()

    # в разработке
    f1 = pygame.font.Font(None, 60)
    text1 = f1.render('дальнейший геймплей в разработке', 0, (100, 0, 0))
    ga = True
    gamep = pygame.sprite.Group()
    playersp = pygame.sprite.Sprite()
    p.image = load_image('Танчики игрок' + player + '.png')
    p.rect = s.image.get_rect()
    p.rect.x = 0
    p.rect.y = 0
    gamep.add(p)
    while ga:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        screen.fill((0, 0, 0))


        clock.tick(fps)
        screen.blit(text1, (500, 200))
        gamep.draw(screen)
        pygame.display.flip()