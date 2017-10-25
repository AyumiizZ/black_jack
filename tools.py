import random
import arcade.key
from time import sleep
class Deck():
    def __init__(self):
        self.card = [True]*52
class Player():
    def __init__(self, deck):
        self.card = []
        self.deck = deck
        self.score = 0
        self.ACE = 0
        self.busted = False
        self.end = False
    def draw_card(self):
        card_value = random.randint(0,51)
        while not self.deck.card[card_value]:
            card_value = random.randint(0,51)
        self.card.append(card_value)
        self.deck.card[card_value] = False
        self.add_score(card_value)
        if self.score > 21:
            self.busted = True
            self.end = True
        
    def add_score(self, card_value):
        if card_value in [0,1,2,3]:
            self.ACE += 1
            self.score += 11
        elif card_value >= 40:
            self.score += 10
        else:
            self.score += card_value//4+1
        while self.ACE > 0 and self.score > 21:
            self.ACE -= 1
            self.score -= 10
        
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.deck = Deck()
        self.human = Player(self.deck)
        self.bot = Player(self.deck)
        # self.reveal = False
        self.human.draw_card()
        self.bot.draw_card()
        self.human.draw_card() 
        self.bot.draw_card()
        self.game_end = False
        self.bot_thinking = False
        self.bet = 1500
        self.this_bet = 0
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE and not self.human.end and not self.human.busted:
            self.human.draw_card()
        if key == arcade.key.ENTER:
            # self.reveal = True
            self.human.end = True
        # if key == arcade.key.NUM_1:
        #     self.this_bet += 10
        #     self.bet -= 10
        # if key == arcade.key.NUM_2:
        #     self.this_bet += 50
        #     self.bet -= 50
        # if key == arcade.key.NUM_3:
        #     self.this_bet += 100
        #     self.bet -= 100
        # if key == arcade.key.NUM_4:
        #     self.this_bet += 500
        #     self.bet -= 500
        
    def bot_draw(self):
        # print('---')
        # print(self.reveal)
        # print(self.game_end)
        if self.human.end and not self.bot.end and not self.human.busted:
            if self.bot.score == self.bot.score and self.bot.score >= 19:
                print(1)
                self.bot.end = True
            elif self.bot.score > 17 and self.bot.score > self.human.score:
                print(2)
                self.bot.end = True
            else:
                self.bot.draw_card()
                print('draw')
        # and not self.game_end and (self.bot.score <= self.human.score or self.bot.score < 17) and self.bot.score <= 21:
        #     self.bot_thinking = True
        #     self.bot.draw_card()
        # else:
        #     self.bot.end = True
        #     self.bot_thinking = False