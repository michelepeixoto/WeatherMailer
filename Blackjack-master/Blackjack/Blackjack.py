#!/path/to/interpreter
#!/usr/bin/env python3.6

import random

class Deck:

    def __init__(self):
        pass

    def __len__(self):
        return 52

    def card():
        cards = list(range(14))
        cards[0] = "A"
        cards[11] = "J"
        cards[12] = "Q"
        cards[13] = "K"
        deck = cards*4
        return deck[random.randint(1,51)]

class Player:

    def __init__(self, name, money):
        self.name = str(name)
        self.money = int(money)
        self.hand = []
        pass

    def __str__(self):
        return "{}: ${}".format(self.name, self.money)

    def lose_money(self, money):
        self.money -= int(money)
        pass

    def win_money(self, money):
        self.money += int(money)
        pass


def new_round(player, dealer):
    deck = Deck
    bet = int(input("How much will you bet? Enter a number:\n"))
    if bet > player.money:
        print("Not enough funds.")
        new_round(player, dealer)
        pass
    else:
        player.lose_money(bet)
        pass
    print("Dealing cards...")
    player.hand = [deck.card(), deck.card()]
    dealer.hand = [deck.card(), deck.card()]
    print("{} has [{}] and [{}]".format(str(dealer.name), str(dealer.hand[0]), "hidden"))
    print("{} has [{}] and [{}]".format(str(player.name), str(player.hand[0]), str(player.hand[1])))
    choice = "y"
    while choice == "y":
        choice = input("Hit? Type y/n\n")
        if choice != "y":
            print("You stand.")
            print("{} has {}".format(str(dealer.name), str(dealer.hand)))
            print("{} has {}".format(str(player.name), str(player.hand)))
            break
        else:
            player.hand.append(deck.card())
            print("You drew a [{}]".format(player.hand[-1]))
            continue
        pass
    dealer_points = 0
    for cards in range(len(dealer.hand)):
        if dealer.hand[cards] == "A":
            dealer_points += 11
            pass
        elif dealer.hand[cards] == "J" or dealer.hand[cards] == "Q" or dealer.hand[cards] == "K":
            dealer_points += 10
            pass
        else:
            dealer_points += dealer.hand[cards]
            pass
        pass
    while dealer_points < 17:
        dealer.hand.append(deck.card())
        print("Dealer drew a [{}]".format(dealer.hand[-1]))
        if dealer.hand[-1] == "A":
            dealer_points += 11
            pass
        elif dealer.hand[-1] == "J" or dealer.hand[-1] == "Q" or dealer.hand[-1] == "K":
            dealer_points += 10
            pass
        else:
            dealer_points += dealer.hand[-1]
            pass
        if dealer_points >= 17:
            break
        else: 
            continue
        pass
    winner = win_check(player, dealer)
    print(winner.name+" wins!")
    winner.win_money(bet*2)
    print("Ending totals:")
    print(player)
    choice = input("Play again? Type y/n\n")
    if choice == "y":
        new_round(player, dealer)
        pass
    else:
        print("Thanks for playing {}.\nYour ending balance: ${}".format(player.name, player.money))
        game()
        pass
    pass

def win_check(player, dealer):
    player_points, dealer_points = 0, 0
    for cards in range(len(player.hand)):
        if player.hand[cards] == "A":
            player_points += 11
            pass
        elif player.hand[cards] == "J" or player.hand[cards] == "Q" or player.hand[cards] == "K":
            player_points += 10
            pass
        else:
            player_points += player.hand[cards]
            pass
    for cards in range(len(dealer.hand)):
        if dealer.hand[cards] == "A":
            dealer_points += 11
            pass
        elif dealer.hand[cards] == "J" or dealer.hand[cards] == "Q" or dealer.hand[cards] == "K":
            dealer_points += 10
            pass
        else:
            dealer_points += dealer.hand[cards]
            pass
    if player_points > dealer_points and player_points <= 21:
        return player
    elif dealer_points > 21 and player_points <= 21:
        return player
    elif player_points == 21 and dealer_points != 21:
        return player
    else:
        return dealer
    pass

def game():
    print("Blackjack")
    name = input("What is your name?\n")
    money = input("How much will you play with?\n")
    player = Player(name, money)
    dealer = Player("Dealer", 0)    
    print("Aces are worth 11, face cards are worth 10.")
    print("Have fun!")
    new_round(player, dealer)
    pass


game()
#test
