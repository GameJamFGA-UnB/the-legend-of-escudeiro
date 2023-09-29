from libraries.default_values import *


FramePerSec = pg.time.Clock()




def halt(tempo):
    FramePerSec.tick(FPS/tempo)




def cutscene(n):
    if n == 1:
        halt(60)
        pass
    if n == 2:
        pass
    if n == 3:
        pass
    if n == 4:
        pass
    pass