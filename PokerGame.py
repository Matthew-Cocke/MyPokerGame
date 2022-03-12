################################################
# This is where stuff will be imported
import sys
import numpy as np

# Import Classes
from card import *
from deck import *
from player import *
from hand import *



################################################
# This is where funtions will be defined


def main():
	#print("Hello World, this is gonna be poker")

	#seven_spades = card(7)
	#king_diamonds = card(52)
	#rando_card = card(28)

	#print(rando_card.get_rank_string())
	#print(rando_card.get_suit())


	deck_of_cards = deck()
	#deck_of_cards.print_num_array()
	#deck_of_cards.print_deck()
	deck_of_cards.shuffle_deck()
	#deck_of_cards.print_num_array()
	#deck_of_cards.print_deck()

	card_array = []
	for i in range(5):
		card_array.append(deck_of_cards.deal_card())

	for i in range(len(card_array)):
		card_array[i].print_card_as_string()

	print("\n")

	test_hand = hand()
	test_hand.sort_5_cards(card_array)

	for i in range(len(card_array)):
		card_array[i].print_card_as_string()


	#print(deck_of_cards.get_deck_length())
	
	#card_1.print_card_as_string()
	#card_2.print_card_as_string()



################################################
# This will be the script part, try to keep this to just be a call of Main

main()








