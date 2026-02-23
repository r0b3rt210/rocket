import pygame
HEIGHT = 1000
WIDTH = 1250
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("rocket blasting to space")
stars = pygame.image.load(r"rocketinspcace\image\a.png")
rocket = pygame.image.load(r"rocketinspcace\image\b.png")
x = 625
y = 1250
gravity = 1.2
acc = 1.2
run = True
while run == True:
    screen.blit(stars , (0,0))
    screen.blit(rocket , (x , y))

    gravity = gravity + 0.1
    y = y +  gravity
    key_press = pygame.key.get_pressed()
    if key_press[pygame.K_w]:
        y = y - 1.1 * acc
        acc+acc*1.2
        gravity = 0
    if key_press[pygame.K_s]:
        y = y + 2.5
    if key_press[pygame.K_a]:
        x = x - 2.5
    if key_press[pygame.K_d]:
        x = x + 2.5
    if x >= WIDTH-150:
        x = WIDTH-150
    if y >= HEIGHT-219:
        y = HEIGHT-219
        gravity = 1.2
    if x <= 0:
        x = 0
    if y <= 0:
        y = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y = y-5
            if event.key == pygame.K_s:
                y = y+5
            if event.key == pygame.K_a:
                x = x-5
            if event.key == pygame.K_d:
                x = x+5    
    pygame.display.update()
