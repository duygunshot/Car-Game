import pygame
import time

pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))#game resolution

pygame.display.set_caption('Racer')#caption of display

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
car_speed = 0
car_width = 73

clock = pygame.time.Clock()#fps
carImg = pygame.image.load('racecar.png')#get image

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
    
def crash():
    message_display("Crashed!!!")
    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    
    gameExit = False

    while not gameExit:#run until crashed
        for event in pygame.event.get():#get input
        
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                
    
        x += x_change
    
    
        gameDisplay.fill(white)
        car(x,y)
        
        if x > display_width - car_width or x < 0:
            crash()
    
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()