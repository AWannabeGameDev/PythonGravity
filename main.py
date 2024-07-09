import pygame as pg
from constants import *
from sys import exit
from planet import Planet
import spriteHandler
from random import randint
from math import sqrt, pow

clock = pg.time.Clock()

#Planet(1000000, 100, -1000, 0, 0, -200, False)
#Planet(1000, 30, 0, 0, 300, 300, False)
#Planet(1000, 30, 2000, 0, 0, -500, False)
Planet(10000000000, 500, 0, 0, 0, 0, True)
Planet(1000000, 100, 10000, 0, 0, sqrt(GRAVITY_CONST * 10000000000 / 10000), False)
for i in range(1, 9) :
    Planet(10, 25, 300 * i * pow(-1, i), 0, 0, sqrt(GRAVITY_CONST * 1000000 / (300 * i)), False)

while True :
    for event in pg.event.get(pg.QUIT) :
        pg.quit()
        exit()

    deltaTime = clock.tick(60) / 500

    spriteHandler.update(deltaTime)
    spriteHandler.render()