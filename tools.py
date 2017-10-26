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
    def __init__(self, width, height, first_game):
        self.width = width
        self.height = height
        self.first_game = first_game
        self.deck = Deck()
        self.human = Player(self.deck)
        self.bot = Player(self.deck)
        self.human.draw_card()
        self.bot.draw_card()
        self.human.draw_card() 
        self.bot.draw_card()
        self.bot_thinking = False
        # self.money = money
        # self.bet = 0
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE and not self.human.end and not self.human.busted and not self.first_game:
            self.human.draw_card()
        if key == arcade.key.ENTER and not self.first_game:
            self.human.end = True
        if key == arcade.key.ENTER and self.first_game:
            sleep(0.25)
            self.first_game = False
        if key == arcade.key.F1 and (self.bot.end or self.human.busted or self.bot.busted):
            self.__init__(self.width,self.height,False)
        # if key == arcade.key.NUM_1:
        #     self.bet += 10
        #     self.money -= 10
        # if key == arcade.key.NUM_2:
        #     self.bet += 50
        #     self.money -= 50
        # if key == arcade.key.NUM_3:
        #     self.bet += 100
        #     self.money -= 100
        # if key == arcade.key.NUM_4:
        #     self.bet += 500
        #     self.money -= 500
        
    def bot_draw(self):
        if self.human.end and not self.bot.end and not self.human.busted:
            sleep(1)
            if self.bot.score == self.human.score and self.bot.score >= 19:
                # sleep(1)
                # print(1)
                self.bot.end = True
            elif self.bot.score > 17 and self.bot.score > self.human.score:
                # sleep(1)
                # print(2)
                self.bot.end = True
            else:
                # sleep(1)
                self.bot.draw_card()
                # print('draw')