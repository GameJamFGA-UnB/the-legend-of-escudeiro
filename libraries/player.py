import pygame as pg
from pygame.locals import *
from libraries.default_values import *
import random

commonup = pg.transform.scale(pg.image.load('assets/up.png'), (64,128))
lookup = pg.transform.scale(pg.image.load('assets/up_block.png'), (64,128))
lookdown = pg.transform.scale(pg.image.load('assets/down_block.png'), (64,128))
lookleft = pg.transform.scale(pg.image.load('assets/left_block.png'), (64,128))
lookright = pg.transform.scale(pg.image.load('assets/right_block.png'), (64,128))

hero_lookup = pg.transform.scale(pg.image.load('assets/hero_boiano.png'), (64,128))
hero_up = pg.transform.scale(pg.image.load('assets/hero_up.png'), (64,128))
hero_down = pg.transform.scale(pg.image.load('assets/hero_down.png'), (64,128))
hero_sword = pg.transform.scale(pg.image.load('assets/hero_up_sword.png'), (192,128))
hero_swordup = pg.transform.scale(pg.image.load('assets/hero_sword_look.png'), (64,128))
sword = pg.transform.scale(pg.image.load('assets/sword.png'), (64,192))




floor = pg.transform.scale(pg.image.load('assets/floor_template.png'), (256,256))
forest = pg.transform.scale(pg.image.load('assets/floresta.png'), (WIDTH,HEIGHT))
forest_trees = pg.transform.scale(pg.image.load('assets/floresta_arvores.png'), (WIDTH,HEIGHT))
#floor = pg.transform.scale(pg.image.load('assets/floor_template.png'), (WIDTH,HEIGHT))
bossbattle = pg.transform.scale(pg.image.load('assets/boss_battle.png'), (WIDTH,HEIGHT))
dungeon = pg.transform.scale(pg.image.load('assets/dungeon.png'), (WIDTH,HEIGHT))
lastbattle = pg.transform.scale(pg.image.load('assets/last_battle.png'), (WIDTH,HEIGHT))



arrow_up = pg.transform.scale(pg.image.load('assets/projectiles/arrow_up.png'), (64,64))
arrow_down = pg.transform.scale(pg.image.load('assets/projectiles/arrow_down.png'), (64,64))
arrow_left = pg.transform.scale(pg.image.load('assets/projectiles/arrow_left.png'), (64,64))
arrow_right = pg.transform.scale(pg.image.load('assets/projectiles/arrow_right.png'), (64,64))
fire_up = pg.transform.scale(pg.image.load('assets/projectiles/fire_up.png'), (64,64))
fire_down = pg.transform.scale(pg.image.load('assets/projectiles/fire_down.png'), (64,64))
fire_left = pg.transform.scale(pg.image.load('assets/projectiles/fire_left.png'), (64,64))
fire_right = pg.transform.scale(pg.image.load('assets/projectiles/fire_right.png'), (64,64))
snake_up = pg.transform.scale(pg.image.load('assets/projectiles/snake_up.png'), (64,64))
snake_down = pg.transform.scale(pg.image.load('assets/projectiles/snake_down.png'), (64,64))
snake_left = pg.transform.scale(pg.image.load('assets/projectiles/snake_left.png'), (64,64))
snake_right = pg.transform.scale(pg.image.load('assets/projectiles/snake_right.png'), (64,64))

default_blast = [] # 32/32
nuclear_blast = [] #192/192
hero_blast = [] #32/32
for aux in range(1,8):
    default_blast.append(pg.transform.scale(pg.image.load(f'assets/explosions/explosion{aux}.png'), (128,128)))
for aux in range(1,22):
    nuclear_blast.append(pg.transform.scale(pg.image.load(f'assets/explosions/explosion-e{aux}.png'), (776,776)))
for aux in range(1,8):
    hero_blast.append(pg.transform.scale(pg.image.load(f'assets/explosions/explosion-{aux}.png'), (128,128)))


hud = [pg.transform.scale(pg.image.load('assets/life_bar1.png'), (256,64)),
pg.transform.scale(pg.image.load('assets/life_bar2.png'), (256,64)),
pg.transform.scale(pg.image.load('assets/life_bar3.png'), (256,64)),
pg.transform.scale(pg.image.load('assets/life_bar4.png'), (256,64)),
]


class Hero(pg.sprite.Sprite):
    def __init__(self):
        self.icon = hero_lookup
        self.surf = pg.Surface((192,192))
        self.surf.blit(self.icon,(64,0))
        self.surf.fill(mask)
        self.surf.set_colorkey(mask)
        self.rect = self.icon.get_rect()
        self.pos = vec((WIDTH/2, 3*HEIGHT/5))
        self.rect.midbottom = self.pos

    def face(self, face):
        self.rect.midbottom = self.pos
        if face == "lookup": #final level
            self.surf.fill(mask)
            self.rect.midbottom += vec(-64, -64)
            self.surf.blit(hero_lookup,(64,64))
            surface = pg.Surface((64,192))
            surface.set_colorkey(mask)
            surface.blit(sword, (0,0))
            self.surf.blit(surface, (64,0))
            pass
        elif face == "up":
            self.surf.fill(mask)
            self.surf.blit(hero_up,(0,0))
            pass
        elif face == "down":
            self.surf.fill(mask)
            self.surf.blit(hero_down,(0,0))
            pass
        elif face == "sword": # looking north with sword in hand
            self.rect.midbottom += vec(-64,0)
            self.surf.fill(mask)
            self.surf.blit(hero_sword,(0,0))
            pass
        elif face == "swordup":
            self.surf.fill(mask)
            self.surf.blit(hero_swordup,(0,0))
            pass
        else:
            self.surf.fill(mask)

    def hitbox_check(self, entity):
        if ((WIDTH/2-entity.pos.x in range(-32, 32) ) and (HEIGHT/2-entity.pos.y in range(-32, 32) )):
            return True
        return False

class Floor(pg.sprite.Sprite):
    def __init__(self, floor_tipe, add_shadow):
        self.icon = forest
        self.add_shadow = add_shadow
        self.shadow = pg.Surface((256,256))
        self.shadow.blit(floor,(0,0))
        self.shadow.set_alpha(64)
        self.shadow.set_colorkey(mask)
        self.shadow_rect = floor.get_rect()
        self.surf = pg.Surface((WIDTH,HEIGHT))
        self.surf.blit(self.icon,(0,0))
        self.rect = self.icon.get_rect()
        self.pos = vec((WIDTH/2, HEIGHT/2))
        self.rect.center = self.pos
        self.shadow_rect.center = self.pos
        self.set_floor(floor_tipe)
    
    def set_floor(self,floor_type):
        if floor_type == 1:
            self.surf.fill(empty)
            self.surf.blit(forest,(0,0))
            if(self.add_shadow):self.surf.blit(self.shadow,self.shadow_rect)
        if floor_type == 2:
            self.surf.fill(empty)
            self.surf.blit(dungeon,(0,0))
            if(self.add_shadow):self.surf.blit(self.shadow,self.shadow_rect)
        if floor_type == 4:
            self.surf.fill(empty)
            #self.surf.blit(bossbattle,(0,0))
            if(self.add_shadow):self.surf.blit(self.shadow,self.shadow_rect)
        if floor_type == 8:
            self.surf.fill(empty)
            self.surf.blit(lastbattle,(0,0))
        return

class Ceiling(pg.sprite.Sprite):
    def __init__(self, ceiling_type):
        self.icon = forest_trees
        self.surf = pg.Surface((WIDTH,HEIGHT))
        self.surf.blit(self.icon,(0,0))
        self.surf.set_colorkey(mask)
        self.rect = self.icon.get_rect()
        self.pos = vec((WIDTH/2, HEIGHT/2))
        self.rect.center = self.pos
        self.set_ceiling(ceiling_type)


    def set_ceiling(self,floor_type):
        if floor_type == 1:
            self.surf.fill(empty)
            self.surf.blit(forest_trees,(0,0))
        if floor_type == 2:
            self.surf.fill(mask)
        if floor_type == 4:
            self.surf.fill(mask)
        if floor_type == 8:
            self.surf.fill(mask)
        return

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.icon = lookup
        self.surf = pg.Surface((64,128))
        self.surf.blit(self.icon,(0,0))
        self.surf.set_colorkey(mask)
        self.rect = self.icon.get_rect()
        self.lifes = 4;
        self.blockingSide = str();
        self.pos = vec((HEIGHT/2, WIDTH/2))
        self.face("common_up")

    def face(self,side):
        self.blockingSide = side

        if side == "common_up":
            self.pos = vec((WIDTH/2, HEIGHT/4))
            self.rect.midtop = self.pos
            self.surf.fill(empty)
            self.surf.blit(commonup,(0,0))
            pass
        if side == "common_down":
            self.pos = vec((WIDTH/2, 3*HEIGHT/4))
            self.rect.midbottom = self.pos
            self.surf.fill(empty)
            self.surf.blit(commonup,(0,0))
            pass
        if side == "up":
            self.pos = vec((WIDTH/2, HEIGHT/4))
            self.rect.midtop = self.pos
            self.surf.fill(empty)
            self.surf.blit(lookup,(0,0))
            pass
        if side == "down":
            self.pos = vec((WIDTH/2, 3*HEIGHT/4))
            self.rect.midbottom = self.pos
            self.surf.fill(empty)
            self.surf.blit(lookdown,(0,0))
            pass
        if side == "left":
            self.pos = vec((9*WIDTH/32, HEIGHT/2))
            self.rect.midleft = self.pos
            self.surf.fill(empty)
            self.surf.blit(lookleft,(0,0))
            pass
        if side == "right":
            self.pos = vec((23*WIDTH/32, HEIGHT/2))
            self.rect.midright = self.pos
            self.surf.fill(empty)
            self.surf.blit(lookright,(0,0))
            pass

    def getFace(self):
        return self.blockingSide;


    def hitbox_check(self, entity):
        if ((self.pos.x-entity.pos.x in range(-32, 32) ) and (self.pos.y-entity.pos.y in range(-32, 32) )):
            return True
        return False

class Projectiles(pg.sprite.Sprite):
    def __init__(self, typeR, side):
        super().__init__() 
        self.type = typeR
        self.speed = 4
        self.side = side
        self.icon = arrow_up
        self.surf = pg.Surface((64,64))
        self.surf.set_colorkey(mask)
        self.surf.fill(empty)
        self.rect = self.icon.get_rect()
        self.pos = vec((0,0))
        self.face(side)

    def update(self):
        if self.side == UP:
            self.pos.y -= self.speed
            self.rect.midbottom = self.pos
        if self.side == DOWN: #down
            self.pos.y += self.speed
            self.rect.midtop = self.pos
        if self.side == LEFT: #left
            self.pos.x -= self.speed
            self.rect.midright = self.pos
        if self.side == RIGHT: #right
            self.pos.x += self.speed
            self.rect.midleft = self.pos


    def face(self,side):
        if self.type == "random":
            self.type = random.choice(["arrow", "fire", "snake"])
        if side == RANDOM:
            side = random.randint(0,3)
            self.side = side
        if side == UP: #up
            if self.type == "arrow": self.icon = arrow_up
            if self.type == "fire": self.icon = fire_up
            if self.type == "snake": self.icon = snake_up
            self.pos = vec((WIDTH/2, HEIGHT+64))
            self.rect.midbottom = self.pos
        if side == DOWN: #down
            if self.type == "arrow": self.icon = arrow_down
            if self.type == "fire": self.icon = fire_down
            if self.type == "snake": self.icon = snake_down
            self.pos = vec((WIDTH/2, -64))
            self.rect.midtop = self.pos
        if side == LEFT: #left
            if self.type == "arrow": self.icon = arrow_left
            if self.type == "fire": self.icon = fire_left
            if self.type == "snake": self.icon = snake_left
            self.pos = vec((WIDTH+64, HEIGHT/2))
            self.rect.midright = self.pos
        if side == RIGHT: #right
            if self.type == "arrow": self.icon = arrow_right
            if self.type == "fire": self.icon = fire_right
            if self.type == "snake": self.icon = snake_right
            self.pos = vec((-64, HEIGHT/2))
            self.rect.midleft = self.pos
        self.surf.fill(empty)
        self.surf.blit(self.icon,(0,0))


class Particles(pg.sprite.Sprite):
    def __init__(self, typeR, pos):
        super().__init__()
        if(typeR == "default"):
            self.icon = default_blast[0]
            self.size = default_blast.__len__()
        if(typeR == "nuclear"):
            self.icon = nuclear_blast[0]
            self.size = nuclear_blast.__len__()
        if(typeR == "hero"):
            self.icon = hero_blast[0]
            self.size = hero_blast.__len__()
        self.type = typeR
        self.surf = pg.Surface((WIDTH,HEIGHT))
        self.surf.set_colorkey(mask)
        self.surf.fill(mask)
        self.surf.blit(self.icon, pos)
        self.rect = vec(0,0)
        self.blockingSide = str();
        self.pos = pos
        self.frame = 0
        self.time = 3

    def update(self):
        if(self.frame < self.size and self.time == 0):
            if(self.type == "default"):
                self.icon = default_blast[self.frame]
                self.surf.fill(mask)
                self.surf.blit(self.icon, self.pos)
            if(self.type == "nuclear"):
                self.icon = nuclear_blast[self.frame]
                self.surf.fill(mask)
                self.surf.blit(self.icon, vec(-64,-128))
            if(self.type == "hero"):
                self.icon = hero_blast[self.frame]
                self.surf.fill(mask)
                self.surf.blit(self.icon, self.pos)
            self.frame += 1
        self.time -= 1
        if self.time < 0:
            self.time = 3


class Hud(pg.sprite.Sprite):
    def __init__(self, map):
        super().__init__()
        self.icon = hud[3]
        self.map = map
        self.surf = pg.Surface((WIDTH,HEIGHT))
        self.surf.set_colorkey(mask)
        self.surf.fill(mask)
        self.surf.blit(self.icon, vec(8,8))
        self.rect = vec(0,0)

    def update(self, lifes):
        if self.map == 4: auxD = int(lifes/2)
        elif self.map == 8: auxD = int(lifes/8)
        else: auxD = 0
        auxR = lifes%4
        if auxD == 1 and self.map in [1,2]:
            self.icon = hud[auxD]
        elif auxD == 0 and self.map in [1,2]:
            if auxR == 0 and lifes > 0: self.icon = hud[3]
            else: self.icon = hud[auxR -1]
        elif auxD == 4:
            self.icon = hud[3]
        else: 
            self.icon = hud[auxD]
        self.surf.fill(mask)
        self.surf.blit(self.icon, vec(8,8))        
        pass
