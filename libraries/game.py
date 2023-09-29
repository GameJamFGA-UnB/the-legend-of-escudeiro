import pygame as pg
import math as mt
import sys
from pygame.locals import *
import random
import numpy as np
from libraries.default_values import *


import libraries.player as pl 
FramePerSec = pg.time.Clock()


damage_sfx = "assets/sounds/damage.wav"
death_sfx = "assets/sounds/death.wav"
arrow_sfx = "assets/sounds/explosion_arrow.wav"
fire_sfx = "assets/sounds/explosion_fire.wav"
snake_sfx = "assets/sounds/explosion_snake.wav"
arrow_sfx = "assets/sounds/explosion_arrow.wav"

pg.mixer.init()

forest_music = "assets/sounds/forest_music.wav"
dungeon_music = "assets/sounds/dungeon_music.wav"
demon_music = "assets/sounds/demon_music.wav"
final_music = "assets/sounds/final_battle.wav"



song = pg.mixer.music


class Game(pg.sprite.Sprite):
    def __init__(self, wav_obj, controller, map):
        #self.wav_obj = wave.open(wav_obj, 'rb')
        self.exit = False
        self.gameover = False
        self.map = map
        self.surf = pg.Surface((WIDTH,HEIGHT))
        self.surf.set_colorkey(mask)
        self.player = pl.Player()
        self.hero = pl.Hero()
        self.hud = pl.Hud(map)
        if map == 4: 
            self.hero.face("lookup")
            self.player.lifes = 8
        elif map == 8:
            self.hero.face("capybara")
            self.player.lifes = 32
        else: self.hero.face("swordup")
        self.floor = pl.Floor(map, True)
        self.ceiling = pl.Ceiling(map)
        self.entities = []
        self.particles = []
        self.timer = 1
        self.first_play = True
        #self.entities = [self.hero]
        pass


    def update(self):
        if self.first_play == True: 
            if self.map == 1: song.load(forest_music)
            if self.map == 2: song.load(dungeon_music)
            if self.map == 4: song.load(demon_music)
            if self.map == 8: song.load(final_music)   
            song.play()
            self.first_play = False
        self.surf.fill(mask)
        if self.player.lifes <= 0: 
            self.gameover = True
            song.stop()
        if not song.get_busy():
            song.stop()
            self.exit = True
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == K_ESCAPE:
                    self.gameover = True
                    song.stop()
                if event.key in [K_w, K_UP]:
                    self.player.face("up")
                    pass
                if event.key in [K_s, K_DOWN]:
                    self.player.face("down")
                    pass
                if event.key in [K_a, K_LEFT]:
                    self.player.face("left")
                    pass
                if event.key in [K_d, K_RIGHT]:
                    self.player.face("right")
                    pass
                if event.key in [K_1]:
                    pass
        if random.randint(0, 64/self.map) == 0 and self.timer == 0: 
            self.entities.append(pl.Projectiles("random", 4))
        self.timer -= 1
        if self.timer < 0:
            self.timer = 1

        self.surf.blit(self.floor.surf, self.floor.rect)
        self.surf.blit(self.player.surf, self.player.rect)
        self.surf.blit(self.hero.surf, self.hero.rect)
        for entity in self.entities:
            self.surf.blit(entity.surf, entity.rect)
            entity.update()
            if self.player.hitbox_check(entity):
                if entity.type == "arrow": sfx = pg.mixer.Sound(arrow_sfx) 
                if entity.type == "fire":sfx = pg.mixer.Sound(fire_sfx)
                if entity.type == "snake":sfx = pg.mixer.Sound(snake_sfx)
                self.particles.append(pl.Particles("default", vec(entity.pos.x-64,entity.pos.y-64)))
                self.entities.remove(entity)
                sfx.set_volume(0.2)
                sfx.play()
            if self.hero.hitbox_check(entity):
                self.player.lifes -= 1
                print(self.player.lifes)
                self.particles.append(pl.Particles("default", vec(WIDTH/2-64, HEIGHT/2-64)))
                self.entities.remove(entity)
                sfx = pg.mixer.Sound(death_sfx)
                sfx.set_volume(0.4)
                sfx.play()
        self.surf.blit(self.ceiling.surf, self.ceiling.rect)
        for entity in self.particles:
            entity.update()
            self.surf.blit(entity.surf, entity.rect)
            if entity.frame >= entity.size:
                self.particles.remove(entity)
        
        self.hud.update(self.player.lifes)
        self.surf.blit(self.hud.surf, self.hud.rect)
        

    def level():
        player = pl.Player
        