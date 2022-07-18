from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.mapManager = Mapmanager()
        # self.mapManager.create_floor()
        # self.mapanager.create_walls()
        #self.mapManager.rand_map()
        self.mapManager.load_pickle_map()
        gg = Hero((5,5,60),self.mapManager)

Game = Game()
Game.run()
