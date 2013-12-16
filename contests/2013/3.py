#started 1745
#pause 1810-

infile = open('s3.in', 'r')

team = int(infile.readline().strip())
games = int(infile.readline().strip())
games_remaining = 6 - games

rankings = {1: 0, 2: 0, 3: 0, 4: 0}

games_played = {(1, 2): False,
                (1, 3): False,
                (1, 4): False,
                (2, 3): False,
                (2, 4): False,
                (3, 4): False}

for line in infile:
    parsed_line = [int(x) for x in line.split()]
    teamA = parsed_line[0]
    teamB = parsed_line[1]
    scoreA = parsed_line[2]
    scoreB = parsed_line[3]
    
    if scoreA > scoreB:
        rankings[teamA] += 3
    elif scoreA < scoreB:
        rankings[teamB] += 3
    else:
        rankings[teamA] += 1 
        rankings[teamB] += 1
    games_played[(min(teamA, teamB), max(teamA, teamB))] = True

for key in games_played:
    print key
    

infile.close()