import pygame
import os
from network import Network
from player import Player
import sys
pygame.font.init()
pygame.mixer.init()
ALPHA=(255,255,255)
#path = r"F:\Hacknite"
path = ""
FPS = 40
WIDTH, HEIGHT = 1067, 600
OBS_W, OBS_H = 60,60
#ani = 8
ani = 1
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        
pygame.display.set_caption("Medieval Game")

def def_images():
    global BG, IMG, IMG2, IMG3, IMG4, IMG5, IMG6, IMG7, IMG8, IMG9, IMG10, IMG11, IMG12, IMG13
    BG = pygame.image.load(os.path.join(path,"Background_images","Background_01.png"))
    
    IMG = "Ground_02.png"
    IMG2 = "Ground_08.png"
    IMG3 = "Spikes.png"
    IMG4 = "Ground_05.png"
    IMG5 = "Ground_06.png"
    IMG6 = "Ground_04.png"
    IMG7 = "Bridge_02_edited.png"
    IMG8 = "Ground_10.png"
    IMG9 = "Ground_12.png"
    IMG10 = "Ground_11.png"
    IMG11 = "Ground-Additional_01.png"
    IMG12 = "Coin_02.png"
    IMG13 = "Life.png"
      
def create_ground(obs_ground):
    for i in range(5):
        obs_ground.append((pygame.Rect(OBS_W*i, HEIGHT-OBS_H, OBS_W, OBS_H),IMG))
    obs_ground.append((pygame.Rect(OBS_W*5, HEIGHT-OBS_H, OBS_W, OBS_H),IMG2))
    # for i in range(6,13):
    #     obs_ground.append((pygame.Rect(OBS_W*i, HEIGHT-OBS_H, OBS_W, OBS_H),IMG3))
    obs_ground.append((pygame.Rect(OBS_W*13, HEIGHT-(OBS_H), OBS_W, OBS_H),IMG6))
    obs_ground.append((pygame.Rect(OBS_W*16, HEIGHT-(OBS_H), OBS_W, OBS_H),IMG6))
    obs_ground.append((pygame.Rect(OBS_W*17, HEIGHT-(OBS_H), OBS_W, OBS_H),IMG))

def create_plaform(obs_plat):
    obs_plat.append((pygame.Rect(OBS_W*(6.5), HEIGHT-(OBS_H)*2, 64, 34),IMG7))
    obs_plat.append((pygame.Rect(OBS_W*(8), HEIGHT-(OBS_H)*(2.5), 64, 34),IMG7))
    obs_plat.append((pygame.Rect(OBS_W*(9.5), HEIGHT-(OBS_H)*(3), 64, 34),IMG8))
    obs_plat.append((pygame.Rect(OBS_W*(10.5), HEIGHT-(OBS_H)*(3), 64, 34),IMG9))
    obs_plat.append((pygame.Rect(OBS_W*(12), HEIGHT-(OBS_H)*(2.25), 64, 34),IMG7))
    obs_plat.append((pygame.Rect(OBS_W*(8), HEIGHT-(OBS_H)*(4), 64, 34),IMG7))
    obs_plat.append((pygame.Rect(OBS_W*(6), HEIGHT-(OBS_H)*(4), OBS_W, OBS_H),IMG9))
    obs_plat.append((pygame.Rect(OBS_W*(5), HEIGHT-(OBS_H)*(4), OBS_W, OBS_H),IMG10))
    obs_plat.append((pygame.Rect(OBS_W*(4), HEIGHT-(OBS_H)*(4), OBS_W, OBS_H),IMG10))
    obs_plat.append((pygame.Rect(OBS_W*(3), HEIGHT-(OBS_H)*(4), OBS_W, OBS_H),IMG10))
    #obs_plat.append((pygame.Rect(OBS_W*(2), HEIGHT-(OBS_H)*(4), OBS_W, OBS_H),IMG10))
    obs_plat.append((pygame.Rect(OBS_W*(2), HEIGHT-(OBS_H)*(4), OBS_W, OBS_H),IMG8))
    obs_plat.append((pygame.Rect(OBS_W*(1.3), HEIGHT-(OBS_H)*(5.4), 64, 34),IMG7))
    obs_plat.append((pygame.Rect(OBS_W*(2.3), HEIGHT-(OBS_H)*(6.8), 64, 34),IMG7))
    
    obs_plat.append((pygame.Rect(OBS_W*(8.5), HEIGHT-(OBS_H)*(8), OBS_W, OBS_H),IMG9))
    obs_plat.append((pygame.Rect(OBS_W*(7.5), HEIGHT-(OBS_H)*(8), OBS_W, OBS_H),IMG10))
    obs_plat.append((pygame.Rect(OBS_W*(6.5), HEIGHT-(OBS_H)*(8), OBS_W, OBS_H),IMG10))
    obs_plat.append((pygame.Rect(OBS_W*(5.5), HEIGHT-(OBS_H)*(8), OBS_W, OBS_H),IMG10))
    obs_plat.append((pygame.Rect(OBS_W*(4.5), HEIGHT-(OBS_H)*(8), OBS_W, OBS_H),IMG10))
    #obs_plat.append((pygame.Rect(OBS_W*(3.5), HEIGHT-(OBS_H)*(6.5), OBS_W, OBS_H),IMG10))
    obs_plat.append((pygame.Rect(OBS_W*(3.5), HEIGHT-(OBS_H)*(8), OBS_W, OBS_H),IMG8))
    #obs_plat.append((pygame.Rect(OBS_W*(7.8), HEIGHT-(OBS_H)*(7.25), 64, 34),IMG7))
    #obs_plat.append((pygame.Rect(OBS_W*(6.5), HEIGHT-(OBS_H)*(8), 64, 34),IMG7))
    #obs_plat.append((pygame.Rect(OBS_W*(7.8), HEIGHT-(OBS_H)*(7.7), 64, 34),IMG7))
    obs_plat.append((pygame.Rect(OBS_W*(9.5), HEIGHT-(OBS_H)*(8.75), OBS_W, OBS_H),IMG8))
    obs_plat.append((pygame.Rect(OBS_W*(10.5), HEIGHT-(OBS_H)*(8.75), OBS_W, OBS_H),IMG10))
    obs_plat.append((pygame.Rect(OBS_W*(11.5), HEIGHT-(OBS_H)*(8.75), OBS_W, OBS_H),IMG10))
    obs_plat.append((pygame.Rect(OBS_W*(12.5), HEIGHT-(OBS_H)*(8.75), OBS_W, OBS_H),IMG9))
    obs_plat.append((pygame.Rect(OBS_W*(15), HEIGHT-(OBS_H)*(7), OBS_W, OBS_H),IMG8))
    obs_plat.append((pygame.Rect(OBS_W*(16), HEIGHT-(OBS_H)*(7), OBS_W, OBS_H),IMG10))
    obs_plat.append((pygame.Rect(OBS_W*(17), HEIGHT-(OBS_H)*(7), OBS_W, OBS_H),IMG10))
    obs_plat.append((pygame.Rect(OBS_W*(13), HEIGHT-(OBS_H)*(6), 64, 34),IMG7))
    obs_plat.append((pygame.Rect(OBS_W*(15), HEIGHT-(OBS_H)*(5), 64, 34),IMG7))
    obs_plat.append((pygame.Rect(OBS_W*(13.75), HEIGHT-(OBS_H)*(3.7), 64, 34),IMG7))
    
def create_coins(coins_set):
    coins_set.append(pygame.Rect(OBS_W*16.75,HEIGHT-(OBS_H)*(1.5),25,25))
    coins_set.append(pygame.Rect(OBS_W*13.25,HEIGHT-(OBS_H)*(1.5),25,25))
    coins_set.append(pygame.Rect(OBS_W*10.25,HEIGHT-(OBS_H)*(3.55),25,25))
    coins_set.append(pygame.Rect(OBS_W*5,HEIGHT-(OBS_H)*(6),25,25))
    
def draw_hearts(hearts_set):
    hearts_set.append(pygame.Rect(0,0,30,30))
    hearts_set.append(pygame.Rect(32,0,30,30))
    hearts_set.append(pygame.Rect(64,0,30,30))
    
class Platform(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img, image_folder):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(os.path.join('image, img)).convert()
        self.image = pygame.image.load(os.path.join(path, image_folder, img))
        #self.image.convert_alpha()
        #self.image.set_colorkey(ALPHA)
        self.image = pygame.transform.scale(self.image,(imgw,imgh))
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

class Level:
    def ground(obs_ground):
        ground_list = pygame.sprite.Group()
        i = 0
        while i < len(obs_ground):
            ground = Platform((obs_ground[i][0]).x, (obs_ground[i][0]).y, OBS_W, OBS_H, obs_ground[i][1],'Platformer_images')
            ground_list.add(ground)
            i = i + 1
        return ground_list
    
    def coins(coins_set):
        coins_list = pygame.sprite.Group()
        i = 0
        while i < len(coins_set):
            ground = Platform((coins_set[i]).x, (coins_set[i]).y, 25, 25, IMG12,'Collectable_Object_images')
            coins_list.add(ground)
            i = i + 1
        return coins_list
    
    def hearts(hearts_set):
        hearts_list = pygame.sprite.Group()
        i = 0
        while i < len(hearts_set):
            ground = Platform((hearts_set[i]).x, (hearts_set[i]).y, 30, 30, IMG13,'Collectable_Object_images')
            hearts_list.add(ground)
            i = i + 1
        return hearts_list
    
    
    def platform(obs_plat):
        plat_list = pygame.sprite.Group()
        i=0
        while i < len(obs_plat):
            plat = Platform((obs_plat[i][0]).x, (obs_plat[i][0]).y, (obs_plat[i][0]).width, (obs_plat[i][0]).height, obs_plat[i][1],'Platformer_images')
            plat_list.add(plat)
            i=i+1
        
        return plat_list


def main(): 
    clock = pygame.time.Clock()
    run = True
    def_images()
    obs_ground = []
    create_ground(obs_ground)

    obs_plat = []
    create_plaform(obs_plat)

    coins_set = []
    create_coins(coins_set)

    heart_set = []
    draw_hearts(heart_set)

    ground_list = Level.ground(obs_ground)
    plat_list = Level.platform(obs_plat)
    coins_list = Level.coins(coins_set)
    heart_list = Level.hearts(heart_set)
    
    
    n = Network()
    player2 = Player()
    lis = n.getP()
    player2.rect.x = lis[0]
    player2.rect.y = lis[1]
    player2.width = lis[2]
    player2.height = lis[3]
    player2.parity = lis[4]
    #print(lis,"player 2")

    player = Player()  # spawn player
    if(lis[5]==0):
        player.rect.x = 0  # go to x
        player.rect.y = 0 # go to y
    else:
        player.rect.x = 1067-50  # go to x
        player.rect.y = 0 # go to y
        player.image=pygame.transform.flip(player.image, True, False)
            

    player_list = pygame.sprite.Group()
    player_list.add(player)
    steps = 10

    player_list.add(player2)
    
    while run:
        clock.tick(FPS)
        lis = n.send([player.rect.x,player.rect.y,player.width,player.height,player.parity])
        #print(lis)
        if lis[0]==None:
            run = False
            pygame.quit()
            sys.exit()

        player2.rect.x = lis[0]
        player2.rect.y = lis[1]
        player2.width = lis[2]
        player2.height = lis[3]
        player2.parity = lis[4]
        
        if(player2.parity == -1):
            img = pygame.image.load(os.path.join(path, 'Knight', 'run1-removebg-preview.png')).convert_alpha()
            img = pygame.transform.scale(img, (player.width, player.height))
            player2.image=pygame.transform.flip(img, True, False)
            #player2.parity = prev_parity
        else:
            img = pygame.image.load(os.path.join(path, 'Knight', 'run1-removebg-preview.png')).convert_alpha()
            player2.image = pygame.transform.scale(img, (player.width, player.height))
            

        #print(lis,"player 2")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.control(-steps, 0)
                    
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.control(steps, 0)
                    
                if event.key == pygame.K_UP or event.key == ord('w'):
                    player.jump()
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.control(steps, 0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.control(-steps, 0)

        WIN.blit(BG,(0,0))
        img11 = pygame.image.load(os.path.join(path,"Platformer_images",IMG11))
        img11 = pygame.transform.scale(img11,(OBS_W, OBS_H + 30))
        WIN.blit(img11,(OBS_W*(12.5), HEIGHT-(OBS_H)*(9.75)-30))

        rec = pygame.Rect((OBS_W*(12.5), HEIGHT-(OBS_H)*(9.75)-30),(OBS_W, OBS_H + 30) )
        if not(player.update(ground_list,plat_list,coins_list,heart_list,rec)):
            n.send([None,None,None,None,None])
            run = False
            pygame.quit()
            sys.exit()
        
        player.gravity()
        #player.shrink()
        player_list.draw(WIN)
        ground_list.draw(WIN)
        plat_list.draw(WIN)
        coins_list.draw(WIN)
        heart_list.draw(WIN)

        pygame.display.flip()
        clock.tick(FPS)

        
    main()

if __name__ == "__main__":
    main()
