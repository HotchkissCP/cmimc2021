import json
import copy

fileName = str(input("Please type the exact file name of the match you want to visualize. Ensure that your match data and this file are in the same directory:\n"))

with open (fileName) as f:
    data = json.load(f)

table = [['0' for i in range(7)] for j in range(13)]

numRounds = len(data['gamedata'])
print("There are {} games in this match.".format(numRounds))
index = int(input("Enter which game you want to view from 1 to {}:\n".format(numRounds)))
assert index > 0 and index < numRounds+1,"Did not enter valid game number."
seatNum = data['seat']

for item in data['gamedata'][index-1]['hist']: 
    # each item is a round corresponding to one of the 13 cards from the deck
    table[item['time']-1][0] = item['card']
    
    for i in range(3):
        table[item['time']-1][i+1] = item['moves'][i]['using']
    if item['moves'][seatNum-1]['got'] == [] or item['moves'][seatNum-1]['got']!=item['moves'][seatNum-1]['using']:
        table[item['time']-1][3+seatNum] = item['moves'][seatNum-1]['error']

output = "\nYou are P1. Your opponents are P2 and P3.\n\n"
totals = {}
totals["P1"] = 0
totals["P2"] = 0
totals["P3"] = 0

for row in table:
    scores = {}
    scores["P1"] = row[seatNum]
    if seatNum == 1:
        scores["P2"] = row[2]
        scores["P3"] = row[3]
    elif seatNum == 2:
        scores["P2"] = row[1]
        scores["P3"] = row[3]  
    else:
        scores["P2"] = row[1]
        scores["P3"] = row[2]  
    

    vals = copy.deepcopy(row)
    vals = [vals[1],vals[2],vals[3]]
    scoresInc = sorted(vals)
    currRound = str(table.index(row)+1)
    if row[3+seatNum] == '0':     
        if scoresInc[2] != scoresInc[1]:
            player = max(scores, key=scores.get)
            added = "Round {}: {} wins {} points\n".format(currRound,player,str(row[0]))
            totals[player] += row[0]
        elif len(set(scoresInc))==2:
            a,b = [player for player, score in scores.items() if score == max(scores.values())]
            added = "Round {}: There was a collision between {} and {}\n".format(currRound,a,b)
        elif len(set(scoresInc))==1:
            added = "Round {}: There was a collision between P1, P2, and P3\n".format(currRound)
    else:
        added = "Round {}: Your code threw this error: {}.\n".format(currRound, row[3+seatNum])
        added += "Round {}: As a result, your lowest card was played.\n".format(currRound)
        if scoresInc[2] != scoresInc[1]:
            player = max(scores, key=scores.get)
            added += "Round {}: {} wins {} points\n".format(currRound,player,str(row[0]))
            totals[player] += row[0]
        elif len(set(scoresInc))==2:
            a,b = [player for player, score in scores.items() if score == max(scores.values())]
            added += "Round {}: There was a collision between {} and {}\n".format(currRound,a,b)
        elif len(set(scoresInc))==1:
            added += "Round {}: There was a collision between P1, P2, and P3\n".format(currRound)
    output += added

sortedTotals = {player: total for player, total in sorted(totals.items(), key=lambda item: item[1])}

print(output)

print("Player {} came in 1st place with a score of {}".format(list(sortedTotals)[2],list(sortedTotals.values())[2]))
print("Player {} came in 2nd place with a score of {}".format(list(sortedTotals)[1],list(sortedTotals.values())[1]))
print("Player {} came in 3rd place with a score of {}".format(list(sortedTotals)[0],list(sortedTotals.values())[0]))
yourScore = totals['P1']
yourRank = 3-list(sortedTotals).index('P1') 
rankPoints=[5,2,1]
yourRankPoints = rankPoints[2-list(sortedTotals).index('P1')]
bonusPoints = round(0.01*yourScore,3)
print("As a result, you ranked in place {} and received {} + {} = {} points for this game.".format(yourRank,yourRankPoints,bonusPoints,yourRankPoints+bonusPoints))