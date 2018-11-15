import pygame, sys

pygame.init()
scr = pygame.display.set_mode((1000,600))
bg = pygame.image.load("pilved.png")

world_x= 0
world_y= 420

jump_init = False
jump_veloc = 20

obstructions = [(-300,510),(-300,540),(-150,420),(-180,420),(-180,450)]

def world1(X,Y):
    scr.fill((50,50,50))
        
    for i in range(5):
        for j in range(150):
            pygame.draw.rect(scr,(100+j,0,0),(X+i*1161,(Y-420)+j*4,1161,4))
        scr.blit(bg,(X+i*1161,Y-420))
        pygame.draw.rect(scr,(100,0,0),(X+i*1161,Y-720,1161,300))
    for i in range(50):          
        pygame.draw.rect(scr,(50-i,50-i,50-i),(X-300,Y+4*i,4300,4))
    
    
    
    
    pygame.draw.rect(scr,(50,50,50),(X+600,Y-120,30,30))
    pygame.draw.rect(scr,(50,50,50),(X+600,Y-150,30,30))
    
    pygame.draw.rect(scr,(50,50,50),(X+450,Y-30,30,30))
    pygame.draw.rect(scr,(50,50,50),(X+480,Y-30,30,30))
    pygame.draw.rect(scr,(50,50,50),(X+480,Y-60,30,30))
    
    
def character():
    pygame.draw.rect(scr,(100,100,100),(300,390,30,6))
    pygame.draw.rect(scr,(100,100,100),(300,390+24,30,6))
    pygame.draw.rect(scr,(100,100,100),(300,390,6,30))
    pygame.draw.rect(scr,(100,100,100),(324,390,6,30))
    
    pygame.draw.rect(scr,(0,0,0),(300,390,30,2))
    pygame.draw.rect(scr,(0,0,0),(300,390+28,30,2))
    pygame.draw.rect(scr,(0,0,0),(300,390,2,30))
    pygame.draw.rect(scr,(0,0,0),(328,390,2,30))
    
    pygame.draw.rect(scr,(0,0,0),(304,390+4,22,2))
    pygame.draw.rect(scr,(0,0,0),(304,390+24,22,2))
    pygame.draw.rect(scr,(0,0,0),(304,390+4,2,22))
    pygame.draw.rect(scr,(0,0,0),(324,390+4,2,22))
    

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                jump_init = True
                
    
    if jump_init == True:
        world_y += jump_veloc
        if jump_veloc > 0:
            if (world_x - (world_x % 30), world_y -(world_y % 30)+30) in obstructions:
                jump_veloc = 0
            elif (30 + world_x - (world_x % 30), world_y -(world_y % 30)+30) in obstructions:
                jump_veloc = 0
        if jump_veloc < 0:
            if (world_x - (world_x % 30), world_y -(world_y % 30)) in obstructions:
                world_y =  world_y -(world_y % 30) + 30
                jump_veloc = 21
                jump_init = False
            elif (30 + world_x - (world_x % 30), world_y -(world_y % 30)) in obstructions:
                world_y =  world_y -(world_y % 30) + 30
                jump_veloc = 21
                jump_init = False
        
        jump_veloc -= 1
    if jump_veloc < -20:
        jump_veloc = 20
        jump_init = False
        
        
    if world_y != 420:
        if jump_init == False:
            if ((world_x - (world_x % 30), world_y - 30) not in obstructions) and ((30 + world_x - (world_x % 30), world_y - 30) not in obstructions):
                world_y -= 10
        if world_y < 420:
            world_y = 420
        
    keys=pygame.key.get_pressed()
         
    if (world_x-30, world_y -((world_y)%30)) not in obstructions:
        if keys[pygame.K_RIGHT]:
            world_x -= 2
    if (world_x+30, world_y -((world_y)%30)) not in obstructions:
        if world_x != 300:
            if keys[pygame.K_LEFT]:
                world_x += 2
        

    
    
        
    world1(world_x,world_y)
    
    character()
    
    
    pygame.display.update()