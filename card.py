import random

suits = [ 'Hearts','Clubs','Spades', 'Diamonds' ]
ranks = ['2','3','4','5','6','7','8','9','10','Jack','King','Queen','Ace']

deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
random.shuffle(deck)

hand = [deck.pop() for _ in range(5)]
print("Your have 5 Cards in hand:")

for card in hand:
    print(card)
