import pygame

import random

pygame.font.init()

pygame.init()

# Variabler

running = True

waiting = True

time = 3

w = 50

h = 50

box = pygame.Rect(225, 225, w, h)

my_font = pygame.font.SysFont('Silom', 45)

my_font2 = pygame.font.SysFont('Silom', 35)

my_font3 = pygame.font.SysFont('Silom', 35)

my_font4 = pygame.font.SysFont('Silom', 20)

p1 = False

p2 = False

start = False

Box_Skin1 = (255, 0, 0) #Red

Box_Skin2 = (0, 255, 0) #Green

Box_Skin3 = (106, 13, 173) #Purple

Box_Skin4 = (255, 95, 31) #Orange

colour_1 = (255, 0, 0) #Red, vet ej varför jag har den

colour_2 = (0, 0, 255) #Blue

colour_3 = (255, 255, 255) #White

Select_C = colour_1

background_colour = (0, 0, 0) 
  
screen = pygame.display.set_mode((500, 500))

credits = False

cpu = False

easy = False

medium = False

hard = False

# Timers

pygame.time.set_timer(pygame.USEREVENT, 1000)

pygame.time.set_timer(pygame.USEREVENT+1, 500)

pygame.time.set_timer(pygame.USEREVENT+2, 400)

pygame.time.set_timer(pygame.USEREVENT+3, 200)

pygame.time.set_timer(pygame.USEREVENT+4, 50)

# Window

pygame.display.set_caption('Clicking 4 Life') 

screen.fill(background_colour) 
  
# game loop och grejer till texten

while running: 

    # Skit samma
    
    for event in pygame.event.get(): 
             
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.USEREVENT:
            if start == True:
                time = time - 1
                if time == 0:
                
                    waiting = False

        if not start:
            if event.type ==pygame.MOUSEBUTTONDOWN:
                (mouse_x, mouse_y) = pygame.mouse.get_pos()
                
                if not credits and not cpu:
                
                    if mouse_y>400 and mouse_y<445 and mouse_x>50 and mouse_x<360:
                        print ("you suck!")
                        pygame.quit()
                        
                    if mouse_y>170 and mouse_y<210 and mouse_x>50 and mouse_x<90:
                        Select_C = Box_Skin1
                    if mouse_y>170 and mouse_y<210 and mouse_x>150 and mouse_x<190:
                        Select_C = Box_Skin2
                    if mouse_y>270 and mouse_y<310 and mouse_x>50 and mouse_x<90:
                        Select_C = Box_Skin3
                    if mouse_y>270 and mouse_y<310 and mouse_x>150 and mouse_x<190:
                        Select_C = Box_Skin4

                    if mouse_y>100 and mouse_y<145 and mouse_x>230 and mouse_x<480:
                        start = True 

                    if mouse_y>40 and mouse_y<80 and mouse_x>30 and mouse_x<250:
                        cpu = True

                    elif mouse_y>250 and mouse_y<295 and mouse_x>250 and mouse_x<423:
                        credits = True

                elif credits == True:
                    if mouse_y>0 and mouse_y<45 and mouse_x>2 and mouse_x<78:
                        credits = False

                elif cpu == True:
                    if mouse_y>0 and mouse_y<45 and mouse_x>2 and mouse_x<78:
                        cpu = False
                    if mouse_y>100 and mouse_y<145 and mouse_x>45 and mouse_x<115:
                        start = True
                        easy = True
                    if mouse_y>200 and mouse_y<245 and mouse_x>123 and mouse_x<223:
                        start = True
                        medium = True
                    if mouse_y>344 and mouse_y<389 and mouse_x>313 and mouse_x<385:
                        start = True
                        hard = True

        # Gör att fyrkanten blinkar

        if event.type == pygame.USEREVENT+1:
            if box.left<100 or box.left>350:
                if colour_1 == Select_C:
                     colour_1 = (255, 255, 0)
                elif colour_1 == (255, 255, 0):
                     colour_1 = Select_C
            else:
                colour_1 = Select_C
        elif event.type == pygame.USEREVENT+2:   #Move cpu left
            if cpu and easy and not waiting:
                if random.random()>0.2:

                    box.left=box.left-10

        elif event.type == pygame.USEREVENT+3:   #Move cpu left
            if cpu and medium and not waiting:
                if random.random()>0.1:

                    box.left=box.left-10

        elif event.type == pygame.USEREVENT+4:   #Move cpu left
            if cpu and hard and not waiting:
                if random.random()>0.1:

                    box.left=box.left-10


        # Keyboard

        if event.type == pygame.KEYDOWN:
            if not waiting:
                if  p1 == False and p2 == False:
                    if event.scancode==51:
                         box.left=box.left+10
                    elif event.scancode==52:
                         box.left=box.left+20
                    elif event.scancode==22:
                         box.left=box.left-10
                    elif event.scancode==4:
                         box.left=box.left-20

                elif p1 == True or p2 == True:
                    if event.scancode==44:
                        box = pygame.Rect(225, 225, w, h)
                        waiting = True
                        time = 3
                        p1 = False
                        p2 = False
                    elif event.scancode==41:
                        start = False
                        box = pygame.Rect(225, 225, w, h)
                        waiting = True
                        time = 3
                        p1 = False
                        p2 = False

    # Alla objekt, text och bakgrund
    screen.fill(background_colour) 

    if not start: 

        if credits == True:
            text_surface = my_font.render("Lead Developer", False, (255, 255, 255))
            screen.blit(text_surface, (132,50))
            text_surface = my_font.render("Designer", False, (255, 255, 255))
            screen.blit(text_surface, (182,190))
            text_surface = my_font.render("Composer", False, (255, 255, 255))
            screen.blit(text_surface, (165,330))
            text_surface = my_font.render("MulleFiskBulle", False, (255, 255, 255))
            screen.blit(text_surface, (135,110))
            text_surface = my_font.render("MulleFiskBulle", False, (255, 255, 255))
            screen.blit(text_surface, (135,250))
            text_surface = my_font.render("MulleFiskBulle", False, (255, 255, 255))
            screen.blit(text_surface, (135,400))
            text_surface = my_font4.render("A Small Thanks To My Playtesters", False, (255, 255, 255))
            screen.blit(text_surface, (280,450))
            text_surface = my_font4.render("Emil", False, (255, 255, 255))
            screen.blit(text_surface, (315,465))
            text_surface = my_font4.render("Marcus", False, (255, 255, 255))
            screen.blit(text_surface, (415,465))
            text_surface = my_font4.render("Stephanie", False, (255, 255, 255))
            screen.blit(text_surface, (315,480))
            text_surface = my_font4.render("Jessica", False, (255, 255, 255))
            screen.blit(text_surface, (415,480))
            text_surface = my_font4.render("Thanks Axel I Guess", False, (255, 255, 255))
            screen.blit(text_surface, (20,480))
            text_surface = my_font.render("Esc", False, (255, 255, 255))
            screen.blit(text_surface, (2,0))

        elif cpu == True:

            text_surface = my_font.render("Easy", False, (255, 255, 255))
            screen.blit(text_surface, (45,100))
            text_surface = my_font.render("Medium", False, (255, 255, 255))
            screen.blit(text_surface, (123,200))
            text_surface = my_font.render("Hard", False, (255, 255, 255))
            screen.blit(text_surface, (313,344))
            text_surface = my_font.render("Esc", False, (255, 255, 255))
            screen.blit(text_surface, (2,0))

        else:

            text_surface = my_font.render("Achievments", False, (255, 255, 255))
            screen.blit(text_surface, (50,400))
            text_surface = my_font.render("Player VS Player", False, (255, 255, 255))
            screen.blit(text_surface, (230,100))
            text_surface = my_font.render("Player VS CPU", False, (255, 255, 255))
            screen.blit(text_surface, (30,45))
            text_surface = my_font.render("Credits", False, (255, 255, 255))
            screen.blit(text_surface, (250,250))
            text_surface = my_font.render("Colours", False, (255, 255, 255))
            screen.blit(text_surface, (64,225))
            
            if Select_C == Box_Skin1:

             pygame.draw.rect(screen, colour_3, pygame.Rect(45, 165, 50, 50))

            if Select_C == Box_Skin2:

             pygame.draw.rect(screen, colour_3, pygame.Rect(145, 165, 50, 50))

            if Select_C == Box_Skin3:

             pygame.draw.rect(screen, colour_3, pygame.Rect(45, 265, 50, 50))

            if Select_C == Box_Skin4:

             pygame.draw.rect(screen, colour_3, pygame.Rect(145, 265, 50, 50))

            pygame.draw.rect(screen, Box_Skin1, pygame.Rect(50, 170, 40, 40))
            pygame.draw.rect(screen, Box_Skin2, pygame.Rect(150, 170, 40, 40))
            pygame.draw.rect(screen, Box_Skin3, pygame.Rect(50, 270, 40, 40))
            pygame.draw.rect(screen, Box_Skin4, pygame.Rect(150, 270, 40, 40))

    else:

        pygame.draw.rect(screen, colour_3, pygame.Rect(245, 0, 10, 500))         
        pygame.draw.circle(screen, colour_2, (250, 250), 20)
        pygame.draw.rect(screen, colour_1, box)

        # Updatera texten

        if waiting:
            if time > 0:
                text_surface = my_font.render(str(time), False, (255, 255, 255))
                screen.blit(text_surface, (20,0))
            
        if time == 0:
            text_surface = my_font.render("Go!", False, (255, 255, 255))
            screen.blit(text_surface, (20,0))
            
        if p1 == True:
            text_surface = my_font2.render("Press Space  To Restart", False, (255, 255, 255))
            screen.blit(text_surface, (100,300))
            text_surface = my_font.render("Left  Won", False, (255, 255, 255))
            screen.blit(text_surface, (186,150))
            text_surface = my_font3.render("Press Esc  To Quit", False, (255, 255, 255))
            screen.blit(text_surface, (130,400))

        if p2 == True:
            text_surface = my_font.render("Right  Won", False, (255, 255, 255))
            screen.blit(text_surface, (166,150))
            text_surface = my_font2.render("Press Space  To Restart", False, (255, 255, 255))
            screen.blit(text_surface, (100,300))
            text_surface = my_font3.render("Press Esc  To Quit", False, (255, 255, 255))
            screen.blit(text_surface, (130,400))

        if p1 or p2 == True:
            pygame.draw.rect(screen, background_colour, box,)
            box = pygame.Rect(0, 0, w, h)

        # Slutet av spelet/Hur man vinner

        if box.left<0:
            p1 = True
        elif box.left>450:
            p2 = True
       
    # Sätter allt på skärmen och avslutar spelet

    pygame.display.flip()

pygame.quit()