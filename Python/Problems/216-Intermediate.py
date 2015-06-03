import random

class Player:
    #def __init__(self, position, starting_money):
        #self.position = position
        #self.money = starting_money
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
deck = ['{} of {}'.format(*card) for card in ((x,y) for x in values for y in suits)]

random.shuffle(deck)

deal = lambda x: [deck.pop() for _ in range(x)]

num_players = int(input("How many players (2-8): "))

players = []
players.append(Player("Human", deal(2)))
for i in range(num_players - 1):
    players.append(Player("CPU {}".format(i + 1), deal(2)))

for player in players:
    print("{}: {}, {}".format(player.name, *player.hand))

flop, turn, river = deal(3), deal(1), deal(1)
print("Flop: {}, {}, {}".format(*flop))
print("Turn: {}".format(*turn))
print("River: {}".format(*river))

#print("Winner: {}, with a {}.".format(winner, best_hand))
