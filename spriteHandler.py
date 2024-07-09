from sprite import Sprite
import pygame as pg
from constants import *
import camera

sprites = []

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption(SCREEN_TITLE)

def addSprite(sprite : Sprite) :
    sprites.append(sprite)

def update(deltaTime : float) :
    for sprite in sprites :
        sprite.update(deltaTime)

def render() :
    screen.fill((0, 0, 0))
    camera.update()
    camera.render(sprites, screen)
    pg.display.update()