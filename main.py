import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Animated Character")
 
walkRight =[pygame.image.load('pose1.png'),pygame.image.load('pose2.png'),pygame.image.load('pose3.png'),pygame.image.load('pose4.png')]
 
bg = pygame.image.load('bg.jpg')
bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))
char = pygame.image.load('pose1.png')
 
x = 300
y = 500
width = char.get_width()
height = char.get_height()
vel = 5
 
clock = pygame.time.Clock()
 
left = False
right = False
walkCount = 0
 
def redrawGameWindow():
   global walkCount
 
   win.blit(bg, (0,0)) 
   if walkCount + 1 >= 12:
     walkCount = 0
      
   if left: 
     win.blit(pygame.transform.flip(walkRight[walkCount//3],True,False), (x,y))
     walkCount += 1                         
   elif right:
     win.blit(walkRight[walkCount//3], (x,y))
     walkCount += 1
   else:
     win.blit(char, (x, y))
     walkCount = 0
      
   pygame.display.update()
  
 
 
run = True
 
while run:
   clock.tick(24)
 
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False
 
   keys = pygame.key.get_pressed()
  
   if keys[pygame.K_LEFT] and x > vel:
       x -= vel
       left = True
       right = False
 
   elif keys[pygame.K_RIGHT] and x < WIDTH - vel - width: 
       x += vel
       left = False
       right = True
      
   else:
       left = False
       right = False
       walkCount = 0
 
   redrawGameWindow()
  
  
pygame.quit()
