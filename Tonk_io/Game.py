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
 
# Creates the necessary classes       
kbd = Keyboard()
mouse = Mouse()
tonk = Tonk(Vector(WIDTH/2, HEIGHT/2))
inter = Interaction(tonk, kbd, mouse)

# Draw handler
def draw(canvas):
    if(inter.lives != 0):
        inter.playerHit()
        inter.updateCollisions()
        inter.updateEnemies(canvas)
        inter.updateRockets(canvas)
        inter.updateTonk(canvas)
        canvas.draw_text("Lives: " + str(inter.lives), (10, 25), 25, 'Black', 'monospace')
        canvas.draw_text("Score: " + str(inter.score), (150, 25), 25, 'Black', 'monospace')
    else:
        timer.stop()
        frame.stop()

# SimpleGUI stuff
frame = simplegui.create_frame('Tonk.io', WIDTH, HEIGHT, 0)
timer = simplegui.create_timer(2000, inter.timer_handler)
frame.set_canvas_background('White')
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.set_mouseclick_handler(mouse.mouse_handler)
timer.start()
frame.start()
