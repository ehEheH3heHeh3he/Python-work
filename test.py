from collections import Counter

def check_poker_hand(cards):
    ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'X': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    counts = Counter([card[0] for card in cards])
    suits = set([card[1] for card in cards])

    sorted_ranks = sorted([ranks[card[0]] for card in cards])

    straight = len(set(sorted_ranks)) == 5 and (max(sorted_ranks) - min(sorted_ranks) == 4)

    if len(suits) == 1 and straight:
        return "Straight Flush"
    elif len(suits) == 1:
        return "Flush"
    elif straight:
        return "Straight"
    elif 4 in counts.values():
        return "Four of a Kind"
    elif sorted(counts.values()) == [2, 3]:
        return "Full House"
    elif 3 in counts.values():
        return "Three of a Kind"
    elif list(counts.values()).count(2) == 4:
        return "Two Pair"
    elif 2 in counts.values():
        return "One Pair"
    else:
        return "High Card"

# usage:
hand = input("Enter your poker hand : ").split()
if len(hand) != 5:
    print("Invalid hand. Please provide exactly 5 cards.")
else:
    print("Your hand is:", check_poker_hand(hand))
