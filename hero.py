class Hero():

    def __init__(self,pos,manager):
        self.hero = loader.loadModel("smiley")
        self.manager = manager

        self.hero.setPos(pos)
        self.hero.setScale(0.3)
        self.hero.setColor(1,0,0)

        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()

    def build(self):
        #опредить координаты где ставить
        old = self.hero.getPos()
        dx,dy = self.check_angle()
        block_pos = old[0] + dx, old[1] + dy, old[2]
        #ставить блок
        self.manager.addBlock(block_pos)

    def cameraBind(self):
        base.disableMouse()
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0,0,2)
        base.camLens.setFov(90)

    def accept_events(self):
        base.accept("a",self.turn_left)
        base.accept("d",self.turn_right)
        base.accept("a-repeat",self.turn_left)
        base.accept("d-repeat",self.turn_right)
        base.accept("w",self.move)
        base.accept("s",self.move_back)

        base.accept("mouse1",self.build)
        
        base.accept("i",self.manager.save_map)
        base.accept("m",self.manager.load_pickle_map)

        base.accept("1",self.manager.set_brick)
        base.accept("2",self.manager.set_stone)

    #check_angle
    #https://pastebin.com/ZGwxXrU8
    def forward_is_empty(self,new):
        return not self.manager.check_position(new)

    def forward_up_is_empty(self):
        old = self.hero.getPos()
        dx,dy = self.check_angle()
        new = old[0] + dx, old[1] + dy, old[2] + 1
        return not self.manager.check_position(new)  

    def bottom_is_empty(self):
        old = self.hero.getPos()
        new = old[0], old[1], old[2] - 1
        return not self.manager.check_position(new) 

    def gravity(self):
        while self.bottom_is_empty():
            old = self.hero.getPos()
            new = old[0], old[1], old[2] - 1
            self.hero.setPos(new)

    def move(self):
        self.gravity()
        
        old = self.hero.getPos()
        dx,dy = self.check_angle()
        new = old[0] + dx, old[1] + dy, old[2]

        if self.forward_is_empty(new):
            self.hero.setPos(new)
        else:
            if self.forward_up_is_empty():
                new = old[0] + dx, old[1] + dy, old[2] + 1
                self.hero.setPos(new)  

    def turn_left(self):
        oldH =  self.hero.getH()
        newH = oldH + 5
        self.hero.setH(newH%360)

    def turn_right(self):
        self.hero.setH((self.hero.getH()-5)%360)

    def move_back(self):
        old = self.hero.getPos()
        dx,dy = self.check_angle()
        new = old[0] - dx, old[1] - dy, old[2]
        self.hero.setPos(new)

    def check_angle(self):
        angle = self.hero.getH()
        if 0 <= angle <= 20:
            return 0,1
        if 20 <= angle <= 65:
            return -1,1
        if 65 <= angle <= 110:
            return -1,0
        if 110 <= angle <= 155:
            return -1,-1
        if 155 <= angle <= 200:
            return 0,-1
        if 200 <= angle <= 245:
            return 1,-1
        if 245 <= angle <= 290:
            return 1,0
        if 290 <= angle <= 355:
            return 1,1
        


    