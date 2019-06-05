import pygame, random

pygame.init()

pygame.display.set_caption('Trip dog')

clock = pygame.time.Clock()

screenWidth = 500
screenHeight = 500
screen = (screenWidth,screenHeight)
win = pygame.display.set_mode(screen)
win.fill((0,0,0))

x = [0,500]
y = [0,500]

first = True
second = False
third = False

run = True
while run:
    
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in range(2):
        for j in range(2):
            for r in range(40,0,-1):    
                colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                pygame.draw.circle(win,colour,(x[i],y[j]),r)
                
    
    if x[0] == 250 and first:
        first = False
        second = True
    elif x[0] == 0 and second:
        second = False
        third = True
        x[0] = 250
        x[1] = 250
    elif third and y[0] == 0:
        run = False
        
            
    if first:
        x[0] += 50    
        x[1] -= 50
        y[0] += 50
        y[1] -= 50
    elif second:
        x[0] -= 50
        x[1] += 50
    elif third:
        y[0] -= 50
        y[1] += 50

    
    

    pygame.display.update()

r = 300
while not(run):

    clock.tick(45)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

    colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    pygame.draw.circle(win,colour,(250,250),r)

    r -= 1
    if r == 0:
        run = True

    pygame.display.update()
        




pygame.quit()