############### Simplified Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

################################################
from replit import clear
import random

should_continue_game = True

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

welcome_message = 'Welcome to black-jack game!'

# start
welcome_message = 'Welcome to black-jack game!'
print(welcome_message)

balance = 100
while should_continue_game:
  # set the player's initial balance
  
  print(f'Your balance is {balance}.')

  # How much to bet?
  is_valid_bet = False
  while not is_valid_bet:
    try:
      bet = int(input('How much do you bet?: '))
      remaining_balance = balance - bet
      if bet > balance:
        print('Invalid: bet exceeds your balance.')
        print('Try again.')
      else:
        print(f'Your bet is {bet}.')
        print(f'Your remaining balance is {remaining_balance}')
        is_valid_bet = True
    except:
      print('Invalid: something wrong with your input.')
      print('Try again.')

  # Player and dealer's cards are displayed
  player_cards = []
  dealer_cards = []

  for i in range(2):
    player_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))
  print(f'Player: {player_cards}')
  # print(f'Dealer: {dealer_cards}')
  print(f'Dealer: [{dealer_cards[0]}, ?]')

  # Pick one more?
  should_continue_player = True
  while should_continue_player:
    pick_one_more = input('Pick one more? (y / n): ')
    if pick_one_more == 'y':
      player_cards.append(random.choice(cards))
      print(f'Player: {player_cards}')
      # print(f'Dealer: {dealer_cards}')
      print(f'Dealer: [{dealer_cards[0]}, ?]')
    elif pick_one_more == 'n':
      should_continue_player = False
    else:
      print('Invalid input. try again.')

    # calculate the score
    player_score = sum(player_cards)
    dealer_score = sum(dealer_cards)

    # Check the player's score is over 21
    if player_score > 21:
      print('You lose')
      balance -= bet
      continue

  # show each other
  print(f'Player\'s score: {player_score}')
  print(f'Dealer\'s score: {dealer_score}')

  # if dealer's score is less than 17, pick one more cards
  if dealer_score < 17:
    should_continue_dealer = True
    while should_continue_dealer:
      if dealer_score < 17:
        print('Dealer pick one more cards')
        dealer_cards.append(random.choice(cards))
        dealer_score = sum(dealer_cards)
        if 11 in dealer_cards and dealer_score > 21:
          dealer_cards.remove(11)
          dealer_cards.append(1)
          dealer_score = sum(dealer_cards)
        print(f'Player: {player_cards}')
        print(f'Dealer: {dealer_cards}')
        print(f'Player\'s score: {player_score}')
        print(f'Dealer\'s score: {dealer_score}')
      else:
        should_continue_dealer = False

  # Check the dealer is over 21
  if dealer_score > 21:
    print('You win')
    balance += bet
    continue

  # Who's the winner?
  result = ''
  if player_score == dealer_score:
    result = 'Draw'
  elif player_score > dealer_score:
    result = 'Win'
  else:
    result = 'Lose'

  # add / subtract / do nothing depending on the result
  if result == 'Win':
    balance += bet
  elif result == 'Lose':
    balance -= bet

  # display the player's balance
  print(f'You {result}.')
  print(f'Your current balance {balance}')

  # Play again?
  play_again = input('Play again? (y / n): ')
  if play_again == 'y':
    should_continue_game = True
  else:
    should_continue_game = False
  clear() 

# End

###########################################

