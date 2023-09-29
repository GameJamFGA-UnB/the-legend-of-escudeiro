import pygame as pg
import math as mt
import sys
from pygame.locals import *
import random
from libraries.default_values import *
import libraries.game as game
#import libraries.cutscene as cs
import libraries.titleScreen as ts
import cx_Freeze


"""
# base = "Win32GUI" allows your application to open without a console window
base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable('main.py', base = base)]

cx_Freeze.setup(
    name = "the legend of escudeiro",
    options = {
        "build_exe" : 
        {"packages" : ["pygame", "math", "sys", "random"], "include_files" : ['assets/', 'libraries/']}
        },
    executables = executables
)



"""


pg.init()
FramePerSec = pg.time.Clock()


displaysurface = pg.display.set_mode((WIDTH, HEIGHT))
icon = pg.image.load('assets/icon.png')
pg.display.set_icon(icon)
pg.display.set_caption("the legend of escudeiro!")

jooj = game.Game("teste","hahah", 1)

jogo = [game.Game("teste", "hahaha", 1),game.Game("teste", "hahaha", 2),game.Game("teste", "hahaha", 4), game.Game("teste", "hahaha", 8)]







gameover = False





"""
pg.joystick.init()

joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]
if joysticks:
    controller = joysticks[0]


def update_joystick():
    if pg.joystick.get_count() == None:
        joysticks = [pg.joystick.Joystick(x) for x in range(pg.joystick.get_count())]
        if joysticks:
            controller = joysticks[0]
        return
    if not controller.get_init():
        controller.init()
    
"""
def draw():
    pass

init = 1



while(True):
    titlescreen = ts.TitleScreen()
    jogo = [game.Game("teste", "hahaha", 1),game.Game("teste", "hahaha", 2),game.Game("teste", "hahaha", 4), game.Game("teste", "hahaha", 8)]

    while(not titlescreen.play):
        titlescreen.update()
        displaysurface.blit(titlescreen.surf,(0,0))
        pg.display.update()

    for jooj in jogo:

        #cs.cutscene(init)
        while(True):
            #update_joystick()
            #print(controller.get_button(0))
            displaysurface.fill((0,0,0))
            jooj.update()
            displaysurface.blit(jooj.surf,(0,0))
            pg.display.update()
            FramePerSec.tick(FPS)
            if jooj.exit:
                gameover = jooj.gameover
                if gameover:

                    break
                #jooj.song.stop()
                break
        if gameover: break

if __name__ == "__main__":
    print("hello world")


    pass