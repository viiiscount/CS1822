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
 
# Creates the necessary classes       
kbd = Keyboard()
mouse = Mouse()
game = Game(kbd, mouse, WIDTH, HEIGHT)

# Draw handler
def draw(canvas):
    if(game.lives != 0):
        timer.start()
        game.gameLoop(canvas)
    else:
        timer.stop()
        canvas.draw_text("You Died :(", (640 - frame.get_canvas_textwidth("You Died :(", 40, 'monospace')/2, 320), 40, 'Black', 'monospace')
        canvas.draw_text("Press Space to restart", (640 - frame.get_canvas_textwidth("Press Space to restart", 25, 'monospace')/2, 400), 25, 'Black', 'monospace')
        canvas.draw_text("Press P to exit", (640 - frame.get_canvas_textwidth("Press P to exit", 25, 'monospace')/2, 450), 25, 'Black', 'monospace')
        if(kbd.fire):
            game.reset()
        elif(kbd.pause):
            frame.stop()

# SimpleGUI stuff
frame = simplegui.create_frame('Tonk.io', WIDTH, HEIGHT, 0)
timer = simplegui.create_timer(2000, game.timer_handler)
frame.set_canvas_background('White')
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.set_mouseclick_handler(mouse.mouse_handler)
frame.start()
