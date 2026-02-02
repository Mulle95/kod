import pygame

pygame.font.init()

# import the pygame module
import pygame

# Define the background colour
# using RGB color coding.
background_colour = (234, 212, 252)

# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((500, 500))

# Set the caption of the screen
pygame.display.set_caption(':)')

# Fill the background colour to the screen
screen.fill(background_colour)

# Update the display using flip
pygame.display.flip()

# Variable to keep our game loop running
running = True

#Gissa
colour_1 = (0, 0, 0)

my_font1 = pygame.font.SysFont('Silom', 45)

# game loop
while running:
  
# for loop through the event queue  
    for event in pygame.event.get():
    
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False

        pygame.draw.rect(screen, colour_1, pygame.Rect(225, 200, 50, 50))
        
        

        pygame.display.flip()