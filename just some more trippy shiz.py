import pygame, random

pygame.init()

pygame.display.set_caption('Trip dog')

clock = pygame.time.Clock()

screenWidth = 1200
screenHeight = 600
screen = (screenWidth,screenHeight)
win = pygame.display.set_mode(screen)
win.fill((0,0,0))

a = random.randint(0,255)
b = random.randint(0,255)
c = random.randint(0,255)

x = [0,screenWidth,0,screenWidth,screenWidth/2, screenWidth/2]
y = [0,0,screenHeight,screenHeight,0, screenHeight]
area = [1,2,3,4,1,3]

first = True
second = False
third = False
fourth = False

changeA = True
changeB = False
changeC = False


run = True
while run:
    
    clock.tick(120)
    
    mouse = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    

    for i in range (6):
        pygame.draw.line(win,(a,b,c),(screenWidth/2,screenHeight/2),(x[i],y[i]))

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

    for l in range(6):
        if x[l] == 0 and y[l] == 0:
            area[l] = 1
            a = random.randint(0,255)
            b = random.randint(0,255)
            c = random.randint(0,255)

        if x[l] == screenWidth and y[l] == 0:
            area[l] = 2

        if x[l] == screenWidth and y[l] == screenHeight:
            area[l] = 3

        if x[l] == 0 and y[l] == screenHeight:
            area[l] = 4

        if area[l] == 1:
            x[l] += 1
        if area[l] == 2:
            y[l] += 1
        if area[l] == 3:
            x[l] -= 1
        if area[l] == 4:
            y[l] -=1
    

    pygame.display.update()

pygame.quit()