import random
import arcade
import tools
from time import sleep
class gameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color((119, 221, 119))
        self.card_sprite = [arcade.Sprite('images/card/'+str(i)+'.png') for i in range(52)]
        self.back_card_sprite = arcade.Sprite('images/card/back.png')
        # self.text1 = arcade.create_text("Score: ", arcade.color.BLACK, 12)
        # self.text2 = arcade.create_text("Score: ", arcade.color.BLACK, 12)
        self.world = tools.World(width,height)
        self.busted_show = False
        
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
            if self.world.bot.card.index(i) == 0 and not self.world.human.end:
                self.back_card_sprite.set_position(c, 450)
                self.back_card_sprite.draw()
                continue
            self.card_sprite[i].set_position(c, 450)
            self.card_sprite[i].draw()
    def update_score(self):
        self.human_score_board = arcade.create_text("Score: " + str(self.world.human.score), arcade.color.BLACK, 12)
        self.bot_score_board = arcade.create_text("Score: " + str(self.world.bot.score), arcade.color.BLACK, 12)
        arcade.render_text(self.human_score_board, 50, 225)
        if self.world.human.end:
            arcade.render_text(self.bot_score_board, 50, 550)
    def winner(self):
        self.busted = arcade.create_text("Busted!!!",arcade.color.BLACK,12)
        self.human_win = arcade.create_text("You win!!!",arcade.color.BLACK,12)
        self.bot_win = arcade.create_text("Dealer win!!!",arcade.color.BLACK,12)
        if self.world.human.busted:
            arcade.render_text(self.busted, 250, 250)
            arcade.render_text(self.bot_win, 300, 300)
        elif self.world.bot.busted:
            arcade.render_text(self.busted, 250, 250)
            arcade.render_text(self.human_win, 300, 300)
        elif self.world.human.end and self.world.bot.end:
            if self.world.human.score > self.world.bot.score:
                arcade.render_text(self.human_win, 250, 250)
            elif self.world.human.score < self.world.bot.score:
                arcade.render_text(self.bot_win, 250, 250)
            else:
                arcade.render_text(arcade.create_text("Tie!!!",arcade.color.BLACK,12),250,250)

    def on_draw(self):
        arcade.start_render()
        self.player_show_card()
        self.bot_show_card()
        self.update_score()
        self.winner()
        self.world.bot_draw()
        # if self.world.bot_thinking:
        #     sleep(1)
        
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
if __name__ == '__main__':
    window = gameWindow(600,600)
    arcade.run()