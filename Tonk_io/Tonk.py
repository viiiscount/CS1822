try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Input_Files.Keyboard import Keyboard
from Input_Files.Mouse import Mouse
from Game import Game

# Constants are written in capital letters
WIDTH = 1280
HEIGHT = 720
IMG = simplegui.load_image('https://raw.githubusercontent.com/viiiscount/CS1822/main/Textures/start.png')

 
# Creates the necessary classes       
kbd = Keyboard()
mouse = Mouse()
game = Game(kbd, mouse, WIDTH, HEIGHT)

# Draw handler
def draw(canvas): 
    if (game.lives == 0):
        canvas.draw_image(IMG, (128, 72), (256, 144), (WIDTH/2-20, HEIGHT/2), (1024, 576))
        if(mouse.getPos() != None):
            game.reset()
    else:
        timer.start()
        game.gameLoop(canvas)



# SimpleGUI stuff
frame = simplegui.create_frame('Tonk.io', WIDTH, HEIGHT, 0)
timer = simplegui.create_timer(2000, game.timer_handler)
frame.set_canvas_background('Silver')
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.set_mouseclick_handler(mouse.mouse_handler)
frame.start()
