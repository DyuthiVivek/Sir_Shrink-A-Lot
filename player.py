import pygame
import os

ALPHA=(255,255,255)
#path = r"F:\Hacknite"
path = ""
FPS = 40
WIDTH, HEIGHT = 1067, 600
OBS_W, OBS_H = 60,60
#ani = 8
ani = 1

class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.lives = 3
        self.is_jumping = True
        self.is_falling = True
        self.images = []
        self.parity = 1
        # for i in range(1, ani+1):
        #     img = pygame.image.load(os.path.join(path, 'Knight', f'run{i}-removebg-preview.png')).convert_alpha()     # optimise alpha
        #     w,h=img.get_size()
        #     img = pygame.transform.scale(img, (w*2, h*2))
        #     self.rect = img.get_rect()
        #     width, height = self.initial = img.get_size() 
        #     self.images.append((img, width, height))
        # self.image=self.images[0][0]
        img = pygame.image.load(os.path.join(path, 'Knight', 'run1-removebg-preview.png')).convert_alpha()
        w,h=img.get_size()
        img = pygame.transform.scale(img, (w*2, h*2))
        self.rect = img.get_rect()
        self.width, self.height = self.initial = img.get_size()
        self.image=img
        self.images.append(img)

    def gravity(self):
        if(self.is_jumping):
            self.movey += 3.2

    def control(self, x, y):
        self.movex += x
        #self.movey += y

    def jump(self):
        if self.is_jumping is False:
            self.is_falling = False
            self.is_jumping = True
    
    def shrink(self):
        shrink_ratio=0.99999999999999994447
        k=0.0000001
        self.image = pygame.transform.scale(self.image, (self.width*shrink_ratio, self.height*shrink_ratio))
        # self.rect.width-=k
        # self.rect.height-=k
        self.width, self.height = self.image.get_size()
        self.rect.y+=self.height*0.0000000000000001

    def coin_collide(self):
        self.image = pygame.transform.scale(self.image, (self.width*3, self.height*3))
        self.rect.width*=1.5
        self.rect.height*=1.5
        self.width, self.height = self.image.get_size()
        print(self.width)

    def update(self,ground_list, plat_list, coins_list, heart_list ,img11):
        
        collide = pygame.Rect.colliderect(self.rect, img11)
        if collide or not(heart_list):
            return False
        
        #print(ground_list)
        ground_hit_list = pygame.sprite.spritecollide(self, ground_list, False)

        for g in ground_hit_list:
            self.movey = 0
            self.rect.bottom = g.rect.top
            self.is_jumping = False  # stop jumping

        # fall off the world
        if self.rect.y > HEIGHT or self.image.get_rect().width==0:
            print("here")
            self.lives -=1
            for h in heart_list:
                pass
            heart_list.remove(h)
            self.image = pygame.transform.scale(self.image, self.initial)
            print(self.image.get_rect().width)
            self.rect.x = 0
            self.rect.y = HEIGHT - OBS_H

        plat_hit_list = pygame.sprite.spritecollide(self, plat_list, False)
        #print(plat_list)
        for p in plat_hit_list:
            self.is_jumping = False  # stop jumping
            self.movey = 0

            if self.rect.bottom <= p.rect.bottom:
                self.rect.bottom = p.rect.top
            else:
                self.movey += 3.2

        coin_hit_list = pygame.sprite.spritecollide(self, coins_list, False)
        for p in coin_hit_list:
            #self.coin_collide()
            coins_list.remove(p)

        if self.is_jumping and self.is_falling is False:
            self.is_falling = True
            self.movey -= 20  # how high to jump
         
        self.rect.x += self.movex
        self.rect.y += self.movey
        
        #self.rect.x = self.rect.x + self.movex
        #self.rect.y = self.rect.y + self.movey
        #print(self.is_falling)
        # moving left
        if self.movex < 0:
            for g in ground_list:
                if self.rect.bottom == g.rect.top:
                    if(self.rect.left <= g.rect.x):
                        self.movey += 2  # how high to jump

            for g in plat_list:
                if self.rect.bottom == g.rect.top:
                    if(self.rect.left <= g.rect.x):
                        self.movey += 2  # how high to jump


            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            #self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)
            self.image = pygame.transform.flip(self.images[0], True, False)
            self.parity = -1
        # moving right
        if self.movex > 0:
            for g in ground_list:
                if self.rect.bottom == g.rect.top:
                    if(self.rect.left <= g.rect.x):
                        self.movey += 2  # how high to jump

            for g in plat_list:
                if self.rect.bottom == g.rect.top:
                    if(self.rect.right >= g.rect.x):
                        self.movey += 2  # how high to jump

            self.frame += 1
            if self.frame > 3*ani:
                self.frame = 0
            #self.image = self.images[self.frame//ani]
            self.image=self.images[0]
            self.parity = 1
        return True

