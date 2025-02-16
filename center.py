import os
import sys
import random
import pygame
import tanks
import tetris


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class ta(pygame.sprite.Sprite):
    image = load_image('Танчики.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = ta.image
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 60

    def update(self, *args):
        if self.rect.collidepoint(args[0].pos):
            tanks.tanks()


class te(pygame.sprite.Sprite):
    image = load_image('Тетрис.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = te.image
        self.rect = self.image.get_rect()
        self.rect.x = 220
        self.rect.y = 60

    def update(self, *args):
        if self.rect.collidepoint(args[0].pos):
            tetris.tetris()


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
    fps = 60

    all_im = pygame.sprite.Group()
    ta(all_im)
    te(all_im)
    f2 = pygame.font.Font(None, 40)
    text2 = f2.render('Денди танчики', 1, (0, 0, 0))
    f3 = pygame.font.Font(None, 40)
    text3 = f3.render('Тетрис', 1, (0, 0, 0))

    running = True
    while running:
        screen.fill((82, 82, 82))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
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
        screen.blit(text2, (10, 270))
        screen.blit(text3, (260, 270))
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
