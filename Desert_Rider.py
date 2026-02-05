import pygame


import random

import math


pygame.mixer.init()

pygame.font.init()


background_colour = (0, 0, 0)

font1 = pygame.font.SysFont('Arial', 25)

font2 = pygame.font.SysFont('BytesizedRegular', 45)

font_score = pygame.font.SysFont('BytesizedRegular', 75)

font_ded = pygame.font.SysFont('BytesizedRegular', 100)

font_ded3 = pygame.font.SysFont('BytesizedRegular', 50)

eat_a_can = pygame.font.SysFont('BytesizedRegular', 50)

text_surface16 = font1.render("KM/H", True, "white")

text_surface1 = font1.render("10", True, "white")

text_surface5 = font1.render("50", True, "white")

text_surface10 = font1.render("100", True, "white")

Mulle = True

C1 = (225, 225, 0)

C2 = (255, 127, 0)

Guh = 255, 0, 0

Gih = 255, 255, 255

text_surfacet = font2.render("PRESS SPACE TO START", True, C1)

text_surfacetd = font2.render("PRESS SPACE TO START", True, C2)

font_deded = font_ded3.render("Press Space To Return To Menu", True, Gih)

font_dedes = font_ded.render(".GAME OVER.", True, Guh)

eat_a_frog = eat_a_can.render("Mulle Productions", True, Gih)

Colour_1 = (235, 235, 235)

Colour_2 = (25 ,25 ,25)

Colour_3 = (62 ,73 ,67)

Colour_4 = (60, 60, 60)

clk = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))

sand = pygame.image.load("Sand.png")

stone1 = pygame.image.load("Stone1.png")
stone1 = pygame.transform.scale(stone1, (150/1.5, 123/1.5))

stone2 = pygame.image.load("Stone2.png")
stone2 = pygame.transform.scale(stone2, (137/1.5, 105/1.5))

stone3 = pygame.image.load("Stone3.png")
stone3 = pygame.transform.scale(stone3, (106/1.5, 75/1.5))

stone4 = pygame.image.load("Stone4.png")
stone4 = pygame.transform.scale(stone4, (86/1.5, 72/1.5))

stone5 = pygame.image.load("Stone5.png")
stone5 = pygame.transform.scale(stone5, (54/1.5, 48/1.5))

Colour_5 = (0, 0, 0)

running = True

imageM = pygame.image.load("CarM.png")
imageM = pygame.transform.scale(imageM, (1223/7, 553/7))

imageW = pygame.image.load("CarW.png")
imageW = pygame.transform.scale(imageW, (1223/7, 553/7))

imageS = pygame.image.load("CarS.png")
imageS = pygame.transform.scale(imageS, (1223/7, 553/7))

enemy = pygame.image.load("Enemy.png")
enemy = pygame.transform.scale(enemy, (1223/7, 553/7))

title_surface = pygame.image.load("Title.png")

smoke = pygame.Surface((10, 10))

smoke.set_alpha(8.5)

smoke.fill((120, 120, 120))

score = 0

gameover = False

sandx = 0

image = imageM

stoneas = [(-150, 100, stone1), (-150, 100, stone1), (-165, 50, stone2), (-165, 50, stone2), (-350, 100, stone3), (-230, 68, stone4), (-350, 100, stone3), (-230, 68, stone4), (-230, 68, stone4), (-230, 68, stone4)]

stones = [(-150, 100, stone1), (-150, 100, stone1), (-165, 50, stone2), (-165, 50, stone2), (-350, 100, stone3), (-230, 68, stone4), (-350, 100, stone3), (-230, 68, stone4), (-230, 68, stone4), (-230, 68, stone4)]

s = 0

v = 0

a = 0

f = 0

shake = 2

k = 100

l = 0

cary = 270

caryD = 0

enemyx = -300

title = False

timger = pygame.USEREVENT + 1

music = ["8Bit i love you.mp3", "8Bit ship.mp3", "8Bit days.mp3", "8Bit my fire.mp3", "8Bit on the storm.mp3"]

musicpos = 0

MUSIC_ENDED = pygame.USEREVENT + 2


pygame.display.set_caption('Desert Rider')


pygame.mixer.music.load("8Bit blues.mp3")

pygame.mixer.music.play(-1) 

pygame.mixer.music.set_volume(0.5)

pygame.mixer.music.set_endevent(MUSIC_ENDED)


pygame.time.set_timer(timger, 3000)


def load_highscore():

    try:

        with open("HighScore.txt", "r") as f:

            return int(f.read())


    except:

        return 0


def save_highscore(value):

    with open("HighScore.txt", "w") as f:

        f.write(str(int(value)))


highscore = load_highscore()


while running:

    if gameover == True:

        score_surface = font_score.render(f"Score: {int(score)}", True, (255,255,255))

        highscore_surface = font_score.render(f"Highscore: {int(highscore)}", True, (255,255,255))


        pygame.draw.rect(screen, Colour_5, pygame.Rect(0, 0, 880, 600))


        screen.blit(highscore_surface, (100, 275))

        screen.blit(score_surface, (100, 175))

        screen.blit(font_dedes, (100, 50))

        screen.blit(font_deded, (50, 475))


    elif title == True:

        screen.fill(background_colour)


        screen.blit(title_surface, (0, 0))

        screen.blit(text_surfacet, (155, 540))

        screen.blit(text_surfacetd, (158, 540))


    elif Mulle == True:

        pygame.draw.rect(screen, Colour_5, pygame.Rect(0, 0, 880, 600))


        screen.blit(eat_a_frog, (50, 50))


        for event in pygame.event.get():

            if event.type == timger:

                title = True

                Mulle = False


    else:

        pygame.draw.rect(screen, Colour_2, pygame.Rect(0, 115+50, 800, 250))


        pygame.draw.rect(screen, Colour_3, pygame.Rect(0, 350+50, 800, 50))

        pygame.draw.rect(screen, Colour_3, pygame.Rect(0, 65+50, 800, 53))


        pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 25, 230+50, 50, 10))

        pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 125, 230+50, 50, 10))

        pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 225, 230+50, 50, 10))

        pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 325, 230+50, 50, 10))

        pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 425, 230+50, 50, 10))

        pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 525, 230+50, 50, 10))

        pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 625, 230+50, 50, 10))

        pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 725, 230+50, 50, 10))

        pygame.draw.rect(screen, Colour_1, pygame.Rect(s + 825, 230+50, 50, 10))


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


        for(x, y, surface) in stones:
            screen.blit(surface, (x, y))

        for(x, y, surface) in stoneas:
            screen.blit(surface, (x, y))


        screen.blit(image, (k, cary+l))

        screen.blit(enemy, (enemyx, 175))


        if v != 0:

            turnv = v/15*2


            if caryD < 0:

                cary = cary-turnv

                image = imageW


            if caryD > 0:

                cary = cary+turnv

                image = imageS


            if caryD == 0:

                image = imageM


        if cary + 553/7 > 410:

            f = -0.3

            shake = 5


            if v > 10:

                f = -0.3


            else:

                f = -0.05


        elif cary + 553/7 < 210:

            f = -0.3

            shake = 5


            if v > 10:

                f = -0.3


            else:

                f = -0.05


        else:

            f = -0.015

            shake = 2


        v = v+a+f


        if v > 15:

            v = 15


        if v < 0:

            v = 0

            shake = 0

        dt = clk.get_time() / 1000 

        wrong_side = False


        if cary < 230:

            wrong_side = True


        if wrong_side and v > 0:

            score += 50 * dt * (v/15)


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


        enemyv = ((1 - v/15)*8 ) +2

        enemyx = enemyx - enemyv-v


        if enemyx < -700: 

            enemyx = random.randint(1700,  5000)


        if k+153 > enemyx  and k < enemyx + 153 and ( (cary+11 > 186 and cary+11 < 233) or ( cary+58 > 186 and cary+58 < 233)):

                gameover = True


                if score > highscore:
                    highscore = int(score)
                    save_highscore(highscore)


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


        if v < 1:

            smoke.set_alpha(0)


        elif v < 2:

            smoke.set_alpha(8.5)


        elif v < 3:

            smoke.set_alpha(8.5*2)


        elif v < 4:

            smoke.set_alpha(8.5*3)


        elif v < 5:

            smoke.set_alpha(8.5*4)


        elif v < 6:

            smoke.set_alpha(8.5*5)


        elif v < 7:

            smoke.set_alpha(8.5*6)


        elif v < 8:

            smoke.set_alpha(8.5*7)


        elif v < 9:

            smoke.set_alpha(8.5*8)


        elif v < 10:

            smoke.set_alpha(8.5*9)


        elif v < 11:

            smoke.set_alpha(8.5*10)


        elif v < 12:

            smoke.set_alpha(8.5*11)


        elif v < 13:

            smoke.set_alpha(8.5*12)


        elif v < 14:

            smoke.set_alpha(8.5*13)


        elif v < 15:

            smoke.set_alpha(8.5*14)


        elif v == 15:

            smoke.set_alpha(8.5*15)


        screen.blit(smoke,(k+random.randint(-20, -2), cary+20+random.randint(-5, +5)) )

        screen.blit(smoke,(k+random.randint(-20, -2), cary+20+random.randint(-5, +5)) )


        pygame.draw.circle(screen, Colour_4, (710, 83), 80)


        score_surface = font_score.render(f"Score: {int(score)}", True, (255,255,255))


        screen.blit(text_surface16, (685, 110))

        screen.blit(text_surface1, (640, 70))

        screen.blit(text_surface5, (699, 10))
    
        screen.blit(text_surface10, (754, 70))


        vink = math.radians(v/15*235-225)


        pygame.draw.line(screen, Colour_2, (710, 80), (710 + math.cos(vink)*50, 80 + math.sin(vink)*50), 10)


        pygame.draw.circle(screen, Colour_2, (713, 83), 10)


    pygame.display.flip()


    for event in pygame.event.get():

        if gameover == True:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:


                    pygame.mixer.music.load("8Bit blues.mp3")

                    pygame.mixer.music.play(-1) 

                    pygame.mixer.music.set_volume(0.5)


                    gameover = False

                    title = True

                    score = 0

                    gameover = False

                    sandx = 0

                    image = imageM

                    stoneas = [(-150, 100, stone1), (-150, 100, stone1), (-165, 50, stone2), (-165, 50, stone2), (-350, 100, stone3), (-230, 68, stone4), (-350, 100, stone3), (-230, 68, stone4), (-230, 68, stone4), (-230, 68, stone4)]

                    stones = [(-150, 100, stone1), (-150, 100, stone1), (-165, 50, stone2), (-165, 50, stone2), (-350, 100, stone3), (-230, 68, stone4), (-350, 100, stone3), (-230, 68, stone4), (-230, 68, stone4), (-230, 68, stone4)]

                    s = 0

                    v = 0

                    a = 0

                    f = 0

                    shake = 2

                    k = 100

                    l = 0

                    cary = 270

                    caryD = 0

                    enemyx = -300

                    title = True

                    musicpos = 0


        elif title == True:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:


                    title = False


                    pygame.mixer.music.load(music[musicpos])


                    musicpos = musicpos + 1


                    pygame.mixer.music.play() 

                    pygame.mixer.music.set_volume(0.5)


        else:

            if event.type == MUSIC_ENDED:


                pygame.mixer.music.load(music[musicpos])

                pygame.mixer.music.play()   


                musicpos = musicpos + 1


                if musicpos >= len(music):

                    musicpos = 0


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

                    a = 0.1


            if event.type == pygame.KEYUP:

                if event.key == pygame.K_SPACE:

                    a = 0


            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LSHIFT:

                    pygame.mixer.music.stop()


    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_ESCAPE:

            running = False


    if event.type == pygame.QUIT:
        running = False


    clk.tick (60)