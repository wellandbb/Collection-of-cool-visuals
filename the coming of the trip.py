import pygame, random

pygame.init()


pygame.display.set_caption('shapes on shapes')

clock = pygame.time.Clock()

screenWidth = 1200
screenHeight = 600
screen = (screenWidth,screenHeight)
win = pygame.display.set_mode(screen)
win.fill((0,0,0))

x1 = [screenWidth/2,screenWidth/2,screenWidth/2,screenWidth/2,screenWidth/2]
y1 = [screenHeight/2,screenHeight/2,screenHeight/2,screenHeight/2,screenHeight/2]

upX1 = [True, False, False, True, True]
upY1 = [True, True, False, False, True]

a1 = random.randint(0,255)
b1 = random.randint(0,255)
c1 = random.randint(0,255)

changeA1 = True
changeB1 = True
changeC1 = True




x2 = [0,screenWidth,screenWidth,0,0]
y2 = [0,0,screenHeight,screenHeight,0]

upX2 = [True, True, True, True, True]
upY2 = [True, True, False, False, True]

a2 = random.randint(0,255)
b2 = random.randint(0,255)
c2 = random.randint(0,255)

changeA2 = True
changeB2 = True
changeC2 = True


run = True
while run:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    for i in range(4):
        pygame.draw.line(win,(a1, b1,c1), (x1[i],y1[i]), (x1[i+1],y1[i+1]))

    for i in range(5):
        if x1[i] <= 0:            
            a1 = random.randint(0,255)
            b1 = random.randint(0,255)
            c1 = random.randint(0,255)
            upX1[i] = True
        elif x1[i] >= screenWidth:
            upX1[i] = False
        if upX1[i]:
            x1[i] += 3
        else:
            x1[i] -= 3
        if y1[i] <= 0:
            upY1[i] = True
        elif y1[i] >= screenHeight:
            upY1[i] = False
        if upY1[i]:
            y1[i] += 2
        else:
            y1[i] -= 2

    if a1 == 255:
        changeA1 = False
    elif a1 == 0:
        changeA1 = True
    if b1 == 255:
        changeB1 = False
    elif b1 == 0:
        changeB1 = True
    if c1 == 255:
        changeC1 = False
    elif c1 == 0:
        changeC1 = True

    if changeA1:
        a1 += 1
    else:
        a1 -= 1
    if changeB1:
        b1 += 1
    else:
        b1 -= 1
    if changeC1:
        c1 += 1
    else:
        c1 -=1


    
    for i in range(4):
        pygame.draw.line(win,(a2, b2,c2), (x2[i],y2[i]), (x2[i+1],y2[i+1]))

    for i in range(5):
        if x2[i] <= 0:            
            a2 = random.randint(0,255)
            b2 = random.randint(0,255)
            c2 = random.randint(0,255)
            upX2[i] = True
        elif x2[i] >= screenWidth:
            upX2[i] = False
        if upX2[i]:
            x2[i] += 3
        else:
            x2[i] -= 3
        if y2[i] <= 0:
            upY2[i] = True
        elif y2[i] >= screenHeight:
            upY2[i] = False
        if upY2[i]:
            y2[i] += 2
        else:
            y2[i] -= 2

    if a2 == 255:
        changeA2 = False
    elif a2 == 0:
        changeA2 = True
    if b2 == 255:
        changeB2 = False
    elif b2 == 0:
        changeB2 = True
    if c2 == 255:
        changeC2 = False
    elif c2 == 0:
        changeC2 = True

    if changeA2:
        a2 += 1
    else:
        a2 -= 1
    if changeB2:
        b2 += 1
    else:
        b2 -= 1
    if changeC2:
        c2 += 1
    else:
        c2 -= 1



    pygame.display.update()

pygame.quit()