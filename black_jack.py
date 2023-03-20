

import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)


def BlackJack():
    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)

    def calculate_score(players_cards):
        sum(players_cards)
        if sum(players_cards) == 21 and len(players_cards) == 2:
            return 0
        if sum(players_cards) > 21 and 11 in players_cards:
            for x in players_cards:
                if x == 11:
                    players_cards[players_cards.index(x)] = 1
        return sum(players_cards)
    user_cards = []
    dealer_cards = []
    is_game_over = False
    
  
    #dealing cards
    for _ in range(2):
      user_cards.append(deal_card())
      dealer_cards.append(deal_card())
    
    while not is_game_over:
      #calculating score
      user_score = calculate_score(user_cards)
      dealer_score = calculate_score(dealer_cards)
      print(f"  Your cards: {user_cards}, current score: {user_score}")
      print(f"  Dealers first card: {dealer_cards[0]}")
      
      #checking score
      if user_score == 0 or dealer_score == 0 or user_score > 21:
        is_game_over = True
      else:
        hit_me = input("Type 'y' to get another card, type 'n' to pass. ")
        if hit_me == "y":
          user_cards.append(deal_card())
        else:
          is_game_over = True
    
    while dealer_score != 0 and dealer_score < 17:
      dealer_cards.append(deal_card())
      dealer_score = calculate_score(dealer_cards)
    
    def compare_scores(user_score, dealer_score):
      if user_score == dealer_score:
        return "It's a draw."
      elif dealer_score == 0:
        return "You lose."
      elif user_score == 0:
        return "You win!"
      elif user_score > 21:
        return "You lose."
      elif dealer_score > 21:
        return"You win!"
      elif user_score > dealer_score:
        return "You win!"
      else:
        return "You lose."
        
    print(f"  The dealers cards are {dealer_cards}, score: {dealer_score}")
    print(f"  Your cards are {user_cards}, score: {user_score}")
    print(compare_scores(user_score, dealer_score))

    
while input("Do you want to play BlackJack? Type 'y' or 'n': ") == "y":
    
    BlackJack()
    