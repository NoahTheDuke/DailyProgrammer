import random
import collections as co
import itertools as it

Player = co.namedtuple('Player', ['name', 'hand'])

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
deck = [(x,y) for x in values for y in suits]

random.shuffle(deck)

deal = lambda x: [deck.pop() for _ in range(x)]

num_players = int(input("How many players (2-8): "))

players = []
players.append(Player("Human", deal(2)))
for i in range(num_players - 1):
    players.append(Player("CPU {}".format(i + 1), deal(2)))
flop, turn, river = deal(3), deal(1), deal(1)
board = flop + turn + river

# Poker hands:
# High card, one pair, two pair,
# three of a kind, straight, flush,
# full house, four of a kind, straight flush
def generate_hand(player_hand):
    test = player_hand.hand + board
    #straight flush
    return it.permutations(test, 5)

for player in players:
    print("{}: {}, {}".format(player.name, *player.hand))

print("Flop: {}, {}, {}".format(*flop))
print("Turn: {}".format(*turn))
print("River: {}".format(*river))

#def best_hand(blah blah):
#   return "blah"

#print("Winner: {}, with a {}.".format(winner, best_hand))
