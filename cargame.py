import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("crash.wav")

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))#game resolution

pygame.display.set_caption('Racer')#caption of display

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
green = (0,200,0)
blue = (0,0,255)
car_speed = 0
car_width = 73
pause = True

clock = pygame.time.Clock()#fps
carImg = pygame.image.load('racecar.png')#get image

def things_dodged(count):#count objects dodged
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged:" + str(count), True, black)
    gameDisplay.blit(text,(0,0))
    
def things(thingx, thingy, thingw,  thingh, color):#draw object
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    
def car(x,y):#add car image on display
    gameDisplay.blit(carImg, (x,y))
    
def text_objects(text, font):#Design text object
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):#Display message when crash
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf , TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()#update display when  crash
    
    time.sleep(1)#Wait 1 second
    
    game_loop()# Start game again
    
def crash():#display text when crash
    pygame.mixer.Sound.play(crash_sound)#play crash sound
    pygame.mixer.music.stop()#stop music

    largeText = pygame.font.SysFont("comicsans", 115)#font for large text
    TextSurf, TextRect = text_objects("Crashed!!!", largeText)#add text and font
    TextRect.center = ((display_width / 2), (display_height / 2))#text position
    gameDisplay.blit(TextSurf, TextRect)#display text

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Try Again", 150, 450, 100, 50, green, bright_green,game_loop)#green try again button
        button("Quit",550, 450, 100, 50, red, bright_red, quitgame)#red quit button

        pygame.display.update()#update display
        clock.tick()#display fps
    #message_display("Crashed!!!")

def button(msg,x,y,w,h,ic,ac, action = None):#create button function
    """msg: What you want the button to say on it.

        x: The x location of the top left coordinate of the button box.

        y: The y location of the top left coordinate of the button box.

        w: Button width.

        h: Button height.

        ic: Inactive color (when a mouse is not hovering).

        ac: Active color (when a mouse is hovering)."""
    mouse = pygame.mouse.get_pos()#get mouse position
    click = pygame.mouse.get_pressed()#get mouse click
    print(click)

    if x + w > mouse[0] > x and y + h > mouse[1] > y:#if mouse at the button position
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))#display bright color for the button
        if click[0] == 1 and action != None:#if mouse clicked
            action()#start the function
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))#display dark color for the button

    smallText = pygame.font.Font("freesansbold.ttf", 20)#font for small text
    TextSurf, TextRect = text_objects(msg, smallText)#add text and font
    TextRect.center = ((x + (w / 2)), (y + (h / 2 )))#text postition
    gameDisplay.blit(TextSurf, TextRect)#display text

def unpause():#unpause function
    global pause
    pause = False

def paused():#pause function
    pygame.mixer.music.pause()#pause music
    largeText = pygame.font.SysFont("comicsansms", 115)#font for large text
    TextSurf, TextRect = text_objects("Paused", largeText)#add text and font
    TextRect.center = ((display_width / 2), (display_height / 2))#text position
    gameDisplay.blit(TextSurf, TextRect)#display text

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        #gameDisplay.fill(white)#fill display with white

        button("Continue", 150, 450, 100, 50, green, bright_green, unpause)#green pause button
        button("Quit",550, 450, 100, 50, red, bright_red, quitgame)#red quit button

        pygame.display.update()#update display
        clock.tick(15)#display fps

def quitgame():#quit function
    pygame.quit()
    quit()

def game_intro():
    intro = True

    pygame.mixer.music.load("jazz.wav")#load music
    pygame.mixer.music.play(-1)#play music until stop

    while intro:#run until crashed
        for event in pygame.event.get():#events logged
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)#fill the display with white color
        largeText = pygame.font.SysFont('comicsansms',115)#font for large text
        TextSurf, TextRect = text_objects("Racer", largeText)#add text and font
        TextRect.center = ((display_width / 2), (display_height / 2))#title position
        gameDisplay.blit(TextSurf, TextRect)#display title

        button("Play",150, 450, 100, 50, green, bright_green,game_loop)#green play buton

        button("Quit",550, 450, 100, 50, red, bright_red, quitgame)#red quit button

        #pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))#display red color for the button

        pygame.display.update()#update display
        clock.tick(15)#menu fps        

def game_loop():
    pygame.mixer.music.load("jazz2.wav")#load music
    pygame.mixer.music.play(-1)#play music until stop

    global pause

    x = (display_width * 0.45)
    y = (display_height * 0.8)
    
    x_change = 0
    
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
    
    thingCount =  1
    
    dodged = 0
    
    gameExit = False

    while not gameExit:#run until crashed
        for event in pygame.event.get():#events logged
        
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                if event.key == pygame.K_RIGHT:
                    x_change = 7
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    pause = False
                    
        x += x_change
    
        gameDisplay.fill(white)#Fill display with color
        
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed# object goes with the speed
        
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
        
        if x > display_width - car_width or x < 0:#crash if car touchs boundaries
            crash()

        if thing_starty > display_height:#if object goes out of display
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 0.1
            thing_width += (dodged * 1.01)
        
        if y < thing_starty + thing_height:# if car y collides with object y 
            print("y crossover")
            if x > thing_startx and x <thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width: #if car x collides with object x 
                print("x crossover")
                crash()    
        pygame.display.update()#update display 
        clock.tick(60)#set fps

game_intro()
game_loop()
pygame.quit()
quit()