import pygame
HEIGHT = 600
WIDTH = 750 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("rocket blasting to space")
stars = pygame.image.load(r"rocketinspcace\image\a.png")
rocket = pygame.image.load(r"rocketinspcace\image\b.png")
x = WIDTH//2
y = HEIGHT//2


run = True
while run == True:
    screen.blit(stars , (0,0))
    screen.blit(rocket , (x , y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y = y-2
            if event.key == pygame.K_s:
                y = y+2
            if event.key == pygame.K_a:
                x = x-2
            if event.key == pygame.K_d:
                x = x+2    
    pygame.display.update()
