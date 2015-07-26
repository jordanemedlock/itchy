

class Itchy(object):
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.image = pygame.image.init('itchy.png')
    def get_image(self):
        return self.image

    
    def move(self,steps):
        pass
    def turnRight(self,degrees):
        pass
    def turnLeft(self,degrees):
        pass
    def pointInDirection(self,degrees):
        pass
    def pointTowards(self,pos):
        pass
    def goto(self,pos):
        pass
    def glide(self,sec,pos):
        pass
    def changeXBy(self,newX):
        pass
    def changeYBy(self,newY):
        pass
    def setXTo(self,newX):
        pass
    def setYTo(self,newY):
        pass
    def ifOnEdgeBounce(self):
        pass
