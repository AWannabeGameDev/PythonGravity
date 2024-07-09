from sprite import Sprite
import pygame as pg
from math import hypot

class Planet(Sprite) :
    mass = None
    velocity = pg.Vector2()
    acceleration = pg.Vector2()
    stationary = None

    def __init__(self, mass : float, radius : float, posX : float, posY : float, velX, velY, stationary : bool) :
        surf = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA)
        pg.draw.circle(surf, (255, 255, 255), (radius, radius), radius)
        rect = surf.get_rect(center = (posX, posY))
        super().__init__(surf, rect)

        self.mass = mass
        self.velocity = pg.Vector2(velX, velY)
        self.stationary = stationary
        gravityField.addPlanet(self)

    def update(self, deltaTime : float) :
        if not self.stationary :
            self.acceleration = gravityField.getAccelerationFor(self)
            self.velocity += self.acceleration * deltaTime
            self.rect.centerx += self.velocity.x * deltaTime
            self.rect.centery += self.velocity.y * deltaTime

    def getUnproportionalizedFieldAt(self, posX : float, posY : float) -> pg.Vector2 :
        xDist = self.rect.centerx - posX
        yDist = self.rect.centery - posY
        dist = hypot(xDist, yDist)

        fieldX = self.mass * xDist / (dist * dist * dist)
        fieldY = self.mass * yDist / (dist * dist * dist)

        return pg.Vector2(fieldX, fieldY)
    
    def getPosition(self) -> pg.Vector2 :
        return pg.Vector2(self.rect.centerx, self.rect.centery)
    
import gravityField