import pygame, random

pygame.init()


pygame.display.set_caption('shapes on shapes')

clock = pygame.time.Clock()

screenWidth = 1200
screenHeight = 600
screen = (screenWidth,screenHeight)
win = pygame.display.set_mode(screen)
win.fill((0,0,0))

x = [0,screenWidth,screenWidth,0,0]
y = [0,0,screenHeight,screenHeight,0]

upX = [True, True, True, True, True]
upY = [True, True, False, False, True]

a = random.randint(0,255)
b = random.randint(0,255)
c = random.randint(0,255)

changeA = True
changeB = True
changeC = True


run = True
while run:
    
    clock.tick(60)
    
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    for i in range(4):
        pygame.draw.line(win,(a, b,c), (x[i],y[i]), (x[i+1],y[i+1]))

    for i in range(5):
        if x[i] <= 0:            
            a = random.randint(0,255)
            b = random.randint(0,255)
            c = random.randint(0,255)
            upX[i] = True
        elif x[i] >= screenWidth:
            upX[i] = False
        if upX[i]:
            x[i] += 3
        else:
            x[i] -= 3
        if y[i] <= 0:
            upY[i] = True
        elif y[i] >= screenHeight:
            upY[i] = False
        if upY[i]:
            y[i] += 2
        else:
            y[i] -= 2

    if a == 255:
        changeA = False
    elif a == 0:
        changeA = True
    if b == 255:
        changeB = False
    elif b == 0:
        changeB = True
    if c == 255:
        changeC = False
    elif c == 0:
        changeC = True

    if changeA:
        a += 1
    else:
        a -= 1
    if changeB:
        b += 1
    else:
        b -= 1
    if changeC:
        c += 1
    else:
        c -=1


    pygame.display.update()

pygame.quit()