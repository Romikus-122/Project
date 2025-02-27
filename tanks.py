import os
import sys
import random

import pygame

lives = 3
livesb = 3
lvl = 1
pointsp = 0
point = []
player = ''

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
        self.time = 20

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
        if pygame.sprite.spritecollideany(self, shells) and self.time == 0:
            self.kill()
        if self.time != 0:
            self.time -= 1

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
        self.mem = 3
        self.mem1 = 30

    def update(self, shells):
        if self.mem1 != 0:
            if self.mem == 1:
                self.image = pygame.transform.rotate(self.orimage, 0)
                self.r = 0
                if self.rect.y > 55:
                    self.rect.y -= 5
                else:
                    self.mem = random.randint(1, 4)
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
            self.mem1 = random.randint(15, 120)
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
            if self.mem == 10:
                self.kill()
        if pygame.sprite.spritecollideany(self, self.br) and self.t == True:
            self.t = False
            if self.mem == 0:
                self.image = load_image('взрыв.png')
                self.rect.x -= 75 / 2
                self.rect.y -= 75 / 2
            self.mem += 1
            if self.mem == 10:
                self.kill()
        if pygame.sprite.spritecollideany(self, enem) and self.t == True:
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

    def update(self, pla, b):
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
            if self.mem == 10:
                self.kill()
        if pygame.sprite.spritecollideany(self, self.br) and self.t == True:
            self.t = False
            if self.mem == 0:
                self.image = load_image('взрыв.png')
                self.rect.x -= 75 / 2
                self.rect.y -= 75 / 2
            self.mem += 1
            if self.mem == 10:
                self.kill()
        if (pygame.sprite.spritecollideany(self, pla) or pygame.sprite.spritecollideany(self, b)) and self.t == True:
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


class Base(pygame.sprite.Sprite):
    def __init__(self, x, y, p, *group):
        super().__init__(*group)
        self.image = load_image(p)
        self.orimage = self.image
        self.r = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.t = 0

    def update(self, shells):
        self.t += 1
        if pygame.sprite.spritecollideany(self, shells) and self.t > 25:
            self.kill()


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
    global point
    poi = fpoints.readlines()
    for i in poi:
        point.append(i[:6])
    fpoints.close()
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
    text3 = f1.render('E для подтверждения', 0, (100, 100, 100))
    text4 = f1.render('W, S для выбора', 0, (100, 100, 100))
    v = True
    global player
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
        screen.blit(text3, (1000, 200))
        screen.blit(text4, (1000, 300))
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
    global pointsp
    pointsp = int(point[int(player)][:6])
    ga = True
    gamep = pygame.sprite.Group()
    Spr(0, 0, 'Танчики игрок' + player + '.png', gamep)
    pl = 'Танчики игрок' + player + '.png'
    mem = 0
    g = pygame.sprite.Group()
    Obv(490, 275, g)
    text6 = f1.render('E для подтверждения', 0, (100, 100, 100))
    text7 = f1.render('W, S для выбора', 0, (100, 100, 100))
    while ga:
        screen.fill((0, 0, 0))
        text5 = f5.render(str(point[int(player)][:6]), 0, (100, 100, 100))
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
                        global lvl
                        lvl = 1
                        trt = True
                        ff1 = pygame.font.Font(None, 100)
                        ff2 = pygame.font.Font(None, 50)
                        textt2 = ff2.render('нажмите W чтобы увеличить уровень', 0, (82, 82, 82))
                        textt3 = ff2.render('нажмите S чтобы уменьшить уровень', 0, (82, 82, 82))
                        textt4 = ff2.render('нажмите E чтобы подтвердить', 0, (82, 82, 82))
                        while trt:
                            screen.fill((0, 0, 0))
                            textt1 = ff1.render('Выбранный уровень: ' + str(lvl), 0, (255, 0, 0))
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    return
                                if event.type == pygame.KEYDOWN:
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            return
                                        if event.key == pygame.K_e:
                                            trt = False
                                        if event.key == pygame.K_w:
                                            if lvl < 5:
                                                lvl += 1
                                        if event.key == pygame.K_s:
                                            if lvl > 1:
                                                lvl -= 1
                            screen.blit(textt1, (500, 300))
                            screen.blit(textt2, (500, 500))
                            screen.blit(textt3, (500, 550))
                            screen.blit(textt4, (500, 600))
                            clock.tick(fps)
                            pygame.display.flip()
                        lvles(lvl, pl, screen, fps)
        clock.tick(fps)
        g.draw(screen)
        screen.blit(text1, (500, 300))
        screen.blit(text2, (500, 400))
        screen.blit(text3, (500, 200))
        screen.blit(text4, (500, 500))
        screen.blit(text5, (100, 0))
        screen.blit(text6, (1100, 200))
        screen.blit(text7, (1100, 300))
        gamep.draw(screen)
        clock.tick(fps)
        pygame.display.flip()


def win(screen, fps, pl):
    global lvlpoints
    global lvl
    global pointsp
    global point
    global player
    pointsp += lvlpoints
    clock = pygame.time.Clock()
    width = 1920
    ini = 0
    while ini <= 1080:
        pygame.draw.rect(screen, (0, 0, 0), ((0, 0), (width, ini)))
        ini += 1000 / fps
        clock.tick(fps)
        pygame.display.flip()
    f1 = pygame.font.Font(None, 100)
    f2 = pygame.font.Font(None, 50)
    text1 = f1.render('Вы выйграли! :)', 0, (82, 82, 82))
    text2 = f1.render('и набрали ' + str(lvlpoints) + ' очков', 0, (82, 82, 82))
    text3 = f2.render('нажмите R для рестарта', 0, (82, 82, 82))
    text4 = f2.render('нажмите ESC для выхода в меню', 0, (82, 82, 82))
    text5 = f2.render('(очки добавлены к профилю)', 0, (82, 82, 82))
    text6 = f2.render('нажмите E для перехода на следующий уровень', 0, (82, 82, 82))
    lvlpoints += int(point[int(player)])
    pp = str(lvlpoints)
    while len(pp) != 6:
        pp = '0' + pp
    point[int(player)] = pp
    #
    f = open('points', 'w')
    for i in point:
        f.write(i + '\n')
    f.close()
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    if event.key == pygame.K_r:
                        return lvles(lvl, pl, screen, fps)
                    if event.key == pygame.K_e:
                        if lvl < 5:
                            lvl += 1
                            return lvles(lvl, pl, screen, fps)
                        else:
                            return
        screen.blit(text1, (500, 100))
        screen.blit(text2, (500, 200))
        screen.blit(text3, (500, 350))
        screen.blit(text4, (500, 400))
        screen.blit(text5, (500, 300))
        screen.blit(text6, (500, 500))
        clock.tick(fps)
        pygame.display.flip()


def end(screen, fps, pl):
    global lvlpoints
    global lvl
    width = 1920
    clock = pygame.time.Clock()
    ini = 0
    while ini <= 1080:
        pygame.draw.rect(screen, (0, 0, 0), ((0, 0), (width, ini)))
        ini += 1000 / fps
        clock.tick(fps)
        pygame.display.flip()
    f1 = pygame.font.Font(None, 100)
    f2 = pygame.font.Font(None, 50)
    text1 = f1.render('Вы проиграли! :(', 0, (82, 82, 82))
    text2 = f1.render('и набрали ' + str(lvlpoints) + ' очков', 0, (82, 82, 82))
    text3 = f2.render('нажмите R для рестарта', 0, (82, 82, 82))
    text4 = f2.render('нажмите ESC для выхода в меню', 0, (82, 82, 82))
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    if event.key == pygame.K_r:
                        return lvles(lvl, pl, screen, fps)
        screen.blit(text1, (500, 100))
        screen.blit(text2, (500, 200))
        screen.blit(text3, (500, 350))
        screen.blit(text4, (500, 400))
        clock.tick(fps)
        pygame.display.flip()



def lvles(lvl, pl, screen, fps):
    ti = 0
    clock = pygame.time.Clock()
    pla = pygame.sprite.Group()
    base = pygame.sprite.Group()
    bush = pygame.sprite.Group()
    bri = pygame.sprite.Group()
    enem = pygame.sprite.Group()
    enems = pygame.sprite.Group()
    shells = pygame.sprite.Group()
    shellsenem = pygame.sprite.Group()
    lives = 3
    livesb = 3
    enemycol = 0
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
    text1 = f1.render('Уровень: ' + str(lvl), 0, (255, 0, 0))
    f2 = pygame.font.Font(None, 90)
    tgame = True
    lvlxy = [475, 55, 975, 975]
    lvlform = open(os.path.join('lvls', 'lvl' + str(lvl)), 'r')
    f3 = pygame.font.Font(None, 50)
    text3 = f3.render('Spase для стрельбы', 0, (100, 100, 100))
    text4 = f3.render('WASD для движения', 0, (100, 100, 100))
    text5 = f3.render('R для рестарта уровня', 0, (100, 100, 100))
    mem = []
    mem1 = []
    mem2 = []
    for i in range(1, 16):
        x = lvlform.readline()
        print(x, i)
        if i == 15:
            enemycol = int(x)
            break
        for i1 in range(0, 14):
            print(x[i1])
            if x[i1] == '0':
                continue
            elif x[i1] == 'P':
                mem.append((lvlxy[0] + i1 * 75, lvlxy[1] + (i - 2) * 75))
            elif x[i1] == 'B':
                mem2.append((lvlxy[0] + i1 * 75, lvlxy[1] + (i - 2) * 75))
                Base(lvlxy[0] + i1 * 75, lvlxy[1] + (i - 2) * 75, 'база.png', base)
            elif x[i1] == 'X':
                Spr(lvlxy[0] + i1 * 75, lvlxy[1] + (i - 2) * 75, 'стена.png', bri)
            elif x[i1] == 'V':
                Spr(lvlxy[0] + i1 * 75, lvlxy[1] + (i - 2) * 75, 'завод.png', enems)
                mem1.append((lvlxy[0] + i1 * 75, lvlxy[1] + (i - 2) * 75))
            elif x[i1] == '#':
                Spr(lvlxy[0] + i1 * 75, lvlxy[1] + (i - 2) * 75, 'куст.png', bush)
    for i in mem:
        Cplayer(*i, pl, pla, bri)
    time = 90
    while tgame:
        screen.fill((0, 0, 0))
        t = str(lvlpoints)
        while len(t) < 6:
            t = '0' + t
        text2 = f2.render('Очки: ' + t, 0, (100, 100, 100))
        pygame.draw.rect(screen, (255, 127, 0), ((425, 5), (1075, 1075)))
        pygame.draw.rect(screen, (0, 0, 0), ((475, 55), (975, 975)))
        if len(enem) < 5 and enemycol != 0 and time > 20:
            trr = random.choice(mem1)
            Enemy(*trr, 'Танчики враг.png', enem, bri)
            enemycol -= 1
            time = 0
        text6 = f3.render('Врагов на подходе: ' + str(enemycol), 0, (100, 100, 100))
        time += 1
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    if event.key == pygame.K_SPACE and len(pla) != 0:
                        Shell(pla.sprites()[0].rect[0] + 35, pla.sprites()[0].rect[1] + 35, pla.sprites()[0].r, shells, bri)
                    if event.key == pygame.K_r:
                        return lvles(lvl, pl, screen, fps)
        if len(pla) == 0:
            for i in li:
                li.remove(i)
                break
            lives -= 1
            if lives > 0:
                for i in mem:
                    Cplayer(*i, pl, pla, bri)
            else:
                if ti >= 20:
                    return end(screen, fps, pl)
                else:
                    ti += 1
        if len(enem) == 0:
            if ti >= 20:
                return win(screen, fps, pl)
            else:
                ti += 1
        if keys[pygame.K_SPACE] and keys[pygame.K_CAPSLOCK] and len(pla) != 0:
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
        enem.update(shells)
        shellsenem.update(pla, base)
        pla.update(0, shellsenem)
        base.update(shellsenem)
        if len(base) == 0:
            for i in lib:
                lib.remove(i)
                break
            livesb -= 1
            if livesb > 0:
                for i in mem2:
                    Base(*i, 'база.png', base)
            else:
                if ti >= 20:
                    return end(screen, fps, pl)
                else:
                    ti += 1
        base.draw(screen)
        enems.draw(screen)
        bri.draw(screen)
        li.draw(screen)
        lib.draw(screen)
        pla.draw(screen)
        enem.draw(screen)
        shells.draw(screen)
        shellsenem.draw(screen)
        bush.draw(screen)
        clock.tick(fps)
        screen.blit(text1, (0, 0))
        screen.blit(text2, (1500, 0))
        screen.blit(text3, (1500, 100))
        screen.blit(text4, (1500, 200))
        screen.blit(text5, (1500, 300))
        screen.blit(text6, (0, 500))
        clock.tick(fps)
        pygame.display.flip()
