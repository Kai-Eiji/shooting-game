# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 12:15:11 2018

@author: 開
"""

 # this is the main file to run the game
import shoot_game, pygame

bg = pygame.image.load("bg.png")


        

pygame.init()
screen_width = 800
screen_height = 580
bg = pygame.transform.smoothscale(bg,(screen_width,screen_height))
win = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Shootong Game")
clock = pygame.time.Clock()
title_image = pygame.image.load('opening.jpg')
title_image = pygame.transform.smoothscale(title_image,(int(screen_width * 0.66),int(screen_height * 0.5)))
opening = True


    
run = True
shoot = 0
stage = 0

shooter = shoot_game.Shooter(250,400,50,50)
enemyShooter = shoot_game.enemy(250,100,50,50,9,screen_width,(0,0,255),"enemy6.jpg")
enemyShooting = shoot_game.shooting(enemyShooter,shooter,screen_height)
bulletList = []



enemyShooter2 = shoot_game.enemy(0,100,50,50,9,screen_width,(30,255,255),"enemy4.jpg")
enemyShooting2 = shoot_game.shooting(enemyShooter2,shooter,screen_height)

enemyShooter3 = shoot_game.enemy(740,150,50,50,9,screen_width,(30,255,255),"enemy4.jpg")
enemyShooting3 = shoot_game.shooting(enemyShooter3,shooter,screen_height)


enemyShooter4 = shoot_game.boss(250,100,100,100,5,screen_width,(0,0,255),"boss2.jpg",120)
enemyShooting4 = shoot_game.boss_shooting(enemyShooter4,shooter,screen_height)


def drawscreen(win):
   win.blit(bg, (0,0))
   
   if opening == True:
       win.blit(title_image, (int((screen_width - title_image.get_width()) / 2), 50))
       font = pygame.font.SysFont("comicsans",60)
       text = font.render("Press Enter to Start",1,(255,0,0))
       win.blit(text,(int((screen_width - text.get_width()) / 2),450))
       
   else:
       shooter.draw(win)
       enemyShooter.draw(win)
       enemyShooting.draw(win)
       global stage
       
       if stage == 1 and time1 >= 27:
           enemyShooter2.draw(win)
           enemyShooting2.draw(win)
           
           enemyShooter3.draw(win)
           enemyShooting3.draw(win)
           
       if stage == 4:
           enemyShooter4.draw(win)
           enemyShooting4.draw(win)
       
       if not shooter.GameOver:
           for bullet in bulletList:
               bullet.draw(win)
           
       
           
       if shooter.GameOver and not stage == 6:
           font = pygame.font.SysFont("comicsans",130)
           text = font.render("Game Over",1,(255,0,0))
           win.blit(text, ((screen_width /2) - (text.get_width() /2), (screen_height /2) - text.get_height()/2))
           
       if stage == 3:
           for i in range(5):
               font = pygame.font.SysFont("comicsans",130)
               text2 = font.render("Last Stage",1,(255,0,0))
               win.blit(text2, ((screen_width /2) - (text2.get_width() /2), (screen_height /2) - text2.get_height()/2))
               pygame.display.update()
               pygame.time.wait(200)
               text3 = font.render("Last Stage",1,(255,255,255))
               win.blit(text3, ((screen_width /2) - (text3.get_width() /2), (screen_height /2) - text3.get_height()/2))
               pygame.display.update()
               pygame.time.wait(200)
           
           stage = 4
           
       if stage == 5 and time2 >= 27 and not shooter.GameOver == True:
           font = pygame.font.SysFont("comicsans",100)
           text = font.render("Game Completed!!",1,(0,255,0))
           win.blit(text, ((screen_width /2) - (text.get_width() /2), (screen_height /2) - text.get_height()/2))
           stage = 6
           
       
       
   pygame.display.update()
      
   
   
def my_bullet_hit(enemyShooter,bullet):
    global stage
    if bullet.y - bullet.radius <= enemyShooter.y + enemyShooter.height and bullet.y + bullet.radius >= enemyShooter.y and bullet.x + bullet.radius >= enemyShooter.x and bullet.x - bullet.radius <= enemyShooter.x + enemyShooter.width:
        if enemyShooter.visible:
            try:
                bulletList.pop(bulletList.index(bullet))
                enemyShooter.hitbox -= 5
            except ValueError:
                a = 1
        
        if enemyShooter.hitbox <= 0:
            enemyShooter.visible = False
    
    
   
time1 = 0
time2 = 0 

while run:
    clock.tick(27)
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(stage)
            run = False

    if not opening:
        
        if shoot >= 1:
            shoot += 1
        if shoot == 5:
            shoot = 0

            
        for bullet in bulletList:
            if bullet.y >= 0:
                bullet.y -= bullet.vel
            else:
                bulletList.pop(bulletList.index(bullet))
            
            if stage == 0:
                my_bullet_hit(enemyShooter,bullet)
            elif stage == 1 and time1 >= 27:
                my_bullet_hit(enemyShooter2,bullet)
                my_bullet_hit(enemyShooter3,bullet)
            elif stage == 4:
                my_bullet_hit(enemyShooter4,bullet)
                
        if pygame.time.get_ticks() % 3 == 0:
            if stage == 0:
                enemyShooting.shoot()
            elif stage == 1:
                enemyShooting2.shoot()
                enemyShooting3.shoot()
            elif stage == 4:
                enemyShooting4.shoot()
               
        enemyShooting.move()
        if time1 >= 27:
            enemyShooting2.move()
            enemyShooting3.move()
        enemyShooting4.move()
        
           
        
        if enemyShooter4.visible == False:
            stage = 5
            time2 += 1
        
        elif enemyShooter2.visible == False and enemyShooter3.visible == False and stage == 1:
            stage = 3
            
        elif enemyShooter.visible == False and stage <= 1:
            stage = 1
            time1 += 1
        
       
    
    
    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_RETURN]:
        opening = False
    
    if keys[pygame.K_LEFT] and shooter.x - (shooter.width/2)> 5:
        shooter.x -= shooter.vel
            
    if keys[pygame.K_RIGHT] and shooter.x + (shooter.width/2) < screen_width - 5:
        shooter.x += shooter.vel
        
    if keys[pygame.K_UP] and shooter.y - (shooter.height/2) > 5:
        shooter.y -= shooter.vel

    if keys[pygame.K_DOWN] and shooter.y + (shooter.height/2) < screen_height - 5:
        shooter.y += shooter.vel        
        
    if keys[pygame.K_SPACE] and shoot == 0:
        if len(bulletList) < 7:
            bulletList.append(shoot_game.Bulletts(shooter.x,shooter.y,5,(0,255,0)))
            shoot = 1
            
        
    
       
    drawscreen(win)
    
    
    
  
    
pygame.quit()

