from random import random


class Mapmanager():
    def __init__(self):
        self.model = 'block.egg' # модель кубика в файле block.egg
        self.texture = 'block.png'# текстура кубика           
        self.color = (0,1,0,1)
        self.startNew()
 
    def startNew(self):       
	    self.land = render.attachNewNode("Land")

    def clear(self):
        self.land.removeNode()
        self.startnew()
        
    def addBlock(self, position):
        block = loader.loadModel(self.model)
        texture = loader.loadTexture(self.texture)
        block.setTexture(texture)
        if position[2] < 2:
            block.setColor((0.1,0.1,0.1,0))
        elif position[2] < 5:
            block.setColor((1,0,0,0))
        # block.setColor(self.color)
        block.setPos(position)
        block.reparentTo(self.land)

    def load_map(self):
        with open("map.txt", "r") as file:
            data = file.readlines()
        
        x = 0

        for str in data:
            y = 0
            temp = str.split(" ")[:-1]
            for max_z in temp:
                for z in range(int(max_z)+1):
                    self.addBlock((x,y,int(z)))
                y += 1

            x += 1 

    def rand_map(self):
        for x in range(20):
            for y in range(20):
                for z in range(5):
                    if random() > (z*0.3):
                        self.addBlock((x,y,z))
