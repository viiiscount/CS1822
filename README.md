CS1822 Game Project
- Tonk.py - The main file that you should run to play the game. Creates the simpleGUI frame, timers, draw handler, etc.
- Game.py - Has the main game loop, as well as all of the main game functions.
- Keyboard.py - Handles keydown and keyup events (keyboard inputs).
- Mouse.py - Handles mouse clicks, and returns the current mouse position.
- Ammo.py - Ammo class, has functions for the Ammo objects such as draw() and hit(). Also contains getters for the position and radius.
- Enemy.py - Enemy class, has functions for the Enemy objects such as draw(). Has an update() method that updates its velocity. Also contains getters for the position, velocity and radius.
- Interaction.py - Contains the functions that handle collisions between the rockets, enemies, ammo, and player.
- Player.py - Player class, has functions for the Player object such as draw(). Has an update() method that updates its velocity and prevents the player from leaving the arena. Also contains getters for the position, velocity and radius.
- Rocket.py - Rocket class, has functions for the Rocket objects such as draw(). Has an update() method that updates its velocity. Also contains getters for the position, velocity and radius.
- Spritesheet.py -  Handles drawing the explosion when an enemy is killed using a spritesheet.
- Vector.py - The vector class developed in lectures. Vectors are used for all the positions and velocities of all objects.
- __init__ files are for allowing the main file Tonk.py to import from other files
