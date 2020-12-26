class ibb:
    def __init__(self):
        self.o = 5
        self.width1 = 20
        self.height1 = 20
        self.x1 = width/8
        self.y1 = height/2
    
    def display(self):
        noStroke()
        frameRate(60)
        #body and head
        fill(244,77,130)
        rect(self.x1,self.y1,self.width1,self.height1) #body
        ellipse(self.x1,self.y1-self.height1/2,self.width1,self.width1) #head
        #eyes
        fill(0,50,75)
        rect(self.x1-self.width1/6,self.y1-2*self.height1/3,self.width1/8,self.width1/4)
        rect(self.x1+self.width1/6,self.y1-2*self.height1/3,self.width1/8,self.width1/4)
        #feet
        fill(244,77,130)
        rect(self.x1-self.width1/6,self.y1+3*self.height1/4,self.width1/5,self.height1/2)
        rect(self.x1+self.width1/6,self.y1+3*self.height1/4,self.width1/5,self.height1/2)
        arc(self.x1-4*self.width1/15,self.y1+self.height1,2*self.width1/5,2*self.width1/5,PI,2*PI)
        arc(self.x1+4*self.width1/15,self.y1+self.height1,2*self.width1/5,2*self.width1/5,PI,2*PI)
        
    def move(self):
        self.x1 += self.o
        if self.x1 >= 500:
            self.o = 0
