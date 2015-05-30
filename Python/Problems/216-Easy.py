import random

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
deck = ['{} of {}'.format(*card) for card in ((x,y) for x in values for y in suits)]

random.shuffle(deck)

deal = lambda x: [deck.pop() for _ in range(x)]
burn = deck.pop

num_players = int(input("How many players (2-8): "))

myhand = deal(2)
print("Your hand: {}, {}".format(*myhand))
for i in range(num_players - 1):
    hand = deal(2)
    print("CPU {} hand: {}, {}".format(i + 1, *hand))

_, flop, _, turn, _, river = burn(), deal(3), burn(), deal(1), burn, deal(1)
print("Flop: {}, {}, {}".format(*flop))
print("Turn: {}".format(*turn))
print("River: {}".format(*river))
