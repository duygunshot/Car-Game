import pygame
pygame.init()

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))#game resolution

pygame.display.set_caption('Racer')#caption of display

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()#fps
carImg = pygame.image.load('racecar.png')#get image

def car(x,y):#add car image on display
    gameDisplay.blit(carImg, (x,y))
    
x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
car_speed = 0

crashed = False
while not crashed:#run until crashed
    for event in pygame.event.get():#get input
        
        if event.type == pygame.QUIT:
            crashed = True

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
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()