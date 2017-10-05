import random
import arcade
# from blackjackTools import deck
class gameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        # arcade.set_background_color(arcade.color.BLACK)
        arcade.set_background_color((119, 221, 119))
        # self.world = World(width,height)
    def on_draw(self):
        arcade.start_render()
if __name__ == '__main__':
    window = gameWindow(600,600)
    arcade.run()