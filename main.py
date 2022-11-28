import pandas as pd
import numpy as np

# Read the data
data = pd.read_csv('data.csv')

# First, determine the score we would bet
aWin = '1-0'
xWin = '0-0'
bWin = '0-1'

# Choose the bigger cote
data['bet'] = np.where(data['coteA'] > data['coteX'], np.where(data['coteA'] > data['coteB'], aWin, bWin), np.where(data['coteX'] > data['coteB'], xWin, bWin))

# Choose the smaller cote
#data['bet'] = np.where(data['coteA'] < data['coteX'], np.where(data['coteA'] < data['coteB'], aWin, bWin), np.where(data['coteX'] < data['coteB'], xWin, bWin))

# Always bet xWin
#ata['bet'] = xWin

# split into betA, betB
data[['betA', 'betB']] = data['bet'].str.split('-', expand=True)

# remove the bet column
data = data.drop('bet', axis=1)

# Then, determine the points we would win
for index, row in data.iterrows():
    if row['betA'] == str(row['scoreA']) and row['betB'] == str(row['scoreB']):
        if row['betA'] > row['betB']:
            data.at[index, 'points'] = row['coteA'] * 2
        elif row['betA'] < row['betB']:
            data.at[index, 'points'] = row['coteB'] * 2
        else:
            data.at[index, 'points'] = row['coteX'] * 2
    # If scoreA won and we bet on A
    elif row['betA'] > row['betB'] and row['scoreA'] > row['scoreB']:
        data.at[index, 'points'] = row['coteA']
    # If scoreB won and we bet on B
    elif row['betB'] > row['betA'] and row['scoreB'] > row['scoreA']:
        data.at[index, 'points'] = row['coteB']
    # if scoreA == scoreB and we bet on X
    elif row['betA'] == row['betB'] and row['scoreA'] == row['scoreB']:
        data.at[index, 'points'] = row['coteX']
    # Else we lose the bet
    else:
        data.at[index, 'points'] = 0

# Finally, we sum the points
print(data['points'].sum())

print(data)