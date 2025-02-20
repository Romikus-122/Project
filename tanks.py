import os
import sys
import random

import pygame

lives = 3
livesb = 3

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey == None:
        colorkey = image.get_at((0, 0))
    if colorkey == 1:
        colorkey = image.get_at((10, 10))
    image.set_colorkey(colorkey)
    return image


class Obv(pygame.sprite.Sprite):
    image = load_image('обводка.png', 1)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = Obv.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, mem):
        self.rect.y = mem


class Cplayer(pygame.sprite.Sprite):
    def __init__(self, x, y, p, group, br):
        super().__init__(group)
        self.image = load_image(p)
        self.orimage = self.image
        self.r = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.br = br

    def update(self, mem, shells):
        if mem == 1:
            self.image = pygame.transform.rotate(self.orimage, 0)
            self.r = 0
            if self.rect.y > 55:
                self.rect.y -= 5
            if pygame.sprite.spritecollideany(self, self.br):
                self.rect.y += 5
        if mem == 2:
            self.image = pygame.transform.rotate(self.orimage, 90)
            self.r = 90
            if self.rect.x > 475:
                self.rect.x -= 5
            if pygame.sprite.spritecollideany(self, self.br):
                self.rect.x += 5
        if mem == 3:
            self.image = pygame.transform.rotate(self.orimage, 180)
            self.r = 180
            if self.rect.y < 55 + 975 - 75:
                self.rect.y += 5
            if pygame.sprite.spritecollideany(self, self.br):
                self.rect.y -= 5
        if mem == 4:
            self.image = pygame.transform.rotate(self.orimage, 270)
            self.r = 270
            if self.rect.x < 475 + 975 - 75:
                self.rect.x += 5
            if pygame.sprite.spritecollideany(self, self.br):
                self.rect.x -= 5
        if pygame.sprite.spritecollideany(self, shells):
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, p, group, br):
        super().__init__(group)
        self.image = load_image(p)
        self.orimage = self.image
        self.r = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.br = br
        self.mem = 2
        self.mem1 = 20

    def update(self, shells):
        if self.mem1 != 0:
            if self.mem == 1:
                self.image = pygame.transform.rotate(self.orimage, 0)
                self.r = 0
                if self.rect.y > 55:
                    self.rect.y -= 5
                if pygame.sprite.spritecollideany(self, self.br):
                    self.rect.y += 5
                    self.mem = random.randint(1, 4)
            if self.mem == 2:
                self.image = pygame.transform.rotate(self.orimage, 90)
                self.r = 90
                if self.rect.x > 475:
                    self.rect.x -= 5
                else:
                    self.mem = random.randint(1, 4)
                if pygame.sprite.spritecollideany(self, self.br):
                    self.rect.x += 5
                    self.mem = random.randint(1, 4)
            if self.mem == 3:
                self.image = pygame.transform.rotate(self.orimage, 180)
                self.r = 180
                if self.rect.y < 55 + 975 - 75:
                    self.rect.y += 5
                else:
                    self.mem = random.randint(1, 4)
                if pygame.sprite.spritecollideany(self, self.br):
                    self.rect.y -= 5
                    self.mem = random.randint(1, 4)
            if self.mem == 4:
                self.image = pygame.transform.rotate(self.orimage, 270)
                self.r = 270
                if self.rect.x < 475 + 975 - 75:
                    self.rect.x += 5
                else:
                    self.mem = random.randint(1, 4)
                if pygame.sprite.spritecollideany(self, self.br):
                    self.rect.x -= 5
                    self.mem = random.randint(1, 4)
            self.mem1 -= 1
        else:
            self.mem = random.randint(1, 4)
            self.mem1 = random.randint(20, 100)
        if pygame.sprite.spritecollideany(self, shells):
            global lvlpoints
            lvlpoints += 10
            self.kill()


class Shell(pygame.sprite.Sprite):
    def __init__(self, x, y, r, group, br):
        super().__init__(group)
        self.image = load_image('снаряд.png')
        self.image = pygame.transform.rotate(self.image, r)
        self.r = r
        self.orimage = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mem = 0
        self.br = br
        self.t = True

    def update(self, enem):
        if self.rect.y > 55 and self.rect.x > 475 and self.rect.y < 55 + 975 - 6 and self.rect.x < 475 + 975 - 6 and self.mem == 0 and self.t:
            if self.r == 0:
                self.rect.y -= 10
            if self.r == 180:
                self.rect.y += 10
            if self.r == 90:
                self.rect.x -= 10
            if self.r == 270:
                self.rect.x += 10
        else:
            if self.mem == 0:
                self.image = load_image('взрыв.png')
                self.rect.x -= 75 / 2
                self.rect.y -= 75 / 2
            self.mem += 1
            if self.mem == 25:
                self.kill()
        if pygame.sprite.spritecollideany(self, self.br):
            self.t = False
            if self.mem == 0:
                self.image = load_image('взрыв.png')
                self.rect.x -= 75 / 2
                self.rect.y -= 75 / 2
            self.mem += 1
            if self.mem == 25:
                self.kill()
        if pygame.sprite.spritecollideany(self, enem):
            self.t = False

class Shellenem(pygame.sprite.Sprite):
    def __init__(self, x, y, r, group, br):
        super().__init__(group)
        self.image = load_image('снаряд.png')
        self.image = pygame.transform.rotate(self.image, r)
        self.r = r
        self.orimage = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mem = 0
        self.br = br
        self.t = True

    def update(self, pla):
        if self.rect.y > 55 and self.rect.x > 475 and self.rect.y < 55 + 975 - 6 and self.rect.x < 475 + 975 - 6 and self.mem == 0 and self.t:
            if self.r == 0:
                self.rect.y -= 10
            if self.r == 180:
                self.rect.y += 10
            if self.r == 90:
                self.rect.x -= 10
            if self.r == 270:
                self.rect.x += 10
        else:
            if self.mem == 0:
                self.image = load_image('взрыв.png')
                self.rect.x -= 75 / 2
                self.rect.y -= 75 / 2
            self.mem += 1
            if self.mem == 25:
                self.kill()
        if pygame.sprite.spritecollideany(self, self.br):
            self.t = False
            if self.mem == 0:
                self.image = load_image('взрыв.png')
                self.rect.x -= 75 / 2
                self.rect.y -= 75 / 2
            self.mem += 1
            if self.mem == 25:
                self.kill()
        if pygame.sprite.spritecollideany(self, pla):
            self.t = False


class Spr(pygame.sprite.Sprite):
    def __init__(self, x, y, p, *group):
        super().__init__(*group)
        self.image = load_image(p)
        self.orimage = self.image
        self.r = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, p, *group):
        super().__init__(*group)
        self.image = load_image(p)
        self.orimage = self.image
        self.r = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


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
    ttext2 = f1.render(str(point[1][:6]), 0, (100, 100, 100))
    ttext3 = f1.render(str(point[2][:6]), 0, (100, 100, 100))
    ttext4 = f1.render(str(point[3][:6]), 0, (100, 100, 100))
    ttext5 = f1.render(str(point[4][:6]), 0, (100, 100, 100))
    ttext6 = f1.render(str(point[5][:6]), 0, (100, 100, 100))
    ttext7 = f1.render(str(point[6][:6]), 0, (100, 100, 100))
    ttext8 = f1.render(str(point[7][:6]), 0, (100, 100, 100))

    Spr(500, 350, 'Танчики игрок0.png', sg)
    Spr(500, 425, 'Танчики игрок1.png', sg)
    Spr(500, 500, 'Танчики игрок2.png', sg)
    Spr(500, 575, 'Танчики игрок3.png', sg)
    Spr(500, 650, 'Танчики игрок4.png', sg)
    Spr(500, 725, 'Танчики игрок5.png', sg)
    Spr(500, 800, 'Танчики игрок6.png', sg)
    Spr(500, 875, 'Танчики игрок7.png', sg)
    g = pygame.sprite.Group()
    Obv(490, 340, g)


    f1 = pygame.font.Font(None, 60)
    text1 = f1.render('Денди Танчики', 0, (255, 0, 0))
    text2 = f1.render('Выберите танк', 0, (100, 100, 100))
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
        clock.tick(fps)
        pygame.display.flip()

    # главное меню
    f1 = pygame.font.Font(None, 60)
    text1 = f1.render('Компания', 0, (255, 0, 0))
    text2 = f1.render('Создать свой уровень', 0, (255, 0, 0))
    f3 = pygame.font.Font(None, 100)
    text3 = f3.render('Денди танчики', 0, (255, 0, 0))
    text4 = f1.render('Открыть свой уровень', 0, (255, 0, 0))
    f5 = pygame.font.Font(None, 50)
    text5 = f5.render(str(point[int(player)][:6]), 0, (100, 100, 100))
    ga = True
    gamep = pygame.sprite.Group()
    Spr(0, 0, 'Танчики игрок' + player + '.png', gamep)
    pl = 'Танчики игрок' + player + '.png'
    mem = 0
    g = pygame.sprite.Group()
    Obv(490, 275, g)
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
        clock.tick(fps)
        pygame.display.flip()
    if mem == 0:
        print(1)
    if mem == 1:
        print(2)
    if mem == 2:
        print(3)



    # лвл1
    pla = pygame.sprite.Group()
    bri = pygame.sprite.Group()
    enem = pygame.sprite.Group()
    shells = pygame.sprite.Group()
    shellsenem = pygame.sprite.Group()
    lives = 3
    livesb = 3
    global lvlpoints
    lvlpoints = 0
    li = pygame.sprite.Group()
    p = pygame.sprite.Sprite()
    Spr(10, 100, pl, li)
    Spr(10, 200, pl, li)
    Spr(10, 300, pl, li)
    #
    lib = pygame.sprite.Group()
    Spr(110, 100, 'база.png', lib)
    Spr(110, 200, 'база.png', lib)
    Spr(110, 300, 'база.png', lib)
    f1 = pygame.font.Font(None, 100)
    text1 = f1.render('Уровень: 1', 0, (255, 0, 0))
    f2 = pygame.font.Font(None, 90)
    tgame = True
    lvlxy = [475, 55, 975, 975]
    lvlform = open(os.path.join('lvls', 'lvl1'), 'r')
    mem = []
    for i in range(1, 15):
        x = lvlform.readline()
        print(x, i)
        for i1 in range(0, 14):
            print(x[i1])
            if x[i1] == '0':
                continue
            elif x[i1] == 'P':
                mem.append((lvlxy[0] + i1 * 75, lvlxy[1] + (i - 2) * 75))
            elif x[i1] == 'B':
                pass
            elif x[i1] == 'X':
                Brick(lvlxy[0] + i1 * 75, lvlxy[1] + (i - 2) * 75, 'стена.png', bri)
            elif x[i1] == 'V':
                Enemy(lvlxy[0] + i1 * 75, lvlxy[1] + (i - 2) * 75, 'Танчики враг.png', enem, bri)
    for i in mem:
        Cplayer(*i, pl, pla, bri)
    while tgame:
        screen.fill((0, 0, 0))
        t = str(lvlpoints)
        while len(t) < 6:
            t = '0' + t
        text2 = f2.render('Очки: ' + t, 0, (100, 100, 100))
        pygame.draw.rect(screen, (255, 127, 0), ((425, 5), (1075, 1075)))
        pygame.draw.rect(screen, (0, 0, 0), ((475, 55), (975, 975)))
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    if event.key == pygame.K_SPACE:
                        Shell(pla.sprites()[0].rect[0] + 35, pla.sprites()[0].rect[1] + 35, pla.sprites()[0].r, shells, bri)
                    if event.key == pygame.K_r:
                        pass
                        # рестарт лвла
        if keys[pygame.K_SPACE] and keys[pygame.K_CAPSLOCK]:
            Shell(pla.sprites()[0].rect[0] + 35, pla.sprites()[0].rect[1] + 35, pla.sprites()[0].r, shells, bri)
        if keys[pygame.K_w]:
            pla.update(1, shellsenem)
        elif keys[pygame.K_a]:
            pla.update(2, shellsenem)
        elif keys[pygame.K_s]:
            pla.update(3, shellsenem)
        elif keys[pygame.K_d]:
            pla.update(4, shellsenem)
        for i in enem:
            s = random.randint(1, 100)
            if s <= 2:
                Shellenem(i.rect[0] + 35, i.rect[1] + 35, i.r, shellsenem, bri)
        shells.update(enem)
        shellsenem.update(pla)
        pla.update(0, shellsenem)
        enem.update(shells)
        bri.draw(screen)
        li.draw(screen)
        lib.draw(screen)
        pla.draw(screen)
        enem.draw(screen)
        shells.draw(screen)
        shellsenem.draw(screen)
        clock.tick(fps)
        screen.blit(text1, (0, 0))
        screen.blit(text2, (1500, 0))
        clock.tick(fps)
        pygame.display.flip()