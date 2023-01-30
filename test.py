class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
class Deck(Card):
    def __init__(self):
        self.suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        self.ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.deck = []
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit, rank))
    
    def draw_card(self):
        return self.deck.pop()

class Shoe(Deck):
    def __init__(self, number_of_decks):
        self.number_of_decks = number_of_decks
        self.shoe = []
        for i in range(self.number_of_decks):
            deck = Deck()
            self.shoe += deck.deck

def compare_cards(dragon, tiger):
    dragon_value = int(dragon.rank) if dragon.rank.isdigit() else 10 if dragon.rank in ['J', 'Q', 'K'] else 11
    tiger_value = int(tiger.rank) if tiger.rank.isdigit() else 10 if tiger.rank in ['J', 'Q', 'K'] else 11
    if dragon_value > tiger_value:
        return "Dragon wins"
    elif tiger_value > dragon_value:
        return "Tiger wins"
    else:
        return "It's a tie"

# if __name__ == '__main__':
#     shoe = Shoe(1)
#     dragon = shoe.draw_card()
#     tiger = shoe.draw_card()
#     result = compare_cards(dragon, tiger)
#     print("Dragon is: {} of {}".format(dragon.rank, dragon.suit))
#     print("Tiger is: {} of {}".format(tiger.rank, tiger.suit))
#     print(result)
    
class DragonTiger:
    def __init__(self,shoe):
        self.shoe = shoe
        self.dragon_hand = []
        self.tiger_hand = []

    def deal(self):
        self.dragon_hand = self.shoe.deck.pop()
        self.tiger_hand = self.shoe.deck.pop()

    def compare(self):
        dragon_value = self.rank_values.get(self.dragon_hand.rank, self.dragon_hand.rank)
        tiger_value = self.rank_values.get(self.tiger_hand.rank, self.tiger_hand.rank)
        if dragon_value > tiger_value:
            return "Dragon won"
        elif tiger_value > dragon_value:
            return "Tiger won"
        else:
            return "It's a tie"

if __name__ == '__main__':
    shoe = Shoe(8)
    game = DragonTiger(shoe)
    game.deal()
    result = game.compare()
    print("Result:", result)
