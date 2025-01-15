import os
import sys

import pygame



def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class cl(pygame.sprite.Sprite):
    imc = load_image('Нажатие.png')

    def __init__(self, group, i, x, y):
        super().__init__(group)
        self.image = load_image(i)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        print(1)
        if self.rect.collidepoint(args[0].pos):
            print(2)
            self.image = self.imc

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Game Center')
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()
    screen.fill((82, 82, 82))
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('вас приветствует Game Center, во что сыграем сегодня?', 1, (0, 0, 0))
    mem = 0

    all_im = pygame.sprite.Group()
    x = 10
    y = 60
    for i in ['Танчики.png']:
        print(i)
        x = x
        y = y
        cl(all_im, i, x, y)

    running = True
    while running:
        screen.fill((82, 82, 82))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    if mem < 1000:
                        mem += 10
                if event.button == 5:
                    if mem > 0:
                        mem -= 10
                if event.button == 1:
                    for cl in all_im:
                        cl.update(event)
        all_im.draw(screen)
        pygame.draw.rect(screen, (70, 70, 70), ((0, 0), (1920, 50)))
        screen.blit(text1, (10, 10))
        pygame.display.flip()
    pygame.quit()
