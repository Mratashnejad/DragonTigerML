import collections
import random


PlayingCard = collections.namedtuple('card', ['suit' , 'rank'])

class PlayingDeck :
    ranks = [str(rank) for rank in range(2,11)] + ['J','Q','K','A']
    suits = ['Spades' , 'Diamonds' , 'Hearts' , 'Clubs']
    rank_values = {'J' : 11, 'Q':12,'K':13,'A':1}

    def __init__(self):
        self._cards = [PlayingCard(rank, suit)
        for suit in self.suits
            for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self,position):
        return self._cards[position]

    def deal(self):
        return self._cards.pop()

    def play(self):
        self.Dragon = self.deal()
        self.Tiger = self.deal()

    def result(self):
        print("Dragon is :", self.Dragon.rank , "of" , self.Dragon.suit)
        print("Tiger is :", self.Tiger.rank , "of" , self.Tiger.suit)
        dragon_value = self.rank_values.get(self.Dragon.rank,self.Dragon.rank)
        tiger_value = self.rank_values.get(self.Tiger.rank , self.Tiger.rank)

        if dragon_value > tiger_value :
            print("Dragon won with {} of {}" .format(self.Dragon.rank , self.Dragon.suit))
        elif dragon_value < tiger_value :
            print("Tiger won with {} of {}" .format(self.Tiger.rank , self.Tiger.suit))
        else :
            print("It's a TIE")

    
if __name__ == '__main__':
    
    deck = PlayingDeck()
    random.shuffle(deck._cards)
    
    deck.play()
    deck.result()
    # for card in deck:
    #     print(card)
    
    # for card in reversed(deck):
    #     print(card)

    




