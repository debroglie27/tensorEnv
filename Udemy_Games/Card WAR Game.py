import random

Suits = ("Hearts", "Diamonds", "Spades", "Clubs")
Ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

class Card():

    def __init__(self, Suit, Rank):
        self.Suit = Suit
        self.Rank = Rank
        self.value = values[Rank]

    def __str__(self):
        return f"{self.Rank} of {self.Suit}"


class Deck():

    def __init__(self):
        self.deck = []
        for suit in Suits:
            for rank in Ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_one(self):
        return self.deck.pop()


class Player():

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


mydeck = Deck()
mydeck.shuffle()

player1 = Player("one")
player2 = Player("Two")

for i in range(26):
    player1.all_cards.append(mydeck.deal_one())
    player2.all_cards.append(mydeck.deal_one())

war_cards = 5
round_num = 0
game_on = True
while game_on:

    round_num += 1
    print(f"Round Number: {round_num}")

    if len(player1.all_cards) == 0:
        print("\nPlayer One out of cards!")
        print("Player Two Wins:)")
        game_on = False
        break

    if len(player2.all_cards) == 0:
        print("\nPlayer Two out of cards!")
        print("Player One Wins:)")
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player1.remove_one())

    player_two_cards = []
    player_two_cards.append(player2.remove_one())

    at_war = True
    while at_war:

        if player_one_cards[-1].value < player_two_cards[-1].value:
            player2.add_cards(player_one_cards)
            player2.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value > player_two_cards[-1].value:
            player1.add_cards(player_one_cards)
            player1.add_cards(player_two_cards)
            at_war = False

        else:
            print("War!")

            if len(player1.all_cards) < war_cards:
                print("Player One unable to declare War!")
                print("Player Two Wins:)")
                game_on = False
                break

            elif len(player2.all_cards) < war_cards:
                print("Player Two unable to declare War!")
                print("Player One Wins:)")
                game_on = False
                break

            else:
                for i in range(war_cards):
                    player_one_cards.append(player1.remove_one())
                    player_two_cards.append(player2.remove_one())

