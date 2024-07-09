import pygame as pg
from constants import *
from math import exp

position = ZERO_VECTOR.copy()
scale = 1
scaleInput = 0

isDragging = False

def update() :
    global isDragging, position, scale, scaleInput

    for event in pg.event.get((pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP, pg.MOUSEMOTION, pg.KEYDOWN, pg.MOUSEWHEEL)) :
        if event.type == pg.MOUSEBUTTONDOWN :
            isDragging = True
            pg.mouse.get_rel()

        elif event.type == pg.MOUSEBUTTONUP :
            isDragging = False

        elif event.type == pg.MOUSEMOTION and isDragging :
            drag = pg.mouse.get_rel()
            position -= pg.Vector2(drag[0], drag[1]) / scale

        if event.type == pg.MOUSEWHEEL :
            if event.y == 1 :
                scaleInput += 0.1
            else :
                scaleInput -= 0.1

            if scaleInput >= 0 :
                scale = scaleInput + 1
            else :
                scale = exp(scaleInput)
                scale = scale if scale > 0.001 else 0.001

def render(sprites : list, screen : pg.Surface) :
    for sprite in sprites :
        sprite.render(screen, position, scale)