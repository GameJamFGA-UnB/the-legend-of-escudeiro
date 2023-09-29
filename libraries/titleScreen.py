from typing import Any
from libraries.default_values import *
"""






"""
image = pg.transform.scale(pg.image.load('assets/castelo.png'), (WIDTH,HEIGHT))




class TitleScreen(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.icon = image
        self.play = False
        self.surf = pg.Surface((WIDTH,HEIGHT))
        self.surf.set_colorkey(mask)
        self.surf.fill(mask)
        self.surf.blit(self.icon, vec(0,0))
        self.rect = vec(0,0)
    pass

    def update(self):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key in [K_KP_ENTER, K_RETURN]:
                    self.play = True

