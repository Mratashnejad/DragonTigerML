class Card:
    suits = ["Spades" , "Heart" , "Clubs" , "Dimonds"]
    ranks = {'A': 1 , '2':2 , '3':3 , '4':4, '5':5,'6':6, '7':7 , '8':8 , '9':9, '10':10, 'J': 11 , 'Q':12 ,'K':13}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"
class CuttingCard:
    cuttingcard1 = "Cutting Card1"
    cuttingcard2 = "Cutting Card2"

    def __init__(self,cuttingcard1,cuttingcart2):
        self.cuttingcard1 = cuttingcard1
        self.cuttingcard2 = cuttingcart2

    def __repr__(self):
        return str(self.cuttingcard1 , self.cuttingcard2)
        
class Deck(Card):
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in self.suits for rank in self.ranks.keys()]
    def __repr__(self):
        return str(self.deck)

class Shoe(Deck,CuttingCard):

    def __init__(self,shoe = None):
        super().__init__()
        if shoe is None:
            self.shoe = [self.deck for i in range(8)] + [self.cuttingcard2] #here cutting curd must be at the end of the shoe
        else :
            self.shoe = shoe

    def __repr__(self):
        rep = str(self.shoe)
        return rep 

if __name__ == '__main__':
    # print(Card("Spades", "A"))
    #print(Deck())
    print("start shoe")
    print(Shoe())
    print("end shoe")