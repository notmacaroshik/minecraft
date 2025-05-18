from direct.showbase.ShowBase import ShowBase
from map_manager import MapManager
from hero import Hero


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        manager = MapManager('models/block.egg','images/block.png')
        # manager = MapManager('models/Sailboat.egg','tekstures/SailTexture.tif')r
        manager.start_new()
        manager.load_land('files/land.txt')
        manager.load_land('files/land2.txt')
        hero = Hero((0, 0, 0.1), manager.land)
        # self.model = loader.loadModel('models/Sailboat.egg')
        # self.model1 = loader.loadModel('models/Boeing707.egg')
        # self.model1.reparentTo(render)
        # self.texture = loader.loadTexture('tekstures/SailTexture.tif')
        # self.model.setTexture(self.texture)
        # self.texture1 = loader.loadTexture('tekstures/BoeingTexture.tif')
        # self.model1.setTexture(self.texture)
        # self.model.reparentTo(render)
        # self.model.setScale(0.25)
        # self.model.setPos(-2, 25, -3)
        # self.model1.setScale(0.1)
        # self.model1.setPos(2, 10, 3)
        # self.pandaActor = Actor("models/panda-model",
        #                         {"walk": "models/panda-walk4"})
        # self.pandaActor.setScale(0.05, 0.05, 0.05)
        # self.pandaActor.setPos(0,0,1)
        # self.pandaActor.reparentTo(self.render)
        # # Loop its animation.
        # self.pandaActor.loop("walk")

        base.camLens.setFov(90)
game = Game()
game.run()