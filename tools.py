import random
import arcade.key
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
    def draw_card(self):
        card_value = random.randint(0,51)
        while not self.deck.card[card_value]:
            card_value = random.randint(0,51)
        self.card.append(card_value)
        self.deck.card[card_value] = False
        self.add_score(card_value)
        if self.score > 21:
            self.busted = True
        
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
        self.reveal = False
        self.human.draw_card()
        self.bot.draw_card()
        self.human.draw_card() 
        self.bot.draw_card()
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE and not self.reveal and not self.human.busted:
            self.human.draw_card()
        if key == arcade.key.ENTER:
            self.reveal = True