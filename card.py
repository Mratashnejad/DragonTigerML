class Card:
    suits = ["Spades" , "Heart" , "Clubs" , "Dimonds"]
    ranks = {'A': 1 , '2':2 , '3':3 , '4':4, '5':5,'6':6, '7':7 , '8':8 , '9':9, '10':10, 'J': 11 , 'Q':12 ,'K':13}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck(Card):
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in self.suits for rank in self.ranks.keys()]

    def __repr__(self):
        return str(self.deck)

class Shoe(Deck):
    def __init__(self, number_of_decks):
        super().__init__()
        self.number_of_decks = number_of_decks
        self.shoe = self.deck * number_of_decks
    
    def __repr__(self):
        return str(self.shoe)

if __name__ == '__main__':
    # print(Card("Spades", "A"))
    print(Deck())
    # print(Shoe(2))
