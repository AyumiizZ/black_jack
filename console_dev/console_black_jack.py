import random
card = [True]*52
def card_info(card_value):
    card_sym = ['Club','Diamonds','Hearts','Spades']
    card_type = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    return (card_value//13)+1, card_sym[card_value%4]+' '+card_type[(card_value//13)+1]
# 0 = Ace-club 1 = Ace-diamonds ... 50 King-hearts 51 King-spades
command = input()
player = []
# dealer = []
# draw card
while command != 'Stand':
    card_value = random.randint(0,51)
    while not card[card_value]:
        card_value = random.randint(0,51)
    player.append(card_value)
    card_value,info = card_info(card_value)
    