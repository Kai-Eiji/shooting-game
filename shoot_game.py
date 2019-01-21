# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 12:16:41 2018

@author: 開
"""


# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 22:42:12 2018

@author: 開
"""
import pygame, random

pygame.init()

class Shooter(object):
    
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.hitbox = 50
        self.GameOver = False
        Image = pygame.image.load('shooter3.jpg')
        self.image = pygame.transform.smoothscale(Image,(width,height))
        
    def draw(self,win):
        #pygame.draw.rect(win,(0,0,0),(self.x - (self.width/2), self.y - (self.height/2),self.width,self.height),0)
        pygame.draw.rect(win,(255,0,0),(self.x - (self.width/2),self.y + 40,50,7),0)
        pygame.draw.rect(win,(50,205,50),(self.x - (self.width/2),self.y + 40 ,self.hitbox,7),0)
        
        win.blit(self.image,((self.x - (self.width/2), self.y - (self.height/2))))

    
        
        

        
       
class enemy(object):
    
    def __init__(self,x,y,width,height,vel,end,color,image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.end = end
        self.hitbox = 60
        self.visible = True
        self.color = color
        Image = pygame.image.load(image)
        self.image = pygame.transform.smoothscale(Image,(width,height))
    def draw(self,win):
        if self.visible:
            self.move()
            #pygame.draw.rect(win,self.color,(self.x, self.y, self.width, self.height),0)
            pygame.draw.rect(win,(255,0,0), (self.x - 5, self.y - 20, 60,7),0)
            pygame.draw.rect(win,(255,255,255), (self.x - 5, self.y - 20, self.hitbox,7),0)
            win.blit(self.image,(self.x,self.y))
        
    def move(self):
        
        self.x += self.vel
        
        if self.x + self.width >= self.end - 5:
            self.vel = self.vel * -1
        
        if self.x <= 5 and self.vel < 0:
            self.vel = self.vel * -1
            self.x += 1
        
    
class Bulletts(object):
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.vel = 10
        self.color = color
        
        
    def draw(self, win):
        pygame.draw.circle(win,self.color,(self.x,self.y,),self.radius)

class shooting(object):
    
    
    
    def __init__(self,the_shooter,shooter,screen_height):
        self.the_shooter = the_shooter
        self.shooter = shooter
        self.enemyBulletList = []
        self.screen_height = screen_height
        
    def shoot(self):
        if self.the_shooter.visible:
            if self.the_shooter.x < self.shooter.x + self.shooter.width + 10 and self.the_shooter.x > self.shooter.x - 10:
                if len(self.enemyBulletList) < 5:
                    self.enemyBulletList.append(Bulletts(self.the_shooter.x + int(self.the_shooter.width / 2),self.the_shooter.y + int(self.the_shooter.height /2),5,(0,0,255)))
                self.enemyShoot = 1
        
    def move(self):
        if len(self.enemyBulletList) > 0:
            for self.enemybullet in self.enemyBulletList:
                self.hit(self.enemybullet,self.enemyBulletList)
                
                if self.enemybullet.y <= self.screen_height:
                    self.enemybullet.y += self.enemybullet.vel
                else:
                    self.enemyBulletList.pop(self.enemyBulletList.index(self.enemybullet))            
        
    def hit(self,enemybullet,enemyBulletList):
        enemybullet
        enemyBulletList
        damege = 5
        if enemybullet.y + enemybullet.radius >= self.shooter.y - (self.shooter.height/2) and enemybullet.y - enemybullet.radius <= self.shooter.y +(self.shooter.height / 2) and enemybullet.x + enemybullet.radius >= self.shooter.x - (self.shooter.width/2) and enemybullet.x - enemybullet.radius <= self.shooter.x + (self.shooter.width/2):
            
            enemyBulletList.pop(enemyBulletList.index(enemybullet))
            self.shooter.hitbox -= damege
        elif self.shooter.hitbox <= 0:
            self.shooter.hitbox = 0
            self.shooter.vel = 0
            self.the_shooter.vel = 0
            #bullet.vel = 0
            enemybullet.vel = 0
            
            self.shooter.GameOver = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()            
    
    def draw(self, win):
        
        for self.enemybullet in self.enemyBulletList:        
            pygame.draw.circle(win,self.enemybullet.color,(self.enemybullet.x,self.enemybullet.y,),self.enemybullet.radius)
        
class boss():
    
     def __init__(self,x,y,width,height,vel,end,color,image,hitbox):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.end = end
        self.hitbox = hitbox
        self.solidbox = hitbox
        self.visible = True
        self.color = color
        Image = pygame.image.load(image)
        self.image = pygame.transform.smoothscale(Image,(width,height))
    
        
     def draw(self,win):
        if self.visible:
            self.move()
            #pygame.draw.rect(win,self.color,(self.x, self.y, self.width, self.height),0)
            pygame.draw.rect(win,(255,0,0), (self.x - 5, self.y - 20, self.solidbox,7),0)
            pygame.draw.rect(win,(255,255,255), (self.x - 5, self.y - 20, self.hitbox,7),0)
            win.blit(self.image,(self.x,self.y))
     def move(self):
         i = random.randint(1,15)
         
         if i == 10:
             self.vel = self.vel * -1
        
         elif self.x + self.width >= self.end - 5:
            self.vel = self.vel * -1
        
         elif self.x <= 5 and self.vel < 0:
            self.vel = self.vel * -1
            self.x += 1
            
         self.x += self.vel
         
        

class boss_shooting():
    
    def __init__(self,the_shooter,shooter,screen_height):
        self.the_shooter = the_shooter
        self.shooter = shooter
        self.enemyBulletList = []
        self.screen_height = screen_height
        self.enemyBulletList2 = []
        self.enemyBulletList3 = []
    
    def shoot(self):
        if self.the_shooter.visible:
            if abs((self.the_shooter.x + self.the_shooter.width/2) - (self.shooter.x + self.shooter.width / 2)) < 60 or abs((self.shooter.x + self.shooter.width/2) - (self.the_shooter.x + self.the_shooter.width / 2)) < 60:
                if len(self.enemyBulletList) < 5:
                    self.enemyBulletList.append(Bulletts(self.the_shooter.x + int(self.the_shooter.width / 2),self.the_shooter.y + self.the_shooter.height,5,(255,150,150)))
                if len(self.enemyBulletList2) < 5:
                    self.enemyBulletList2.append(Bulletts(self.the_shooter.x + int(self.the_shooter.width / 2),self.the_shooter.y + self.the_shooter.height,5,(255,150,150)))
                if len(self.enemyBulletList3) < 5:
                    self.enemyBulletList3.append(Bulletts(self.the_shooter.x + int(self.the_shooter.width / 2),self.the_shooter.y + self.the_shooter.height,5,(255,150,150)))
                self.enemyShoot = 1 
    
    
    def hit(self,enemybullet,enemyBulletList):
        enemybullet
        enemyBulletList
        damege = 5
        if enemybullet.y + enemybullet.radius >= self.shooter.y - (self.shooter.height/2) and enemybullet.y - enemybullet.radius <= self.shooter.y +(self.shooter.height / 2) and enemybullet.x + enemybullet.radius >= self.shooter.x - (self.shooter.width/2) and enemybullet.x - enemybullet.radius <= self.shooter.x + (self.shooter.width/2):
            
            enemyBulletList.pop(enemyBulletList.index(enemybullet))
            self.shooter.hitbox -= damege
        elif self.shooter.hitbox <= 0:
            self.shooter.hitbox = 0
            self.shooter.vel = 0
            self.the_shooter.vel = 0
            #bullet.vel = 0
            enemybullet.vel = 0
            
            self.shooter.GameOver = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()            
            
    def move(self):
        
        if len(self.enemyBulletList) > 0:
            for self.enemybullet in self.enemyBulletList:
                self.hit(self.enemybullet,self.enemyBulletList)
                
                if self.enemybullet.y <= self.screen_height:
                    self.enemybullet.y += self.enemybullet.vel                   
                else:
                    self.enemyBulletList.pop(self.enemyBulletList.index(self.enemybullet))     
                    
        if len(self.enemyBulletList2) > 0:
            for self.enemybullet2 in self.enemyBulletList2:
                self.hit(self.enemybullet2,self.enemyBulletList2)
                
                if self.enemybullet2.y <= self.screen_height:
                    self.enemybullet2.y += self.enemybullet.vel
                    self.enemybullet2.x += int(self.enemybullet.vel / 2)
                else:
                    self.enemyBulletList2.pop(self.enemyBulletList2.index(self.enemybullet2))      
                    
        if len(self.enemyBulletList3) > 0:        
            for self.enemybullet3 in self.enemyBulletList3:
                self.hit(self.enemybullet3,self.enemyBulletList3)
                
                if self.enemybullet3.y <= self.screen_height:
                    self.enemybullet3.y += self.enemybullet.vel
                    self.enemybullet3.x -= int(self.enemybullet.vel / 2)
                else:
                    self.enemyBulletList3.pop(self.enemyBulletList3.index(self.enemybullet3))      
                
    def draw(self,win):
        
        for self.enemybullet in self.enemyBulletList:        
            pygame.draw.circle(win,self.enemybullet.color,(self.enemybullet.x,self.enemybullet.y,),self.enemybullet.radius)
        
        
        for self.enemybullet2 in self.enemyBulletList2:        
            pygame.draw.circle(win,self.enemybullet2.color,(self.enemybullet2.x,self.enemybullet2.y,),self.enemybullet2.radius)
        
        for self.enemybullet3 in self.enemyBulletList3:        
             pygame.draw.circle(win,self.enemybullet3.color,(self.enemybullet3.x,self.enemybullet3.y,),self.enemybullet3.radius)
        
       
        
    
    
