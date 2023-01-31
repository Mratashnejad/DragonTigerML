import random
import time
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

    def addfirstcuttingcard(self):
        shoe_len = len(self.shoe)
        print(shoe_len)


class DragonTiger:
    Card = Card
    def __init__(self,shoe):
        self.shoe = shoe
        self.dragon_hand = []
        self.tiger_hand = []

    def shuffle(self):
        random.shuffle(self.shoe)

    def deal(self):
        self.dragon_hand = self.shoe.pop()
        self.tiger_hand = self.shoe.pop()

    def compare(self):
        dragon_vale = Card.ranks.get(self.dragon_hand.rank)
        tiger_value = Card.ranks.get(self.tiger_hand.rank)

        if dragon_vale > tiger_value :
            return "Dragon Won"
        elif dragon_vale < tiger_value :
            return "Tiger Won"
        else:
            return "Its a TIE"



if __name__ == '__main__':
    counter = 0

    while True:
        print("round number : ",counter)
        shoe = Shoe()
        game = DragonTiger(shoe.deck)
        game.shuffle()
        game.deal()
        print("Dragon is :", game.dragon_hand)
        print("Tiger is : ", game.tiger_hand)
        result = game.compare()
        print("Result:" ,result)
        counter += 1 
        print("End Round")
        time.sleep(3) # wait for 15 seconds before starting the next game
        