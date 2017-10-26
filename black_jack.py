import random
import arcade
from tools import World
class gameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color((119, 221, 119))
        self.card_sprite = [arcade.Sprite('images/card/'+str(i)+'.png') for i in range(52)]
        self.back_card_sprite = arcade.Sprite('images/card/back.png')
        self.world = World(width,height,True)
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
            arcade.render_text(self.busted, 255, 290)
            arcade.render_text(self.bot_win, 240, 260)
        elif self.world.bot.busted:
            arcade.render_text(self.busted, 255, 290)
            arcade.render_text(self.human_win, 250, 260)
        elif self.world.human.end and self.world.bot.end:
            if self.world.human.score > self.world.bot.score:
                arcade.render_text(self.human_win, 250, 280)
            elif self.world.human.score < self.world.bot.score:
                arcade.render_text(self.bot_win, 240, 280)
            else:
                arcade.render_text(arcade.create_text("Tie!!!",arcade.color.BLACK,12),250,250)
        if self.world.human.busted or self.world.bot.busted or self.world.bot.end:
            arcade.render_text(arcade.create_text("Press <F1> to start new game :3",arcade.color.BLACK,12),170,230)

    def on_draw(self):
        arcade.start_render()
        # arcade.render_text(arcade.create_text('Your money: {}'.format(self.world.money),arcade.color.BLACK,12),0,0)
        if self.world.first_game:
            self.first()
        else:
            self.player_show_card()
            self.bot_show_card()
            self.update_score()
            self.winner()
            self.world.bot_draw()
        
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
    
    def first(self):
        arcade.render_text(arcade.create_text(
'''
                            HOW TO PLAY
Reach a final score higher than the dealer without exceeding 21
                                or
 Let the dealer draw addition card until their hand exceeds 21 
    (The dealer must have a final score higher than 17)

                             CONTROL
        Press <SPACE> To Hit
        Press <ENTER> To Stand
        Press <F1> To start new game (when game end)

        CONTINUE TO GAME BY PRESS <ENTER>
''',arcade.color.BLACK,12),50,400)

if __name__ == '__main__':
    window = gameWindow(600,600)
    arcade.run()
