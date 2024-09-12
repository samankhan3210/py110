import random
import os
import json
import shutil
import textwrap
import time

with open('twenty_one_messages.json', 'r', encoding='utf-8') as file:
    MESSAGES = json.load(file)

MAX_SCREEN_WIDTH = shutil.get_terminal_size().columns
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANK_CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', \
            'Jack', 'Queen', 'King', 'Ace']
CARD_VALUES = {'2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6,\
            '7' : 7, '8' : 8, '9' : 9, '10' : 10, 
    'Jack' : 10, 'Queen' : 10, 'King' : 10, 
    'Ace' : [1, 10]
}
GOAL = 21
MIN_DEALER_SCORE = 17
PLAYER = "player"
DEALER = "dealer"

def display_wrapped_message(prompt):
    print(textwrap.fill(prompt, width=MAX_SCREEN_WIDTH))

def display_welcome_screen():
    display_wrapped_message(MESSAGES['line'])
    display_wrapped_message(MESSAGES['welcome'])
    display_wrapped_message(MESSAGES['line'])
    display_wrapped_message(MESSAGES['rules_message'])

    for rule in MESSAGES['rules'].values():
        display_wrapped_message(rule)
        print()

    input()

def display_winner(prompt):
    print(MESSAGES['winner'].format(winner = prompt))

def join_and(lst, delimeter = ', ', last_word = 'and'):
    if isinstance(lst, list) and len(lst) > 1:
        lst_copy = lst[:]
        lst_copy[len(lst) - 1] = last_word + " " + lst[len(lst) - 1]
        joined_lst = delimeter.join(map(str, lst_copy))
        return joined_lst
    return lst

def display_cards_at_hand(player_cards, dealer_card):
    print(MESSAGES['dealers_cards'].format(
        dealer_card = join_and(dealer_card)))
    print(MESSAGES['players_cards'].format(
        player_cards = join_and(player_cards)))

def intialize_deck():
    deck = []
    for _ in SUITS:
        for card in RANK_CARDS:
            deck.append(card)
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)

def deal_cards(deck, cards):
    shuffle_deck(deck)
    cards[PLAYER] = [deck.pop(), deck.pop()]
    cards[DEALER] = [deck.pop(), deck.pop()]

def hit(deck, player_cards):
    new_card = deck.pop(0)
    player_cards.append(new_card)
    return new_card

def bust(score, player_name):
    if score > GOAL:
        print(MESSAGES['bust'].format(player = player_name.capitalize()))
        return True
    return False

def get_ace_value(current_value):
    if current_value + 11 <= GOAL:
        return 11
    return 1

def calculate_score_values(cards):
    score = 0
    aces = 0
    for card in cards:
        if card != "Ace":
            score += CARD_VALUES[card]
        else:
            aces += 1
    
    for _ in range(aces):
        score += get_ace_value(score)

    return score

def clear_screen(timer = 1):
    time.sleep(timer)
    os.system("cls || clear")

def player_turn(current_deck, player_cards, dealer_card):
    valid_choices = ["hit", "h", "stay", "s"]
    player_score = calculate_score_values(player_cards)
    print("---> Your Turn")

    while True:
        display_cards_at_hand(player_cards, dealer_card)
        print(f"Your Score : {player_score}")
        choice = input(MESSAGES["hit_or_stay"]).strip().lower()

        if choice not in valid_choices:
            print(MESSAGES['error_message'])
        else:
            if choice in ["hit", "h"]:
                print(MESSAGES['hit'])
                hit(current_deck, player_cards)
                player_score = calculate_score_values(player_cards)
                if bust(player_score, PLAYER):
                    player_score = 0
                    break

            else:
                print(MESSAGES['stay'])
                break

        clear_screen()
    return player_score

def dealer_turn(current_deck, dealer_cards):
    print("---> Dealer's Turn")
    dealer_score = calculate_score_values(dealer_cards)

    while dealer_score < MIN_DEALER_SCORE:
        print("Dealer has : ",join_and(dealer_cards))
        print(f"Dealer's Score : {dealer_score}")
        hit(current_deck, dealer_cards)
        dealer_score = calculate_score_values(dealer_cards)
        print()
        time.sleep(1.2)

    print("Dealer has : ",join_and(dealer_cards))
    print(f"Dealer's Score : {dealer_score}")
    if bust(dealer_score, DEALER):
        dealer_score = 0

    return dealer_score

def compare_cards(player_score, dealer_score):
    print(f"\nYour Score : {player_score}")
    print(f"Dealer's Score : {dealer_score}")

    if player_score < dealer_score:
        display_winner(DEALER.capitalize())
    elif player_score > dealer_score:
        display_winner(PLAYER.capitalize())
    else:
        print("< ----- > It's a TIE. < ----- > ")

def play_game(deck, cards):
    player_score = player_turn(deck, cards[PLAYER],
                                cards[DEALER][0])
    clear_screen()
    if player_score:
        dealer_score = dealer_turn(deck, cards[DEALER])

        if dealer_score:
            compare_cards(player_score, dealer_score)
        else:
            display_winner(PLAYER)

    else:
        display_winner(DEALER)

def play_again(prompt):
    ''' asks the user if he wants to play again '''
    again = ' '
    while again not in ['y', 'n', 'yes', 'no']:
        print()
        again = input(MESSAGES[prompt])
        again = again.strip().lower()

    if again[0] == 'n':
        return False

    return True

def main():
    display_welcome_screen()
    while True:
        os.system("cls || clear")
        cards = {
            PLAYER : [],
            DEALER : []
        }
        deck = intialize_deck()
        deal_cards(deck, cards)
        play_game(deck, cards)

        if not play_again("play_again"):
            print(MESSAGES["goodbye"])
            break

main()