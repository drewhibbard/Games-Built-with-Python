#!/usr/bin/env python
# coding: utf-8

# In[ ]:


suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
        'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10,
         'King': 10, 'Ace': 11}

playing = True


# In[ ]:


class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return f'{self.rank} of {self.suit}'


# In[ ]:


import random

class Deck:
    
    def __init__(self):
        self.deck = []
        for rank in ranks:
            for suit in suits:
                self.deck.append(Card(suit, rank))
                
    def __str__(self):
        current_deck = ''
        for card in self.deck:
            current_deck += '\n' + card.__str__()
        return current_deck
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        new_card = self.deck.pop()
        return new_card
        


# In[ ]:


class Hand:
    
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
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# In[ ]:


class Chips:
    
    def __init__(self, total=100):
        self.total = total
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet


# In[ ]:


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('\nHow many chips would you like to bet?'))
        except ValueError:
            print('That is not a valid number.  Try again.')
        else:
            if chips.bet > chips.total:
                print('Bet exceeds available chips.  Try again.')
            else:
                break


# In[ ]:


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


# In[ ]:


def hit_or_stand(deck, hand):
    global playing 
    
    while True:
        choice = input('Hit (h) or Stand (s)?')
        if choice[0].lower() == 'h':
            hit(deck, hand)
        elif choice[0].lower() == 's':
            print('\nPlayer stands. Dealer will now play.')
            playing = False
        else:
            print('\nInvalid entry. Please try again.')
            continue
        break


# In[ ]:


def show_some(player, dealer):
    print('\nPlayer:')
    print(*player.cards, sep = '\n')
    print('\nDealer:')
    print('<Hidden>')
    print(dealer.cards[1])
          
def show_all(player, dealer):
    print('\nPlayer:')
    print(*player.cards, sep = '\n')
    print('\nDealer:')
    print(*dealer.cards, sep = '\n')


# In[ ]:


def player_bust(chips):
    print('Player busts!')
    chips.lose_bet()
    
def blackjack(chips):
    print('Blackjack!')
    chips.win_bet()
    
def player_win(chips):
    print('Player wins!')
    chips.win_bet()
    
def dealer_bust(chips):
    print('Dealer busts! Player wins!')
    chips.win_bet()

def dealer_win(chips):
    print('Dealer wins!')
    chips.lose_bet()
    
def push():
    print('Tie. Push')


# In[ ]:


player_chips = Chips()

while True:
    
    print('Welcome to Blackjack!')
    
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    
    
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    take_bet(player_chips)
    show_some(player_hand, dealer_hand)  
     
    while playing:
        
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)
        
        if player_hand.value > 21:
            player_bust(player_chips)
            break
            
    if player_hand.value <=21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
            
        show_all(player_hand, dealer_hand)
        
        if player_hand.value > dealer_hand.value and player_hand.value == 21:
            blackjack(player_chips)
        elif player_hand.value > dealer_hand.value:
            player_win(player_chips)
        elif player_hand.value < dealer_hand.value:
            dealer_win(player_chips)
        elif dealer_hand.value > 21:
            dealer_bust(player_chips)
        else:
            push()
            
    print(f'\nPlayer now has {player_chips.total} chips')
    
    replay = input('Would you like to play another hand?')
    if replay[0].upper() == 'Y':
        playing = True
        continue
    else:
        print('\nThanks for playing! Goodbye.')
        break
 


# In[ ]:




