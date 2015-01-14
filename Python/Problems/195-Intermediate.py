import random
import sys

print("Welcome to Math Dice Solver! What dice will you be using?")
dice = input(">").rstrip()

target_die, scoring_dice = dice.split()
discard, target_die = target_die.split('d')
num_of_sc_dice, type_of_sc_dice = scoring_dice.split('d')
num_of_sc_dice, type_of_sc_dice = int(num_of_sc_dice), int(type_of_sc_dice)
target = random.randrange(1, int(target_die) + 1)
dice_shown = []
dice_shown = [random.randrange(1, type_of_sc_dice + 1) for x in range(num_of_sc_dice)]
print("1d{} sets the Target to {}.".format(target_die, target))
print("{}d{} produces {} to work with.".format(num_of_sc_dice, type_of_sc_dice, dice_shown))

solution = "Figure it out, nerd."
print("One solution is: {}".format(solution))
