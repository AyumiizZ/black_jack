import random
import arcade
import tools
class gameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        # arcade.set_background_color(arcade.color.BLACK)
        arcade.set_background_color((119, 221, 119))
        self.card_sprite = [arcade.Sprite('images/card/'+str(i)+'.png') for i in range(52)]
        self.deck = tools.Deck()
        self.world = tools.World(width,height)
        self.human = tools.Player(self.deck)
        # self.bot = tools.Player()
        self.human.draw_card()
    def show_card(self):
        for i in self.human.card:
            self.card_sprite[i].set_position(100, 100)
            self.card_sprite[i].draw()
    def on_draw(self):
        arcade.start_render()
        self.show_card()
if __name__ == '__main__':
    window = gameWindow(600,600)
    arcade.run()