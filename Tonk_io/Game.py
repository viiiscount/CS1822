try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import math
from Physics_Files.Vector import Vector
from Physics_Files.Tonk import Tonk
from Input_Files.Keyboard import Keyboard
from Input_Files.Mouse import Mouse
from Interaction import Interaction


# Constants are written in capital letters
WIDTH = 1280
HEIGHT = 720
        
kbd = Keyboard()
mouse = Mouse()
tonk = Tonk(Vector(WIDTH/2, HEIGHT/2))
inter = Interaction(tonk, kbd, mouse)

def draw(canvas):
    inter.updateRockets(canvas)
    inter.updateTonk()
    tonk.update()
    tonk.draw(canvas)

frame = simplegui.create_frame('Tonk.io', WIDTH, HEIGHT, 0)
frame.set_canvas_background('White')
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.set_mousedrag_handler(mouse.mouse_handler)
frame.start()
