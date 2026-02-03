import pygame

import random

import math

pygame.mixer.init()

pygame.font.init()


#Variables
background_colour = (150, 150, 150)

font1 = pygame.font.SysFont('Arial', 25)

text_surface16 = font1.render("KM/H", True, "white")

text_surface1 = font1.render("10", True, "white")
text_surface2 = font1.render("2", True, "white")
text_surface3 = font1.render("3", True, "white")
text_surface4 = font1.render("4", True, "white")
text_surface5 = font1.render("50", True, "white")
text_surface6 = font1.render("6", True, "white")
text_surface7 = font1.render("7", True, "white")
text_surface8 = font1.render("8", True, "white")
text_surface9 = font1.render("9", True, "white")
text_surface10 = font1.render("100", True, "white")
text_surface11 = font1.render("11", True, "white")
text_surface12 = font1.render("12", True, "white")
text_surface13 = font1.render("13", True, "white")
text_surface14 = font1.render("14", True, "white")
text_surface15 = font1.render("15", True, "white")

Colour_1 = (235, 235, 235)

Colour_2 = (25 ,25 ,25)

Colour_3 = (62 ,73 ,67)

Colour_4 = (60, 60, 60)

clk = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))

sand = pygame.image.load("sand.png")

stone1 = pygame.image.load("stone1.png")
stone1 = pygame.transform.scale(stone1, (150/1.5, 123/1.5))

stone2 = pygame.image.load("stone2.png")
stone2 = pygame.transform.scale(stone2, (137/1.5, 105/1.5))

stone3 = pygame.image.load("stone3.png")
stone3 = pygame.transform.scale(stone3, (106/1.5, 75/1.5))

stone4 = pygame.image.load("stone4.png")
stone4 = pygame.transform.scale(stone4, (86/1.5, 72/1.5))

stone5 = pygame.image.load("stone5.png")
stone5 = pygame.transform.scale(stone5, (54/1.5, 48/1.5))

s = 0

v = 0

a = 0

f = 0

shake = 2

k = 100

l = 0

cary = 270

caryD = 0

running = True

stoneas = [(50, 100, stone1), (50, 100, stone1), (65, 50, stone2), (65, 50, stone2), (350, 100, stone3), (230, 68, stone4), (350, 100, stone3), (230, 68, stone4), (230, 68, stone4), (230, 68, stone4)]

stones = [(50, 100, stone1), (50, 100, stone1), (65, 50, stone2), (65, 50, stone2), (350, 100, stone3), (230, 68, stone4), (350, 100, stone3), (230, 68, stone4), (230, 68, stone4), (230, 68, stone4)]

# Load car and change size.
imageM = pygame.image.load("bilM.png")
imageM = pygame.transform.scale(imageM, (1223/7, 553/7))

imageW = pygame.image.load("bilW.png")
imageW = pygame.transform.scale(imageW, (1223/7, 553/7))

imageS = pygame.image.load("bilS.png")
imageS = pygame.transform.scale(imageS, (1223/7, 553/7))

image = imageM

sandx = 0

pygame.mixer.music.load("Riders on the storm.mp3")

pygame.mixer.music.play(-1) 

pygame.mixer.music.set_volume(0.5)

# Rectangles...
pygame.draw.rect(screen, Colour_3, pygame.Rect(0, 350, 500, 50))

pygame.draw.rect(screen, Colour_3, pygame.Rect(0, 65, 500, 50))

pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 25, 230, 50, 10))

pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 125, 230, 50, 10))

pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 225, 230, 50, 10))

pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 325, 230, 50, 10))

pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 425, 230, 50, 10))

pygame.draw.rect(screen, Colour_2, pygame.Rect(0, 115, 500, 250))

# Game title.
pygame.display.set_caption('kar gem')


# Fill background.
screen.fill(background_colour)


# ---
while running:


    # Rectangles...
    pygame.draw.rect(screen, Colour_2, pygame.Rect(0, 115+50, 800, 250))

    pygame.draw.rect(screen, Colour_3, pygame.Rect(0, 350+50, 800, 50))

    pygame.draw.rect(screen, Colour_3, pygame.Rect(0, 65+50, 800, 53))


    # Moving rectangles!
    pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 25, 230+50, 50, 10))

    pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 125, 230+50, 50, 10))

    pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 225, 230+50, 50, 10))

    pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 325, 230+50, 50, 10))

    pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 425, 230+50, 50, 10))

    pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 525, 230+50, 50, 10))

    pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 625, 230+50, 50, 10))

    pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 725, 230+50, 50, 10))

    pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 825, 230+50, 50, 10))


    # So much sand...
    screen.blit(sand, (sandx + 0, -88))
    screen.blit(sand, (sandx + 256, -88))
    screen.blit(sand, (sandx + 256*2, -88))
    screen.blit(sand, (sandx + 256*3, -88))
    screen.blit(sand, (sandx + 256*4, -88))

    screen.blit(sand, (sandx + 0, 400))
    screen.blit(sand, (sandx + 256, 400))
    screen.blit(sand, (sandx + 256*2, 400))
    screen.blit(sand, (sandx + 256*3, 400))
    screen.blit(sand, (sandx + 256*4, 400))
    
    # Rocks
    for(x, y, surface) in stones:
        screen.blit(surface, (x, y))

    for(x, y, surface) in stoneas:
        screen.blit(surface, (x, y))


    # Put the car on screen.
    screen.blit(image, (k, cary+l))


    # The car/velocities/friction bullshit logic.
    if v != 0:
        if caryD < 0:
            cary = cary-1
            image = imageW
        if caryD > 0:
            cary = cary+1
            image = imageS
        if caryD == 0:
            image = imageM

    if cary + 553/7 > 410:
        f = -0.3
        shake = 5

        if v > 10:
            f = -0.3
        else:
            f = -0.1

    elif cary + 553/7 < 210:
        f = -0.3
        shake = 5

        if v > 10:
            f = -0.3
        else:
            f = -0.1

    else:
        f = -0.015
        shake = 2

    v = v+a+f

    if v > 15:
        v = 15
    if v < 0:
        v = 0
        shake = 0

    if v == 0:
        
        caryD = 0

    if v == 15:
        shake = 2.2

    l = l + 0.3

    if l > 0+shake:
        l = 0

    s = s - v
    
    if s < -99:
        s = 0

    for i, (x, y, surface) in enumerate(stones):
        x = x - v
        if x < -100:
            ny =  random.randint(0, 100)
    
            stones[i] = (840 + random.randint(0, 900), ny , surface )
        else:
            stones[i] = (x, y, surface)

    for i, (x, y, surface) in enumerate(stoneas):
        x = x - v
        if x < -100:
            ny =  random.randint(400, 550)
    
            stoneas[i] = (840 + random.randint(0, 900), ny , surface )
        else:
            stoneas[i] = (x, y, surface)

    sandx = sandx - v
    if (sandx) <= -256:
        sandx = 0
    
    # Controlling the car
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                caryD = -1 

            if event.key == pygame.K_s:
                caryD = +1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                caryD = 0

            if event.key == pygame.K_s:
                caryD = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                a = 0.2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                a = 0


        # Quit the game
        if event.type == pygame.QUIT:
            running = False



    pygame.draw.circle(screen, Colour_4, (710, 83), 80)

    screen.blit(text_surface16, (685, 110))

    screen.blit(text_surface1, (640, 70))

    screen.blit(text_surface5, (699, 10))
 
    screen.blit(text_surface10, (754, 70))

    vink = math.radians(v/15*235-225)

    pygame.draw.line(screen, Colour_2, (710, 80), (710 + math.cos(vink)*50, 80 + math.sin(vink)*50), 10)

    pygame.draw.circle(screen, Colour_2, (713, 83), 10)

    # Shows everything on the screen
    pygame.display.flip()


    # FPS
    clk.tick (60)