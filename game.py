import pygame
import math, random
from superwires import games, color
vec = pygame.math.Vector2
 
SIZE = WIDTH, HEIGHT = 600, 400 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('red') #The background colod of our window
FPS = 10 #Frames per second
BACKGROUND_IMAGE = pygame.image.load('background.jpg')
# Player properties similar to the self.x += 2 used in lab12
PLAYER_ACC = 0.5
 
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('walk1.png'))
        self.images.append(pygame.image.load('walk2.png'))
        self.images.append(pygame.image.load('walk3.png'))
        self.images.append(pygame.image.load('walk4.png'))
        self.images.append(pygame.image.load('walk5.png'))
        self.images.append(pygame.image.load('walk6.png'))
        self.images.append(pygame.image.load('walk7.png'))
        self.images.append(pygame.image.load('walk8.png'))
        self.images.append(pygame.image.load('walk9.png'))
        self.images.append(pygame.image.load('walk10.png'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(50, 136, 150, 198)
 
    def update(self):
        PLAYER_ACC= 5
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.rect.x -= PLAYER_ACC
        if keys[pygame.K_a]:
            self.rect.x += PLAYER_ACC
       
        self.index += 1
 
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

        
 
def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
        my_group.update()
        #screen.fill(BACKGROUND_COLOR)
        #background image
        screen.blit(BACKGROUND_IMAGE, (0,0))
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(10) 
   
if __name__ == '__main__':
    main()
