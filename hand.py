from card import *

class hand:

	def __init__(self):
		self.card_array = []
		self.hand_strength = None



	def add_card_to_hand(self, card):
		self.card_array.append(card)



	def s(self):
		self.card_array = []



	def get_hand(self):
		return self.card_array



	def get_hand_size(self):
		return len(self.card_array)



	def set_hand_strength(self, hand_strength):
		self.hand_strength = hand_strength



	def get_hand_strength(self, hand_strength):
		return self.hand_strength


	def sort_5_cards(self, array_of_cards):
		output_array = array_of_cards

		#sort the cards using bubble sort
		for i in range(len(output_array)):
			for j in range(len(output_array) - 1):
				card_1_rank = output_array[j].get_rank()
				card_2_rank = output_array[j + 1].get_rank()

				if card_1_rank > card_2_rank:
					#do the swap
					lower_card = output_array[j + 1]
					output_array[j + 1] = output_array[j]
					output_array[j] = lower_card

		return output_array



	def find_hand_strength(self, community_cards):
		# this is gonna be the hard algorithm
		# list of all posible poker hands
		# royal flush, straight flush, Quads, full house, flush, straight, trips, two pair, pair, high card

		# giving all these hand strengths a number, would be 10, 9, 8, 7, .... , 1

		# royal flush = 10, straight flush = 9, quads = 8, full house = 7, flush = 6
		# straight = 5, trips = 4, two pair = 3, pair = 2, high card = 1

		# for eample, quads should have a weighting of 8, but because quad Aces should beat quad 2s, we gotta ensure that the Aces beat the 2's each time

		# this is easy, as every hand is ranked by its highest card
		# I am thinking of assigning the quad aces a weighting of 8.14 (as the ace is equivilant to a 14), and the quad 2's a weighting of 8.02
		# giving each card a weight of Ace = 14, King = 13, .... Two = 2, we can try to assign decimal point weights
		# Ace only counts as a low card in one specific straight, so we can treat it as 14 with no wories

		# also have to handle whether that 5th card will be the tiebreaker,
		# so 7 7 7 7 2 would lose to 7 7 7 7 King
		# and the hand strength would look like 8.0702 and 8.0713 respectively

		# a similar method can be used with all other hands.
		# a flush of Ace King 10 7 2 would have a strength of 6.1413100702

		# a high card hand of Ace King 10 7 6 would have a strength of 1.1413100706

		#this way hand strengths can be compared by a simple comparison

		# the good news for these decimal point weights, you just mulitply the rank of the card by 10^(-x) and add it to the running weight

		all_useable_cards = self.card_array + community_cards
		x = 12


	def what_hand_is_this(self, array_of_cards):
		#this funciton should, given 5 cards in the input array, return the strongest hand
		return 0




	def check_for_royalflush(self, array_of_cards):
		# strength of 0 means that this hand type wasnt found
		strength = 0

		return strength

	def check_for_straigtflush(self, array_of_cards):
		x = 12
		return True

	def check_for_quads(self, array_of_cards):
		x = 12
		return True

	def check_for_fullhouse(self, array_of_cards):
		x = 12
		return True

	def check_for_flush(self, array_of_cards):
		x = 12
		return True

	def check_for_straight(self, array_of_cards):
		x = 12
		return True

	def check_for_trips(self, array_of_cards):
		x = 12
		return True

	def check_for_twopair(self, array_of_cards):
		x = 12
		return True

	def check_for_pair(self, array_of_cards):
		x = 12
		return True

	def check_for_high_card(self, array_of_cards):
		x = 12
		return True



