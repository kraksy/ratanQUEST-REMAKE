import arcade

from settings import *

class ratan(arcade.Window):

    def __init__(self):
        super().__init__(screen_height, screen_width, title)
    
        arcade.set_background_color(arcade.csscolor.BLANCHED_ALMOND)

    def setup(self):

        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        wall = arcade.Sprite("base.png", tile_scale)

        for x in range(0, 256, 64):
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)
        
        pass

    def on_draw(self):

        self.clear()

def main():
    window = ratan()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()