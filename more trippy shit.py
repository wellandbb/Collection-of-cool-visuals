import pygame, random

pygame.init()

pygame.display.set_caption('Trip dog')

clock = pygame.time.Clock()

screenWidth = 500
screenHeight = 500
screen = (screenWidth,screenHeight)
win = pygame.display.set_mode(screen)
win.fill((0,0,0))


def mouseClick():
    for r in range(100,0,-1):
        pygame.draw.circle(win,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),mouse,r)

run = True
while run:
    
    clock.tick(27)
    
    mouse = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseClick()
    

    pygame.display.update()

pygame.quit()