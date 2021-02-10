# Bet Starter File

# NOTE: You can run this file locally to test if your program is working.

#=============================================================================

# INPUT FORMAT: hand, others, card, scores

# hand: Your current hand (a list of integers 2 to 14)
# others: All other players' hands, in a fixed order
# card: The card currently being bet on (an integer 2 to 14)
# scores: All current scores of players (from this game only) in a
#   fixed order. Your score is displayed as the first value.

# Example Input:

# hand: [2, 4, 14]
# others: [[6, 8, 9], [5, 11, 13]]
# card: 9
# scores: [34, 21, 18]

#=============================================================================

# OUTPUT FORMAT: A single integer between 2 and 14, inclusive, that is
# currently in your hand.

# Invalid outputs will result in your lowest card being played by default.

### WARNING: COMMENT OUT YOUR DEBUG/PRINT STATEMENTS BEFORE SUBMITTING !!!
### (this file uses standard IO to communicate with the grader!)

#=============================================================================

# Write your bot in the bet_bot class. Helper functions and standard library
# modules are allowed, and can be written before/inside these classes.

# You can define as many different strategies as you like, but only the class
# currently named "bet_bot" will be run officially.


# Example bot that plays a random card every round:

import random

class new_bot:
    def __init__(self):
        # You can define global states (that last between moves) here
        self.history = []
        pass
    
    def move(self, hand, others, card, scores):
        # You should write your code that moves every turn here
        self.history.append([hand,others])
        
        # if LOCAL_VIEW: print(self.history)        

        #attempts to pick some of the biggest cards
        biggestCards = sorted(hand, reverse=True)
        
        other_biggest_cards = []
        for other in others:
          other_sorted = sorted(other, reverse=True)
          other_biggest_cards.append(other_sorted[0])

        other_biggest_cards = sorted(other_biggest_cards)
        if LOCAL_VIEW: print(other_biggest_cards)

        if card > 10:
          if biggestCards[0] > other_biggest_cards[1]:
            return biggestCards[0]
          else:
            if len(hand) < 4:
              return biggestCards[-1]
            return biggestCards[3]
        elif card > 6:
          if biggestCards[0] > other_biggest_cards[1]:
            if len(hand) == 1:
              return hand[0]
            return biggestCards[1]
          else:
            return biggestCards[-1]
        else:
          return biggestCards[-1]

class bet_bot:
    def __init__(self):
        # You can define global states (that last between moves) here
        pass
    
    def move(self, hand, others, card, scores):
        # You should write your code that moves every turn here
        biggestCards = sorted(hand, reverse=True)

        if card > 10:
          return biggestCards[0]
        elif card > 7:
          if len(hand) == 1:
            return hand[0]
          else:
            return biggestCards[1]
        else:
          return biggestCards[-1]

class random_bot:
    def __init__(self):
        # You can define global states (that last between moves) here
        pass
    
    def move(self, hand, others, card, scores):
        # You should write your code that moves every turn here
        
        return random.choice(hand)

#=============================================================================

# Local testing parameters

# If you would like to view a turn by turn game display while testing locally,
# set this parameter to True

LOCAL_VIEW = False

# Set a list of 3 strategies you would like to test locally

LOCAL_STRATS = [bet_bot(), bet_bot(), bet_bot()]

#=============================================================================












































# You don't need to change any code below this point

import json
import sys

def WAIT():
    return json.loads(input())

def SEND(data):
    print(json.dumps(data), flush=True)

MASK = lambda a,i: a[:i] + a[i+1:]

def PLAY(players):
    total = [0] * 3
    for ROUND in range(1, 6):
        scores = [0] * 3
        hands = [[*range(2, 15)] for i in range(3)]
        deck = [*range(2, 15)]
        if LOCAL_VIEW:
            print("ROUND",ROUND)
        for _ in range(13):
            card = random.choice(deck)
            deck.remove(card)
            if LOCAL_VIEW:
                for i in range(3):
                    print(f"Player {i+1}'s hand:", ' '.join(map(str, hands[i])))
                print("Card being bet on:", card)
            values = []
            for i in range(3):
                try:
                    val=players[i].move(hands[i],MASK(hands,i),card,[scores[i]]+MASK(scores,i))
                    if not (val==int(val) and val in hands[i]):
                        raise Exception('invalid move')
                except Exception as e:
                    print(f"Player {i+1} has an error: {e}! Playing the lowest card instead.")
                    val = min(hands[i])
                values.append(val)
                if LOCAL_VIEW:
                    print(f"Player {i+1}'s bet:", val)
            for i in range(3):
                hands[i].remove(values[i])
            big = max(values)
            if values.count(big) == 1:
                if LOCAL_VIEW:
                    print(f"Player {values.index(big)+1} has won the card!")
                scores[values.index(big)] += card
            else:
                if LOCAL_VIEW:
                    print("There was a tie! Nobody won the card.")
            if LOCAL_VIEW:
                print("Current totals:", ' '.join(map(str, scores)))
                print()
                input("Enter to continue (change LOCAL_VIEW to toggle this)")
        for i in range(3):
            scores[i] /= 100
        big = max(scores)
        tie = scores.count(big)
        if tie == 3:
            for i in range(3):
                scores[i] += 1
        elif tie == 2:
            for i in range(3):
                if scores[i] == big:
                    scores[i] += 2
                else:
                    scores[i] += 1
        else:
            index = scores.index(big)
            scores[index] += 5
            small = min(scores)
            for i in range(3):
                if scores[i] == small:
                    scores[i] += 1
                elif i != index:
                    scores[i] += 2
        for i in range(3):
            total[i] += scores[i]
        print()
        print("Round",ROUND,"scores:",' '.join(map(str, scores)))
        print()
    print("Game finished!")
    print("Final scores:",' '.join(map(str, total)))
    if not LOCAL_VIEW:
        print("Change LOCAL_VIEW to True to see a turn by turn replay")

if len(sys.argv) < 2 or sys.argv[1] != 'REAL':
    PLAY(LOCAL_STRATS)
    input()

else:
    player = bet_bot()
    while True:
        data = WAIT()
        play = player.move(data["hand"],data["others"],data["card"],data["scores"])
        SEND(play)