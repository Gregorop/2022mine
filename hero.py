class Hero():

    def __init__(self,pos):
        #self.land = land
        self.hero = loader.loadModel("smiley")

        self.hero.setPos(pos)
        self.hero.setScale(0.3)
        self.hero.setColor(1,0,0)

        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        base.disableMouse()
        base.camera.reparentTo(self.hero)
        #base.camera.setPos(pos)
        base.camera.setPos(0,0,1.5)
        base.camLens.setFov(90)

    def accept_events(self):
        base.accept("a",self.turn_left)
        base.accept("a"+"-repeat",self.turn_left)
        base.accept("d",self.turn_right)
        base.accept("d"+"-repeat",self.turn_right)
        base.accept("w",self.move)
        base.accept("s",self.move_back)
        base.accept("w-repeat",self.move)
        base.accept("s-repeat",self.move_back)
        
    def turn_left(self):
        self.hero.setH((self.hero.getH()+5)%360)
        print(self.hero.getH())

    def turn_right(self):
        self.hero.setH((self.hero.getH()-5)%360)
        print(self.hero.getH())

    def move(self):
        old_pos = self.hero.getPos()
        step_x,step_y = self.check_angle() 
        #step_x *= 0.5
        #step_y *= 0.5
        new_pos = old_pos[0] + step_x, old_pos[1] + step_y, old_pos[2]
        self.hero.setPos(new_pos)

    def move_back(self):
        old_pos = self.hero.getPos()
        step_x,step_y = self.check_angle()
        new_pos = old_pos[0] - step_x, old_pos[1] - step_y, old_pos[2]
        self.hero.setPos(new_pos)

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
        if angle >= 355:
            return 0,1


    