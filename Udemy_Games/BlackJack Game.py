import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

print("******* Welcome To BlackJack *******\n")

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank+' of '+self.suit


class Deck():

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+card.__str__()
        return 'The Deck Contains:'+deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips():

    def __init__(self, total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self, a=1):
        self.total += self.bet//a

    def lose_bet(self, a=1):
        self.total -= self.bet//a


def take_bet(chips):
    while True:
        try:
            chips.bet = abs(int(input('How many chips would you like to bet?: ')))
            if chips.bet == 0:
                print("Sorry! Please Provide a Non-Zero Value")
                continue
        except:
            print('Sorry! Please Enter an Integer')
        else:
            if chips.bet > chips.total:
                print('Sorry! You do not have enough chips. You Have: {} chips'.format(chips.total))
            else:
                break

def take_chips():
    while True:
        try:
            c = abs(int(input("Enter the number of chips You Have: ")))
            if c == 0:
                print("Sorry! Please Provide a Non-Zero Value")
                continue
        except:
            print("Sorry! Please Enter an Integer")
        else:
            return c

def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input('Do You Want to Hit or Stand? Enter h or s: ')

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn!")
            playing = False
        else:
            print("Sorry! I did not understand that. Please Enter h or s only!!!")
            continue
        break

def show_some(player, dealer):
    print("\nDealer's Hand(One Card Hidden!):\n{}".format(dealer.cards[1]))
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    print("\nDealer's Hand: ")
    for card in dealer.cards:
        print(card)
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)

def player_busts(chips):
    print("\nPlayer Busted!")
    chips.lose_bet()

def player_wins(chips):
    print("\nPlayer Wins:)")
    chips.win_bet(2)

def dealer_busts(chips):
    print("\nDealer Busted!  Player Wins:)")
    chips.win_bet()

def dealer_wins(chips):
    print("\nDealer Wins!")
    chips.lose_bet(2)

def push():
    print("\nDealer and Player Ties! PUSH")

c = take_chips()
Player_chips = Chips(c)

while True:

    deck = Deck()
    deck.shuffle()

    Player_hand = Hand()
    Player_hand.add_card(deck.deal())
    Player_hand.add_card(deck.deal())

    Dealer_hand = Hand()
    Dealer_hand.add_card(deck.deal())
    Dealer_hand.add_card(deck.deal())

    take_bet(Player_chips)

    show_some(Player_hand, Dealer_hand)

    while playing:

        hit_or_stand(deck, Player_hand)
        show_some(Player_hand, Dealer_hand)

        if Player_hand.value > 21:
            player_busts(Player_chips)
            break

    if Player_hand.value <= 21:

        while (Dealer_hand.value < Player_hand.value or Dealer_hand.value == Player_hand.value < 15) and Dealer_hand.value <= 17:
            hit(deck, Dealer_hand)

        show_all(Player_hand, Dealer_hand)

        if Dealer_hand.value > 21:
            dealer_busts(Player_chips)
        elif Dealer_hand.value > Player_hand.value:
            dealer_wins(Player_chips)
        elif Dealer_hand.value < Player_hand.value:
            player_wins(Player_chips)
        else:
            push()

    print("Player's Total chips are: {}".format(Player_chips.total))

    new_game = input("\nDo You want to Play Again? y/n: ")

    if new_game[0].lower() == 'y':
        if Player_chips.total > 0:
            playing = True
            continue
        else:
            print("You don't have any chips to play!")
            ch = input("Do You Want to get chips? y/n: ")
            if ch[0].lower() == 'y':
                c = take_chips()
                Player_chips = Chips(c)
            else:
                print("\nThank You for Playing:)")
                break
    else:
        print("\nThank You for Playing:)")
        break



