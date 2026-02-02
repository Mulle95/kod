# import the pygame module
import pygame

# Define the background colour
# using RGB color coding.
background_colour = (0, 150, 0)



Colour_1 = (255, 255, 0)

Colour_2 = (0, 0, 0)

Colour_3 = (120, 120, 120)




clk = pygame.time.Clock()

# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((500, 500))

# Set the caption of the screen
pygame.display.set_caption('fb<dfb<fdbi')


screen.fill(background_colour)

pygame.draw.rect(screen, Colour_2, pygame.Rect(0, 115, 500, 250))

pygame.draw.rect(screen, Colour_3, pygame.Rect(0, 350, 500, 50))

pygame.draw.rect(screen, Colour_3, pygame.Rect(0, 65, 500, 50))

s = 0

v = 10

a = 0

f = 0

shake = 2

pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 25, 230, 50, 10))

pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 125, 230, 50, 10))

pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 225, 230, 50, 10))

pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 325, 230, 50, 10))

pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 425, 230, 50, 10))

# Update the display using flip
pygame.display.flip()

imageM = pygame.image.load("Macka.png")
imageM = pygame.transform.scale(imageM, (1223/9, 553/9))

imageW = pygame.image.load("Macka W.png")
imageW = pygame.transform.scale(imageW, (1223/9, 553/9))

imageS = pygame.image.load("Macka S.png")
imageS = pygame.transform.scale(imageS, (1223/9, 553/9))

image = imageM

k = 100

l = 0

cary = 270

caryD = 0

# Variable to keep our game loop running
running = True



while running:
    screen.fill(background_colour)

    pygame.draw.rect(screen, Colour_2, pygame.Rect(0, 115, 500, 250))

    pygame.draw.rect(screen, Colour_3, pygame.Rect(0, 350, 500, 50))

    pygame.draw.rect(screen, Colour_3, pygame.Rect(0, 65, 500, 50))

    pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 25, 230, 50, 10))

    pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 125, 230, 50, 10))

    pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 225, 230, 50, 10))

    pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 325, 230, 50, 10))

    pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 425, 230, 50, 10))

    pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 525, 230, 50, 10))

   

    screen.blit(image, (k, cary+l))
    if v != 0:
        if caryD < 0:
            cary = cary-1
            image = imageW
        if caryD > 0:
            cary = cary+1
            image = imageS
        if caryD == 0:
            image = imageM

    if cary + 553/9 > 370:
        f = -0.3
        shake = 5

        if v > 10:
            f = -0.3
        else:
            f = -0.1


    else:
        f = -0.015  #FRiction för asfalt
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
        shake = 2.9




    l = l + 0.3

    if l > 0+shake:
        l = 0

    s = s - v
    
    if s < -99:
        s = 0
    
    

    #pygame.draw.rect(screen, Colour_3, pygame.Rect(0, 350, 500, 50))
    #pygame.draw.rect(screen, Colour_3, pygame.Rect(0, 65, 500, 50))

    

# for loop through the event queue  
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

    # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    clk.tick (60)