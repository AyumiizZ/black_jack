import random
class Deck():
    def __init__(self):
        self.card = [True]*52
class Player():
    def __init__(self, deck):
        self.card = []
        self.deck = deck
    def draw_card(self):
        card_value = random.randint(0,51)
        while not self.deck.card[card_value]:
            card_value = random.randint(0,51)
        self.card.append(card_value)
        self.deck.card[card_value] = False
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height