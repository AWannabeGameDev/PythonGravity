import pygame as pg
from constants import *

class Sprite :
    surface = None
    rect = None
    drawSurf = None
    drawRect = None
    prevScaleOffset = None

    def __init__(self, surface : pg.Surface, rect : pg.Rect) :
        self.surface = surface.copy()
        self.rect = rect.copy()
        self.prevScaleOffset = 1
        self.drawRect = rect.copy()
        self.drawSurf = surface.copy()
        spriteHandler.addSprite(self)

    def render(self, surface : pg.Surface, positionOffset : pg.Vector2, scaleOffset : float) :
        self.drawRect.x = scaleOffset * (self.rect.x - positionOffset.x) + CENTER_OFFSET.x
        self.drawRect.y = scaleOffset * (self.rect.y - positionOffset.y) + CENTER_OFFSET.y

        if scaleOffset != self.prevScaleOffset :
            surfaceScale = scaleOffset if scaleOffset >= 0.1 else 0.1
            self.drawSurf = pg.transform.scale(self.surface, (self.surface.get_width() * surfaceScale, self.surface.get_height() * surfaceScale))

            self.prevScaleOffset = scaleOffset
        
        surface.blit(self.drawSurf, self.drawRect)

    def update(*args, **kwargs) :
        pass

import spriteHandler