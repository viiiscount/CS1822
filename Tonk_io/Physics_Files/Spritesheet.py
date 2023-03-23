try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Constants are written in capital letters
IMG = simplegui.load_image("https://raw.githubusercontent.com/viiiscount/CS1822/main/Textures/pngegg.png")

class Spritesheet:
    
    def __init__(self, posX, posY):
        self.image = IMG
        self.rows = 4
        self.columns = 5
        self.x = self.image.get_width() / self.columns
        self.y = self.image.get_height() / self.rows
        self.centreX = self.x/2
        self.centreY = self.y/2
        self.num_frames = 0
        self.xPos = posX
        self.yPos = posY
        
    def draw(self, canvas):
        canvas.draw_image(self.image, (self.centreX, self.centreY), (self.x, self.y), (self.xPos, self.yPos), (50, 50))
        
    def next_frame(self):     
        if(self.centreX == (self.x * (self.columns - 0.5))):
            self.centreX = self.x/2
            self.centreY = self.centreY + self.y
            self.num_frames = self.num_frames + 1 
        else:
            self.centreX = self.centreX + self.x
            self.num_frames = self.num_frames + 1
    
    def done(self):
        doneYesNo = False
        if(self.num_frames == 20):
            doneYesNo = True
        return doneYesNo

class Clock:
    time = 0
    
    def tick(self):
        self.time = self.time + 1
    
    def transition(self, frame_duration):
        changeYesNo = False
        if (self.time % frame_duration == 0):
            changeYesNo = True
        return changeYesNo