from card import *
from hand import *


class player:

	def __init__(self, name):
		self.name = name
		self.hand = hand()
		self.hand_strength = 0



	def set_name (self, name):
		self.name = name



	def get_name (self, name):
		return self.name



	def set_hand(self, card_1, card_2):
		self.hand.add_card_to_hand(card_1)
		self.hand.add_card_to_hand(card_2)



	def empty_hand(self):
		self.hand.empty_hand()



	def get_hand(self):
		return self.hand



	def set_hand_strength(self, hand_strength):
		self.hand_strength = hand_strength



	def get_hand_strength(self, hand_strength):
		return self.hand_strength



	def find_hand_strength(self, comunity_cards):
		self.hand.find_hand_strength(comunity_cards)



