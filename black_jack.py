import random
import arcade
import tools
class gameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color((119, 221, 119))
        self.card_sprite = [arcade.Sprite('images/card/'+str(i)+'.png') for i in range(52)]
        self.back_card_sprite = arcade.Sprite('images/card/back.png')
        self.text1 = arcade.create_text("Score: ", arcade.color.BLACK, 12)
        self.text2 = arcade.create_text("Score: ", arcade.color.BLACK, 12)
        self.world = tools.World(width,height)
        
    def player_show_card(self):
        c = 100
        # print(self.human.card)
        for i in self.world.human.card:
            self.card_sprite[i].set_position(c, 125)
            self.card_sprite[i].draw()
            c+=50
    def bot_show_card(self):
        c = 50
        # print(self.bot.card)
        for i in self.world.bot.card:
            c+=50
            if self.world.bot.card.index(i) == 0 and not self.world.reveal:
                self.back_card_sprite.set_position(c, 450)
                self.back_card_sprite.draw()
                continue
            self.card_sprite[i].set_position(c, 450)
            self.card_sprite[i].draw()
    def update_score(self):
        self.text1 = arcade.create_text("Score: " + str(self.world.human.score), arcade.color.BLACK, 12)
        self.text2 = arcade.create_text("Score: " + str(self.world.bot.score), arcade.color.BLACK, 12)
        arcade.render_text(self.text1, 50, 550)
        arcade.render_text(self.text2, 50, 225)
    def on_draw(self):
        arcade.start_render()
        self.player_show_card()
        self.bot_show_card()
        self.update_score()
        
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
if __name__ == '__main__':
    window = gameWindow(600,600)
    arcade.run()