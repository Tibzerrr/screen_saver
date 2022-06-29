import pygame
import numpy as np
import time
pygame.init()

dt = .15

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

def main(n,f,R,p,multi=True):
    run = True
    clock = pygame.time.Clock()

    l = n*[p*[(960,540)]]
    c = n*[p*[[0,0,0]]]
    pos = [[960,540] for i in range(p)]
    vit = [(np.random.rand(2)-.5)*100 for i in range(p)]
    astre = [np.random.rand(2) for i in range(p)]
    for i in range(p):
        astre[i][0]*=1920
        astre[i][1]*=1080
    screen = pygame.display.set_mode((1920, 1080))
    while run :
        pygame.mouse.set_visible(False)
        for i in range(p):
            if np.random.random()<.01:
                astre[i] = np.random.rand(2)
                astre[i][0]*=1920
                astre[i][1]*=1080
            dm = astre[i] - pos[i]
            d = dm[0]**2 + dm[1]**2
            acc = 5*dm/np.sqrt(d)
            vit[i] += acc*dt
            if vit[i][0]**2 + vit[i][1] >500:
                vit[i] /= 1.1
            pos[i] += vit[i]*dt

        t = time.time()
        l.pop()
        c.pop()
        l = [[pos[i].copy() for i in range(p)]] + l
        if multi:
            c = [[color(t+(i*f/p),f) for i in range(p)]] + c
        else:
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

main(100,5,15,20,multi = False)