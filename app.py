import pyglet

from game import Game 


if __name__ == "__main__":
    game = Game()
    game.setup()

    
    pyglet.app.run() 