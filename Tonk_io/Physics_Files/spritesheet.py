class Spritesheet:
    def __init__(self, imgurl, rows, columns, num_frames, pos_x, pos_y, duration):
        self.img = simplegui.load_image(imgurl)
        self.rows = rows
        self.columns = columns
        self.height = self.img.get_height()
        self.width = self.img.get_width()
        self.frame_height = self.height / rows
        self.frame_width = self.width / columns
        self.frame_centre_y = self.frame_height / 2
        self.frame_centre_x = self.frame_width / 2
        self.num_frames = num_frames
        self.frame_index = [0,0]
        
        self.x = pos_x
        self.y = pos_y
        self.duration = duration
        
    def next_frame(self):
        self.frame_index[0] = (self.frame_index[0] + 1) % self.columns
        if self.frame_index[0] == 0:
            self.frame_index[1] = (self.frame_index[1] + 1) % self.rows
        
    
    def done(self):
        self.num_frames -= 1 / self.randd
        if self.num_frames <= 0:
            return False
        return True
        
    def draw(self, canvas):
        for explosion in explosions:
            Clock.tick(self)
            if explosion.done() == True:
                if Clock.transition(self, explosion.duration) == True:
                    explosion.next_frame()
            source_centre = (
                explosion.frame_width * explosion.frame_index[0] + explosion.frame_centre_x,
                explosion.frame_height * explosion.frame_index[1] + explosion.frame_centre_y            
            )
        
            source_size = (explosion.frame_width, explosion.frame_height)
            dest_centre = (explosion.x, explosion.y)
            dest_size = (100, 100)
        
            canvas.draw_image(explosion.img, source_centre, source_size, dest_centre, dest_size)
