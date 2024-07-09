from planet import Planet
import pygame as pg
from constants import GRAVITY_CONST

bodies = []

def addPlanet(planet : Planet) :
    bodies.append(planet)

def getAccelerationFor(givenPlanet : Planet) -> pg.Vector2 :
    accel = pg.Vector2()
    position = givenPlanet.getPosition()

    for planet in bodies :
        if planet != givenPlanet :
            accel += planet.getUnproportionalizedFieldAt(position.x, position.y)

    return accel * GRAVITY_CONST