import numpy as np
import pygame

def change_color():
    return np.random.choice(['red', 'magenta', 'cyan', 'grey', 'brown', 'green', 'blue', 'yellow', 'pink', 'purple', 'orange', 'grey'])

def main():
    dt = .1
    l = 110
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1300, 800))
    run = True
    p = np.random.rand(2)
    p[0] *= 1300 - l
    p[1] *= 800 - l
    v = np.array([70,70])
    v[0] *= np.random.choice([-1,1])
    v[1] *= np.random.choice([-1,1])
    color = change_color()
    while run:
        clock.tick(60)
        keys_pressed = pygame.key.get_pressed()
        if (p[0] < 0 or p[0] > 1300 - l) and (p[1] < 0 or p[1] > 800 - l):
            v = -v
            color = change_color()
        if p[0] < 0 or p[0] > 1300 - l:
            v[0] = -v[0]
            color = change_color()
        if p[1] < 0 or p[1] > 800 - l:
            v[1] = -v[1]
            color = change_color()

        p += v*dt

        if keys_pressed[pygame.K_LCTRL] and keys_pressed[pygame.K_w]:
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill(pygame.Color("black"))
        pygame.draw.rect(screen, color, pygame.Rect(p[0],p[1],l,l))
        pygame.display.flip()
    pygame.quit()

main()