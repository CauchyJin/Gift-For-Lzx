class heart:
    def __init__(self,heartImg,X,Y):
        self.img = heartImg
        self.xpos = X
        self.ypos = Y
        self.angle = random(0,TWO_PI)
        self.yoffset = 0.01
        
    def update(self):
        self.angle += 0.05
        self.yoffset = sin(self.angle) * 10
        
    def display(self):
        image(self.img, self.xpos, self.ypos + self.yoffset,30,30)
