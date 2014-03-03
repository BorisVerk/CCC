from itertools import combinations
from copy import deepcopy

with open('s3.in', 'r') as infile:

    team = int(infile.readline().strip())
    games = int(infile.readline().strip())
    games_remaining = 6 - games

    # Stores the score of each team
    scores = {1: 0, 2: 0, 3: 0, 4: 0}

    # All possible combinations of 2 teams
    games_left = list(combinations(scores.keys(), 2))

    # Populate scores and determine which games have yet to be played
    for line in infile:
        teamA, teamB, scoreA, scoreB = [int(x) for x in line.split()]
        
        if scoreA > scoreB:
            scores[teamA] += 3
        elif scoreA < scoreB:
            scores[teamB] += 3
        else:
            scores[teamA] += 1 
            scores[teamB] += 1
        games_left.remove((min(teamA, teamB), max(teamA, teamB)))

possible_wins = 0
outcomes = ["win", "loss", "tie"]

def product(iterable, repeat):
    result = [[]]
    for pool in ([iterable] * repeat):
        result = [x+[y] for x in result for y in pool]
    return result

for possible_outcomes in product(outcomes, games_remaining):
    
    temp_scores = deepcopy(scores)

    for x in range(games_remaining):
        if possible_outcomes[x] == "win":
            temp_scores[games_left[x][0]] += 3
        elif possible_outcomes[x] == "loss":
            temp_scores[games_left[x][1]] += 3
        else:
            temp_scores[games_left[x][0]] += 1
            temp_scores[games_left[x][1]] += 1
    
    points = temp_scores.values()
    winning_score = max(points)
    if  temp_scores[team] == winning_score and points.count(winning_score) == 1:
        possible_wins += 1


print possible_wins