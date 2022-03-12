class card:

	def __init__(self, num):
		#number is an int from 1 to 52
		self.num = num
		self.rank = self.find_rank()
		self.suit = self.find_suit()



	def get_rank(self):
		return self.rank



	def get_rank_string(self):
		rank_name = {
			1: "Ace",
			2: "Two",
			3: "Three",
			4: "Four",
			5: "Five",
			6: "Six",
			7: "Seven",
			8: "Eight",
			9: "Nine",
			10: "Ten",
			11: "Jack",
			12: "Queen",
			0: "King"
		}

		return rank_name[self.rank]



	def get_suit(self):
		return self.suit



	def print_card_as_string(self):
		print(self.get_rank_string() + " of " + self.get_suit())



	def find_rank(self):
		#returns the rank of a card, if the rank is 1 (aka the card is an Ace), make the rank 14
		rank = self.num%13
		if rank == 1:
			#this is an ace, make the rank 14
			rank = 14

		return rank



	def find_suit(self):
		number = self.num
		if (number >= 1) and (number <= 13):
			return "Spades"
		if (number >= 14) and (number <= 26):
			return "Hearts"
		if (number >= 27) and (number <= 39):
			return "Clubs"
		if (number >= 40) and (number <= 52):
			return "Diamonds"