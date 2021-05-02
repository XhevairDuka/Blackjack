#  Warm up code along for Milestone Project Two. We will be coding the card game WAR.
import random
# Global variables, values of the cards, suit of cards and ranks
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


#  Card class
class Card:  # card class to create an individual card with a suit, rank and value
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:  # deck class to create and store instances of the card class to construct a deck
    def __init__(self):

        self.all_cards = []  # empty list to store the cards

        for suit in suits:  # nest for loops to create cards and append to all_cards list
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):  # shuffle function to randomize our deck list

        random.shuffle(self.all_cards)  # using built-in random function to shuffle deck

    def deal_one(self):  # function to deal one card

        return self.all_cards.pop()  # using the pop method to take the first element out of our deck


class Player:  # Player class to create and manipulate player hand

    def __init__(self, name):

        self.name = name  # player name
        self.all_cards = []  # empty list to hold the players hand

    def remove_one(self):  # function to remove the top card of the players hand using the pop function
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):  # function to add cards to players hand after winning a round
        if type(new_cards) == type([]):  # extend method needed if the new cards are multiples to avoid nested list
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)  # for single card wins append can be used

    def __str__(self):  # special function to print number of cards in player hand
        return f'Player {self.name} has {len(self.all_cards)} cards'


"""
new_deck = Deck()

# print(new_deck.all_cards)  # will print memory addresses of the card for our new deck

first_card = new_deck.all_cards[0]  # assigns the first item in the new_deck list to first_card
print(first_card)  # now this will sure the special str function to show us the rank and suit of the card

new_deck.shuffle()  # here we use our created shuffle function to shuffle the list of cards

print(new_deck.all_cards[0])  # now the card at the first position is no longer Two of Hearts, so our shuffle worked

my_card = new_deck.deal_one()  # assigning the my_card variable by testing the deal_one function

print(my_card)

print(len(new_deck.all_cards))  # we can check that deal_one function worked because the length of our list decreased

new_player = Player('X')  # creating a player class

print(new_player)  # printing new player shows us the player hand count

new_player.add_cards(my_card)  # now we add a card to the players hand

print(new_player)  # new player hand count

print(new_player.all_cards[0]) # check the card in the players hand at index 0

new_player.add_cards([my_card, my_card, my_card])  # adding more cards

print(new_player) # new player hand count

new_player.remove_one()  # use remove_one method to test

print(new_player)  # confirm new player hand count decreased
"""

player_one = Player('One')  # setting up the player objects
player_two = Player('Two')

new_deck = Deck()  # creating a new deck
new_deck.shuffle()  # shuffling the deck

for x in range(26):  # for loop to give players half of the deck
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True  # variable for game continuation
round_num = 0  # variable to keep track of round count

while game_on:  # while loop to continue game
    round_num += 1  # round counter will increase with each iteration
    print(f'Round Number {round_num}')

    # checks for win condition, if players hand is 0 cards
    if len(player_one.all_cards) == 0:
        print('Player One has run out of cards. Player Two wins!')
        game_on = False
    if len(player_two.all_cards) == 0:
        print('Player Two has run out of cards. Player One wins!')
        game_on = False

    player_one_cards = []  # this is the variable for the cards on the table from player ones hand
    player_one_cards.append(player_one.remove_one())  # removes card from player ones hand and puts it on table

    player_two_cards = []  # same as above but for player two
    player_two_cards.append(player_two.remove_one())

    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            print("WAR!")

            if len(player_one.all_cards) < 5:
                print('Player One cannot declare war')
                print('Player Two wins!')
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print('Player Two cannot declare war')
                print('Player One wins!')
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
