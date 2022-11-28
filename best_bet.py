import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the data
data = pd.read_csv('data.csv')

# Generate all score possible (ex 0-0, 2-1), A should always be more than B
bets = [[i,j, 0, 0] for i in range(0, 10) for j in range(0, 10)]

# Then, determine the points we would win
def get_points(bet, score, cote):
    if bet[0] == score[0] and bet[1] == score[1]:
        if bet[0] == bet[1]:
            return cote[1] * 2
        elif bet[0] > bet[1]:
            return cote[0] * 2
        else:
            return cote[2] * 2
    elif bet[0] > bet[1] and score[0] > score[1]:
        return cote[0]
    elif bet[0] < bet[1] and score[0] < score[1]:
        return cote[2]
    elif bet[0] == bet[1] and score[0] == score[1]:
        return cote[1]
    else:
        return 0

# Test all bets
for i in range(0, len(data)):
    for bet in bets:
        points = get_points(bet, data.iloc[i][['scoreA', 'scoreB']], data.iloc[i][['coteA', 'coteX', 'coteB']])
        bet[2] += points
        bet[3] += 1

# Print the best bets when A win, B win and draw with average points
print('Best bets when A win: {} with sum of {} points and avg of {} points'.format(max(bets, key=lambda x: x[2] if x[0] > x[1] else 0), max(bets, key=lambda x: x[2] if x[0] > x[1] else 0)[2], max(bets, key=lambda x: x[2] if x[0] > x[1] else 0)[2] / max(bets, key=lambda x: x[2] if x[0] > x[1] else 0)[3]))
print('Best bets when B win: {} with sum of {} points and avg of {} points'.format(max(bets, key=lambda x: x[2] if x[0] < x[1] else 0), max(bets, key=lambda x: x[2] if x[0] < x[1] else 0)[2], max(bets, key=lambda x: x[2] if x[0] < x[1] else 0)[2] / max(bets, key=lambda x: x[2] if x[0] < x[1] else 0)[3]))
print('Best bets when draw: {} with sum of {} points and avg of {} points'.format(max(bets, key=lambda x: x[2] if x[0] == x[1] else 0), max(bets, key=lambda x: x[2] if x[0] == x[1] else 0)[2], max(bets, key=lambda x: x[2] if x[0] == x[1] else 0)[2] / max(bets, key=lambda x: x[2] if x[0] == x[1] else 0)[3]))
# Get the best bet
best_bet = max(bets, key=lambda x: x[2])
print('* Best bet is {}-{} with total of {} points'.format(best_bet[0], best_bet[1], best_bet[2]))

# Worst bet
worst_bet = min(bets, key=lambda x: x[2])
print('* Worst bet is {}-{} with total of {} points'.format(worst_bet[0], worst_bet[1], worst_bet[2]))
