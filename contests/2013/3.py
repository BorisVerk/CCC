from itertools import combinations, product as cartesian_product

infile = open('/Users/HDD/src/CCC/contests/2013/s3.in', 'r')


team = int(infile.readline().strip())
games = int(infile.readline().strip())
games_remaining = 6 - games

# Stores the score of each team
scores = {1: 0, 2: 0, 3: 0, 4: 0}

games_left = [comb for comb in combinations(scores.keys(), 2)]

#populate scores and determine which games have yet to be played
for line in infile:
    parsed_line = [int(x) for x in line.split()]
    teamA = parsed_line[0]
    teamB = parsed_line[1]
    scoreA = parsed_line[2]
    scoreB = parsed_line[3]
    
    if scoreA > scoreB:
        scores[teamA] += 3
    elif scoreA < scoreB:
        scores[teamB] += 3
    else:
        scores[teamA] += 1 
        scores[teamB] += 1
    games_left.remove((min(teamA, teamB), max(teamA, teamB)))

infile.close()

possible_wins = 0
outcomes = ["win", "loss", "tie"]

for possible_outcomes in cartesian_product(outcomes, repeat=games_remaining):
    temp_scores = scores.copy()

    for x in range(games_remaining):
        if possible_outcomes[x] == "win":
            temp_scores[games_left[x][0]] += 3
        elif possible_outcomes[x] == "loss":
            temp_scores[games_left[x][1]] += 3
        else:
            temp_scores[games_left[x][0]] += 1
            temp_scores[games_left[x][1]] += 1
    
    points = temp_scores.values()
    if  temp_scores[team] == max(points) and points.count(max(points)) == 1:
        possible_wins += 1

print possible_wins