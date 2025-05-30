from const import *
from random import *
import pickle
class MapManager():
    def __init__(self, model, texture, scale = 0.1, color = RED_05):
        self.model = model
        self.texture_image = texture
        self.scale = scale
        self.color = color
    def add_block(self, pos):
        # print(pos)
        self.block = loader.loadModel(self.model)
        self.texture = loader.loadTexture(self.texture_image)
        self.block.setTexture(self.texture)
        self.block.reparentTo(self.land)
        self.block.setScale(self.scale)
        self.block.setColor(self.color)
        self.block.setPos(pos)
        self.block.setTag('at', str(pos))
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
            return x, y
    def isEmpty(self, pos):
        blocks =self.find_blocks(pos)
        if blocks:
            return False
        else:
            return True
    def findblocks(self, pos):
        return self.land.findAllMatches('=at' + str(pos))
    def find_highest_empty(self, pos):
        x, y, z = pos
        z = 1
        while not self.isEmpty((x, y, z)):
            z += 1
        return (x, y, z)
    def del_block(self, pos):
        block = self.findblocks(pos)
        print(pos)
        for block in block:
            block.removeNode()
    def del_block_from(self, pos):
        x, y, z = self.find_highest_empty(pos)
        pos = x, y, z
        print(pos)
        blocks = self.findblocks(pos)
        for block in blocks:
            block.removeNode()
    def build_block(self, pos):
        x, y, z = pos
        print(pos)
        new = self.find_highest_empty(pos)
        if new[2] <= z + 1:
            self.add_block(new)
    def save_map(self):
        blocks = self.land.getChildren()
        with open('my_map.dat', 'wb') as file:
            pickle.dump(len(blocks), file)
            for block in blocks:
                x, y, z = block.getPos()
                pos = x, y, z
                pickle.dump(pos, file)
    def load_map(self):
        self.clear()
        with open('my_map.dat', 'rb') as file:
            length = pickle.load(file)
            for i in range(length):
                pos = pickle.load(file)
                self.add_block(pos)
