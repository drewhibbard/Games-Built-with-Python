#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# define function used to continually replay until user selects no

def replay():
    choice = input('Do you want to play again? y or n: ')
    return choice.lower() == 'y'


# In[ ]:


from IPython.display import clear_output

# create the board
def display_board(board):
    clear_output()
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])


# In[ ]:


# determine which player is X and which is O

def assign_markers():
    marker = ''
    while marker.upper() != 'X' and marker.upper() != 'O':
        marker = input('Player 1, choose X or O: ')
    if marker.upper() == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')        


# In[ ]:


# randomly assign who goes first

import random

def choose_first():
    num = random.randint(0,1)
    if num:
        return 'Player 1'
    else:
        return 'Player 2'


# In[ ]:


def place_marker(board, position, marker):
    board[position] = marker


# In[ ]:


# check if the desired position is available

def check_free(board, position):
    if board[position] != 'X' and board[position] != 'O':
        return True
    else:
        return False


# In[ ]:


# ask current player for their next move

def choose_position(board):
    choice = 0
    while choice not in range(1,10) or not check_free(board, choice):
        try:
            choice = int(input('Choose your next move.'))
        except:
            print('That position is taken.  Please try again.')
    return choice


# In[ ]:


# define the 8 possible winning combinations

def check_win(board, marker):
    if board[1] == board[2] == board[3] == marker:
        return True
    elif board[4] == board[5] == board[6] == marker:
        return True
    elif board[7] == board[8] == board[9] == marker:
        return True
    elif board[1] == board[4] == board[7] == marker:
        return True
    elif board[2] == board[5] == board[8] == marker:
        return True
    elif board[3] == board[6] == board[9] == marker:
        return True
    elif board[1] == board[5] == board[9] == marker:
        return True
    elif board[3] == board[5] == board[7] == marker:
        return True
    else:
        return False


# In[ ]:


# check if board is full, which will determine a tie if no winner is established

def check_full(board):
    for i in range(1, len(board)):
        if check_free(board, i):
            return False
    return True


# In[ ]:


# Gameplay

print('Welcome to Tic Tac Toe!')

while True:
    # set up board, player markers, and choose who goes first
    the_board = ['', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    player1_marker, player2_marker = assign_markers()
    turn = choose_first()
    print(turn + ' goes first!')
    
    play_game = input('Are you ready to play?')
    if play_game[0].lower() == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        
        if turn == 'Player 1':
            display_board(the_board)
            choice = choose_position(the_board)
            place_marker(the_board, choice, player1_marker)
            if check_win(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 Wins!')
                game_on = False
            else:
                if check_full(the_board):
                    display_board(the_board)
                    print('Tie game!')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            display_board(the_board)
            choice = choose_position(the_board)
            place_marker(the_board, choice, player2_marker)
            if check_win(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 Wins!')
                game_on = False
            else:
                if check_full(the_board):
                    display_board(the_board)
                    print('Tie game!')
                    game_on = False
                else:
                    turn = 'Player 1'
    
    if not replay():
        print('Thanks for playing! Goodbye.')
        break

