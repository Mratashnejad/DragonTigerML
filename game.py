#how dragon tiger should play.


#we have 8 * 52 cards in each deck . 
#there is a cutting card inside each deck,and that card has no FIX position in the deck.but its almost making deck
#to the tow part.


Suits = ['Clubs','Diamonds','Hearts','Spades']
Cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

# DeckSize = 52 * 8
Deck=[]
# counter = 0
def deck(Cards,Suits):
    for i in Suits:
        for j in Cards:
            Deck = j + " " + i
            print(Deck)
        print("\n")
deck(Cards,Suits)
