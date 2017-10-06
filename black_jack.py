import random
import arcade
import tools
class gameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        # arcade.set_background_color(arcade.color.BLACK)
        arcade.set_background_color((119, 221, 119))
        self.card_sprite = [arcade.Sprite('images/card/'+str(i)+'.png') for i in range(52)]
        self.back_card_sprite = arcade.Sprite('images/card/back.png')
        self.deck = tools.Deck()
        self.world = tools.World(width,height)
        self.human = tools.Player(self.deck)
        self.bot = tools.Player(self.deck)
        self.reveal = False
        self.human.draw_card()
        self.bot.draw_card()
        self.human.draw_card()
        self.bot.draw_card()
    def player_show_card(self):
        c = 0
        # print(self.human.card)
        for i in self.human.card:
            self.card_sprite[i].set_position(100+c, 125)
            self.card_sprite[i].draw()
            c+=50
    def bot_show_card(self):
        c = 0
        # print(self.bot.card)
        for i in self.bot.card:
            c+=50
            if self.bot.card.index(i) == 0 and not self.reveal:
                self.back_card_sprite.set_position(75+c, 525)
                self.back_card_sprite.draw()
                continue
            self.card_sprite[i].set_position(75+c, 525)
            self.card_sprite[i].draw()
    def on_draw(self):
        arcade.start_render()
        self.player_show_card()
        self.bot_show_card()
    def on_key_press(self, key, key_modifiers, player):
        self.world.on_key_press(key, key_modifiers, self.human)
if __name__ == '__main__':
    window = gameWindow(600,600)
    arcade.run()