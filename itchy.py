import pygame
from math import *
import time

space = pygame.K_SPACE
left = pygame.K_LEFT
right = pygame.K_RIGHT


def curry(func, arg):
    def curried(*args, **kwargs):
        return func(arg, *args, **kwargs)
    return curried

def missingSelf(func, *args, **kwargs):
    def curried(self):
        return func(self, *args, **kwargs)
    return curried

def queued(func):
    def _func(self, *args, **kwargs):
        self.queue.append(missingSelf(func, *args, **kwargs))
        return None
    return _func

def rot_center(image, angle):
    """rotate a Surface, maintaining position."""

    loc = image.get_rect().center
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite

def flip_center(image):
    """rotate a Surface, maintaining position."""

    loc = image.get_rect().center
    rot_sprite = pygame.transform.flip(image, True, False)
    rot_sprite.get_rect().center = loc
    return rot_sprite

class Itchy(object):
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.image = pygame.image.load('itchy.png')
        self.rect = self.image.get_rect()
        self.direction = 90
        self.facing = 'right'
        self.queue = []
        self.events = []
    def get_image(self):
        self.direction = (self.direction + 90) % 360 - 90
        if self.facing == 'left' and self.direction == -90:
            return flip_center(self.image)
        return rot_center(self.image, -(self.direction-90))
    def get_rect(self):
        return self.rect
    def run(itchy, events):
        self.events = events
        exec(open('run.py').read())


    @queued
    def wait(self, sec):
        time.sleep(sec)
    @queued
    def faceLeft(self):
        self.facing = 'left'
        self.direction = -90
    @queued
    def faceRight(self):
        self.facing = 'right'
        self.direction = 90
    @queued
    def move(self,steps):
        dX = steps*sin(radians(-(self.direction - 180)))
        dY = steps*cos(radians(-(self.direction - 180)))
        vec = [dX,dY]
        self.rect = self.rect.move(vec)
    @queued
    def turnRight(self,degrees):
        self.direction += degrees
    @queued
    def turnLeft(self,degrees):
        self.direciton += degrees
    @queued
    def pointInDirection(self,degrees):
        self.direction = degrees
    @queued
    def pointTowards(self,pos):
        mx, my = self.rect.center
        print mx, my
        print pos
        dx, dy = pos[0] - float(mx), pos[0] - float(my)
        self.direction = degrees(atan(dy/dx)) + 90
    @queued
    def goto(self,pos):
        self.rect.center = pos
    @queued
    def glide(self,sec,pos):
        pass
    @queued
    def changeXBy(self,dX):
        self.rect.center[0] += dX
    @queued
    def changeYBy(self,dY):
        self.rect.center[1] += dY
    @queued
    def setXTo(self,newX):
        self.rect.center[0] = newX
    @queued
    def setYTo(self,newY):
        self.rect.center[1] = newY
    @queued
    def ifOnEdgeBounce(self):
        pass

    def isPressed(self, key):
        for event in self.events:
            if hasattr(event, 'key') and event.key == key:
                return True
        return False

