add_library('sound')

from ibb_ import ibb
from obb_ import obb
from heart_ import heart

heartList = []
heartCount = 40

def setup():
    frameRate(60)
    size(1024,768)
    background(255)
    ellipseMode(CENTER)
    rectMode(CENTER)
    imageMode(CENTER)
    
    global t1,t2
    t1 = width/8
    t2 = 7*width/8
    
    img = loadImage("heart.png")
    for i in range(heartCount):
        x = random(0,width)
        y = map(i,0,heartCount,0,height)
        heartList.append(heart(img,x,y))
    
    #play bgm
    music = SoundFile(this,"Darling.mp3")
    music.play()
    
    global ibb,obb
    ibb = ibb()
    obb = obb()
        
def draw():
    background(255)
    
    #Load background
    imgBackground = loadImage("background.png")
    image(imgBackground,width/2,height/2,width,height)
    
    #Draw two blue squares
    fill(0,0,100)
    rect(30,30,25,25)
    rect(994,30,25,25)
    
    #display the heart when ibb meet with obb
    if t1 > 490 and t2 < 530:
        for h in heartList:
           h.update()
           h.display()
           IMG = loadImage("iloveyou.png")
           image(IMG,width/2,120,551,115)
        
    #HappyBirthday
    img = loadImage("happybirthday.jpeg")
    image(img,width/2,height/2,500,301)
    
    #How to operate
    fill(244,77,130)
    textSize(20)
    text("Press   ->   and   <-   until ibb meet with obb",300,600)
    fill(26,219,79)
    textSize(20)
    text("Once they get together,they will never leave each other",250,200)
    text("You also can try to put your cursor on the blue square",250,650)
    
    #display ibb and obb
    ibb.display()
    obb.display()
    
    #Operation area
    if mouseX > 0 and mouseX < 70 and mouseY > 0 and mouseY < 70:
        img2 = loadImage("you and me.jpeg")
        image(img2,width/2,height/2+30,400,400)
    if mouseX > 980 and mouseX < 1024 and mouseY > 0 and mouseY < 70:
        img3 = loadImage("Love Letter.jpeg") #I write it quite long ago
        image(img3,width/2,height/2,600,600)
    
def keyPressed():
    global t1,t2
    if key == CODED:
        if keyCode == RIGHT:
            ibb.move()
            t1 += 5
        elif keyCode == LEFT:
            obb.move()
            t2 -= 5
