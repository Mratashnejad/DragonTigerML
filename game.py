#how dragon tiger should play.


#we have 8 * 52 cards in each deck . 
#there is a cutting card inside each deck,and that card has no FIX position in the deck.but its almost making deck
#to the tow part.



Cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
Suits = ['Clubs','Diamonds','Hearts','Spades']
DeckSize = 52 * 8
c=[]
counter = 0
def deck(Cards,Suits):
    for i in range(len(Suits)):
        for j in range(len(Cards)):
            c.append(Cards[j]+" "+Suits[i])
            print(c)
           

deck(Cards,Suits)
