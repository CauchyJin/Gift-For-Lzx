class obb:
    def __init__(self):
        self.I = 5
        self.width2 = 20
        self.height2 = 10
        self.x2 = 7*width/8
        self.y2 = height/2
    
    def display(self):
        noStroke()
        frameRate(60)
        #body and head
        fill(26,219,79)
        rect(self.x2,self.y2+self.height2/2,self.width2,self.height2) #body
        ellipse(self.x2,self.y2,self.width2,self.width2) #head
        #eyes
        fill(0,50,75)
        rect(self.x2-self.width2/6,self.y2-self.height2/3,self.width2/8,self.width2/4)
        rect(self.x2+self.width2/6,self.y2-self.height2/3,self.width2/8,self.width2/4)
        #feet
        fill(26,219,79)
        rect(self.x2-self.width2/6,self.y2+6*self.height2/4,self.width2/5,self.height2)
        rect(self.x2+self.width2/6,self.y2+6*self.height2/4,self.width2/5,self.height2)
        arc(self.x2-4*self.width2/15,self.y2+2*self.height2,2*self.width2/5,2*self.width2/5,PI,2*PI)
        arc(self.x2+4*self.width2/15,self.y2+2*self.height2,2*self.width2/5,2*self.width2/5,PI,2*PI)
        
    def move(self):
        self.x2 -= self.I
        if self.x2 <= 520:
            self.I = 0
