from card import *
import numpy as np

class deck:

	def __init__(self):
		#52 cards in a deck
		#stop funciton is weird which is why it says 53
		self.num_array = range(1, 53, 1)
		self.card_array = self.generate_card_array()



	def shuffle_num_array(self):
		shuffled_array = np.random.permutation(self.num_array)
		self.num_array = shuffled_array



	def get_deck_length(self):
		return len(self.card_array)



	def is_empty(self):
		if self.get_deck_length() == 0:
			return True
		else:
			return False



	def shuffle_deck(self):
		print("shuffling the deck")
		self.shuffle_num_array()
		self.card_array = self.generate_card_array()



	def generate_card_array(self):
		array_of_cards = []

		for i in range(len(self.num_array)):
			array_of_cards.append(card(self.num_array[i]))

		return array_of_cards



	def deal_card(self):
		if self.is_empty():
			print("Error: Deck has no more cards, cant deal another card!")
			return None
		else:
			dealt_card = self.card_array.pop()
			return dealt_card



	def print_deck(self):
		for i in range(len(self.card_array)):
			self.card_array[i].print_card_as_string()



	def print_num_array(self):
		for i in range(len(self.num_array)):
			print(self.num_array[i])
