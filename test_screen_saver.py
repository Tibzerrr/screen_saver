import pygame
import numpy as np
import time
pygame.init()

def color(t,f):
    x = t%f
    if x < f/6:
        color = [255,255*x/(f/6),0]
    elif x < 2*f/6:
        color = [255*(2*f/6-x)/(f/6),255,0]
    elif x < 3*f/6:
        color = [0,255,255*(x-2*f/6)/(f/6)]
    elif x < 4*f/6:
        color = [0,255*(4*f/6-x)/(f/6),255]
    elif x < 5*f/6:
        color = [255*(x-4*f/6)/(f/6),0,255]
    else:
        color = [255,0,255*(6*f/6-x)/(f/6)]
    return color

def main(n,f,R):
    run = True
    clock = pygame.time.Clock()
    l = n*[(-100,-100)]
    c = n*[[0,0,0]]
    taille = 900
    screen = pygame.display.set_mode((taille, taille))
    while run :
        t = time.time()
        l.pop()
        c.pop()
        l = [pygame.mouse.get_pos()] + l
        c = [color(t,f)] + c
        screen.fill((0,0,0))
        for i in range(1,n+1):
            pygame.draw.circle(screen,c[n-i],l[n-i],R*(i)/n)
        keys_pressed = pygame.key.get_pressed()
        clock.tick(120)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
        if keys_pressed[pygame.K_DELETE]:
            run = False
        pygame.display.flip()
    pygame.quit()

main(80,5,20)