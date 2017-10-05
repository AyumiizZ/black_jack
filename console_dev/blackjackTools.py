import random
class deck():
    def __init__(self):
        self.card = [True]*52
    def draw_card(self):
        card_value = random.randint(0,52)
        while not self.card[card_value]:
            card_value = random.randint(0,52)
        
class player():
    def __init__(self):
        self.card = []
    