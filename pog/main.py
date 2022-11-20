import arcade

from settings import *

class ratan(arcade.Window):

    def __init__(self):
        super().__init__(screen_height, screen_width, title)
    
        arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)

    def setup(self):

        pass

    def on_draw(self):

        self.clear()

def main():
    window = ratan()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()