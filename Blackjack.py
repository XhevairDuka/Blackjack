# We are creating a blackjack game with a computer dealer and one human player.
import random
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


#  Card class
class Card:  # card class to create an individual card with a suit, rank and value
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):  # string method to print card
        return self.rank + ' of ' + self.suit


class Deck:  # deck class to create and store instances of the card class to construct a deck
    def __init__(self):

        self.deck = []  # empty list to store the cards

        for suit in suits:  # nest for loops to create cards and append to all_cards list
            for rank in ranks:
                created_card = Card(suit, rank)
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has : ' + deck_comp

    def shuffle(self):  # shuffle function to randomize our deck list

        random.shuffle(self.deck)  # using built-in random function to shuffle deck

    def deal(self):  # function to deal one card

        return self.deck.pop()  # using the pop method to take the first element out of our deck


class Hand:

    def __init__(self):
        self.cards = []  # empty list to add cards in hand to
        self.value = 0  # value of cards in hand
        self.aces = 0  # how many aces in hand

    def add_card(self, card):
        # card is being passed by the Deck.deal method we created and the card has a (suit,rank)
        self.cards.append(card)  # appending the card passed in to the cards list
        self.value += values[card.rank]  # finding the value of the card rank and adding it ot the hand value
        # track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # checks for a value greater than 21 and if there is still an ace in hand
        # if true for both then ace will be treated as 1 instead of 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

"""
# Test for card and deck class
test_deck = Deck()  # generates a deck
print(test_deck)  # prints the deck

test_deck.shuffle()  # shuffles the deck
print(test_deck)  # print new shuffled deck

test_player = Hand()  # creates the player hand object

dealtcard = test_deck.deal()  # uses the deal method and assigns a variable 
print(dealtcard)  # shows card that is dealt

test_player.add_card(pulled_card)  # adds dealt card to players hand
print(test_player.value)  # shows players hand value

test_player.add_card(test_deck.deal())  # this line can replace the above lines
"""


class Chip:

    def __init__(self, total=100):
        self.total = total  # sets player chip total to 100
        self.bet = 0  # placeholder for the users bet
    def win_bet(self):
        self.total += self.bet  # if user wins add bet to chip total
    def lose_bet(self):
        self.total -= self.bet  # if user loses subtract bet from chip total


def take_bet(chips):
    while True:

        try:
            chips.bet = int(input("How much would you like to bet? "))  # asks player how much they would like to bet
        except:
            print('Sorry you can only enter an integer')  # if player does not enter an integer
        else:
            if chips.bet > chips.total:  # check if the user is trying to bet more than what they have
                print(f'Sorry you do not have enough chips. You have {chips.total} chips')
            else:
                break


def hit(deck, hand):

    hand.add_card(deck.deal())  # deals a card to the players hand using methods
    hand.adjust_for_ace()  # using the adjust for ace method


def hit_or_stand(deck, hand):
    global playing  # global variable to maintain play

    while playing:
        x = input('Do you want to hit or stand? Enter h or s: ')  # asks the player if they want to hit or stand
        if x[0].lower() == 'h':  # uses hit function to add card to player hand for hit
            hit(deck, hand)

        elif x[0].lower() == 's':  # player stands and passes to dealer's turn
            print("Player stands, Dealer's turn")
            playing = False

        else:  # if users enters anything but h or s
            print(" I don't understand that input. Please only enter h or s")
            continue
        break


def show_some(player, dealer):  # will only show one of the dealers cards
    print("\n Dealer's Hand: ")
    print("First card is hidden!")
    print(dealer.cards[1])  # will only reveal one of dealers cards

    print("\n Player's Hand: ")  # will show players hand
    for card in player.cards:  # iterates through player hand
        print(card)


def show_all(player, dealer):
    print("\n Dealer's Hand: ")
    for card in dealer.cards:
        print(card)

    print(f"Dealer Hand Value: {dealer.value}")

    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)
    print(f"Player Hand Value: {player.value}")


def player_busts(player, dealer, chips):
    print('PLAYER BUST!')
    chips.lose_bet()
    print(chips.total)


def player_wins(player, dealer, chips):
    print('PLAYER WINS!')
    chips.win_bet()
    print(chips.total)


def dealer_busts(player, dealer, chips):
    print('DEALER BUSTS! PLAYER WINS')
    chips.win_bet()
    print(chips.total)


def dealer_wins(player, dealer, chips):
    print('DEALER WINS!')
    chips.lose_bet


def push(player, dealer):
    print('Dealer and player tie! PUSH')


# FULL GAME LOGIC
while True:
    print('WELCOME TO BLACKJACK\n\n\n')

    print('Shuffling the deck\n\n')
    deck = Deck()   # create a deck instance
    deck.shuffle()  # shuffle the deck
    print('Dealing cards\n\n')
    player_hand = Hand()  # create player hand instance
    player_hand.add_card(deck.deal())  # add cards to the player hand
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()  # create dealer hand instance
    dealer_hand.add_card(deck.deal())  # add cards to dealers hand
    dealer_hand.add_card(deck.deal())

    player_chips = Chip()  # giving player their chips

    take_bet(player_chips)  # prompting for player bet

    show_some(player_hand, dealer_hand)  # showing hands, only one card for dealer
    print('Players Turn!\n')
    playing = True
    while playing:
        hit_or_stand(deck, player_hand)  # asks the player to hit or stand

        show_some(player_hand, dealer_hand)  # same as before

        if player_hand.value > 21:  # checks if player hand value is greater than 21
            player_busts(player_hand, dealer_hand, player_chips)  # if greater, player busts
            break
    if player_hand.value <= 21:  # if player stands under 21, dealers turn
            print('Dealers Turn!')
            while dealer_hand.value < 17:  # soft 17 rule. Dealer will not go above 17
                hit(deck, dealer_hand)
            show_all(player_hand, dealer_hand)  # now shows both player and full dealers hand

            if dealer_hand.value > 21:  # check all win conditions
                dealer_busts(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)

            else:
                push(player_hand, dealer_hand)

            print(f'\n Player chips: {player_chips.total}')

    new_game = input('Would you like to play another hand? (y/n)')  # prompt if player wants to play again

    if new_game[0].lower() == 'y':
        playing = True
    else:
        print('Thank you for playing!')
        break
