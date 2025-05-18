from const import *
from random import *
class MapManager():
    def __init__(self, model, texture, scale = 0.1, color = RED_05):
        self.model = model
        self.texture_image = texture
        self.scale = scale
        self.color = color
    def add_block(self, pos):
        self.block = loader.loadModel(self.model)
        self.texture = loader.loadTexture(self.texture_image)
        self.block.setTexture(self.texture)
        self.block.reparentTo(self.land)
        self.block.setScale(self.scale)
        self.block.setColor(self.color)
        self.block.setPos(pos)
    def start_new(self):
        self.land = render.attachNewNode('Land')
    def set_color(self, color):
        self.color = color
    def clear(self):
        self.land.removeNode()
        self.start_new()
    def load_land(self , filename):
        self.clear()
        with open(filename, 'r') as file:
            y = 0
            for line in file.readlines():
                x = 0
                for symbol in line.split(' '):
                    for z in range(int(symbol)+1):
                        r = random()
                        g = random()
                        b = random()
                        a = random()
                        self.set_color((r,g,b,a))
                        self.add_block((x, y, z * self.scale))
                    x += self.scale
                y += self.scale