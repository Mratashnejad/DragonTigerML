import collections
import random


PlayingCard = collections.namedtuple('card', ['suit' , 'rank'])

class PlayingDeck :
    ranks = [str(rank) for rank in range(2,11)] + ['J','Q','K','A']
    suits = ['Spades' , 'Diamonds' , 'Hearts' , 'Clubs']

    def __init__(self):
        self._cards = [PlayingCard(rank, suit)
        for suit in self.suits
            for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self,position):
        return self._cards[position]
    
if __name__ == '__main__':
    deck = PlayingDeck()

    for card in deck:
        print(card)
    
    for card in reversed(deck):
        print(card)

    random.shuffle(deck._cards)
    for card in deck:
        print(card)




