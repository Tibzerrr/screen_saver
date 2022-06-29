import pygame
import numpy as np
import time
pygame.init()

dt = .1

def color(t,f):
    x = t%f
    if x < f/3:
        color = [255*x/(f/3),0,255*(f/3-x)/(f/3)]
    elif x < 2*f/3:
        color = [255*(2*f/3-x)/(f/3),255*(x-f/3)/(f/3),0]
    else:
        color = [0,255*(3*f/3-x)/(f/3),255*(x-2*f/3)/(f/3)]
    return color

def main(n,f,R,p):
    run = True
    clock = pygame.time.Clock()

    l = n*[p*[(450,450)]]
    c = n*[p*[[0,0,0]]]
    taille = 900
    pos = [np.ones(2)*450 for i in range(p)]
    vit = [np.zeros(2) for i in range(p)]
    astre = [np.random.rand(2)*500+250 for i in range(p)]
    screen = pygame.display.set_mode((taille, taille))
    while run :
        for i in range(p):
            if np.random.random()<.025:
                astre[i] = np.random.rand(2)*900
            dm = astre[i] - pos[i]
            d = dm[0]**2 + dm[1]**2
            acc = 5*dm/np.sqrt(d)
            vit[i] += acc*dt
            pos[i] += vit[i]*dt

        t = time.time()
        l.pop()
        c.pop()
        l = [[pos[i].copy() for i in range(p)]] + l
        c = [[color(t,f)]*p] + c
        screen.fill((0,0,0))
        for j in range(p):
            for i in range(1,n+1):
                pygame.draw.circle(screen,c[n-i][j],l[n-i][j],R*(i)/n)
        keys_pressed = pygame.key.get_pressed()
        clock.tick(120)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
        if keys_pressed[pygame.K_DELETE]:
            run = False
        pygame.display.flip()
    pygame.quit()

main(80,5,20,10)