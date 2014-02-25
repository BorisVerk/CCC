#started at 107am-pause 155 -nothing done besides parsing

#note: when actually doing the competition, read all 5 problems first, then
#actually begin writing. This is the 4th problem, but the fifth
#is much more doable
"""
def all_possible_moves(coin_list):
    all_moves = []
    for coin_stack in range(1, len(coinlist)):
        if coin_list[coin_stack]:
            coin = coin_list[coin_stack][0]
            if can_move

def calculate(coins):
    if len(coins) == 1:
        return '0'
    if len(coins) == 2:
        if coins == sorted(coins):
            return '0'
        else: return 'IMPOSSIBLE'
    if len(coins) == 3:
        coins_string = ''
        for x in coins: coins_string += str(x)
        answers = {'321': 20, '312': 16, '132': 12, '231': 8, '213': 4}
        return answers[coins_string]
    
    search_tree = [[[x] for x in coins]]
    visited = []
    moves = 0
    while search_tree:
        element = search_tree.pop()
        if element not in visited:
            visited.append(element)
            if element == sorted(coins):
                return moves
            for move_from_element in all_possible_moves(element):
                if move_from_element not in visited:
                    search_tree.append(move_from_element)
    
    return 'IMPOSSIBLE - Error'
            

with open('s4.in', 'r') as infile:
    n = int(infile.readline().strip())
    while n != 0:
        coins = [int(x) for x in infile.readline().strip().split()]
        print calculate(coins)
        n = int(infile.readline().strip())

        """

# S4 2012: A Coin Game
#
# this is a brute force, Breadth First Search
# of the game tree.
#
# Version 4: a move, or state is an array (of strings)
#
# This is version is due to help and insights of
# Daniel Hui, Amlesh Jayakumar, Daniel Cressman and Kevin Luo.
#
# The idea is that there will be LOTS of moves stored in the
# game tree and before you can add a new one, you have to
# determine if it's already in the tree.
# Doing a search thru the tree takes too long.
#
# So consider the arrangement "35/4/_/2/1"
# That could be thought of as 43010 (in base 5)
# because the 1 is in position 4, 2 in 3,
# 3 in 0, 4 in 1 and the the 5 in position 0 as well.
#
# Now take that number, 43010 and convert it to base 10
# using this method: 4*5^0 + 3*5^1 + 0*5^2 + 1*5^3 + 0*5^4
# = 144.
#
# Now use that number as the index to a visited array.
# Visited is started as all False. As we generate moves,
# the visited array (for that number/move) is set to True
# and we don't "visit" it again.
#
# the size of visited is n^n because the "worst case" is
# "_/_/_/_/12345" which translates to 44444 (in base 5)
# which is one less than 100000 (base 5) or 5^5 base 10.
#

n = 0
visited = []

class Node:
    def __init__(self, m, l):
        self.m = m
        self.level = l

def done (move):
    global n
    i = 0
    while i < n and move[i] == str(i+1):
        i = i + 1
    return i == n

def movetoBaseN (move):
    global n
    basen = 0
    for i in range(n):
        for j in range (len(move[i])):
            x = int(move[i][j]) - 1
            basen += i * n**x
    return basen

#creates a new move, given an oldmove and two positions,
# p1 is the position to take from, p2 - add to
def createNewMove (oldmove, p1, p2):
    global n
    newmove = []
    for i in range (n):
        newmove.append(oldmove[i])

    newmove[p2] = newmove[p1][0:1] + newmove[p2]
    newmove[p1] = newmove[p1][1:]

    # don't allow big guy to move left
    if p2 < p1 and newmove[p2][0:1] == str(n):
        return oldmove
    else:
        return newmove

def search(move):
    global n
    if done(move):
        return 0
    else:
        tree = []
        tree.append(Node(move,0))
        while len(tree) > 0:
            x = tree.pop(0)
            for i in range(n):
                # move right
                if i < n-1:
                    if len(x.m[i+1]) == 0 or x.m[i][0:1] < x.m[i+1][0:1]:
                        newmove = createNewMove(x.m, i, i+1)
                        bn = movetoBaseN (newmove)
                        if not visited[bn]:
                            visited[bn] = True
                            tree.append(Node(newmove,x.level + 1))
                            if done(newmove):
                                return x.level + 1
                # move left
                if i > 0:
                    if len(x.m[i-1]) == 0 or x.m[i][0:1] < x.m[i-1][0:1]:
                        newmove = createNewMove(x.m, i, i-1)
                        bn = movetoBaseN (newmove)
                        if not visited[bn]:
                            visited[bn] = True
                            tree.append(Node(newmove,x.level + 1))
                            if done(newmove):
                                return x.level + 1

        return "IMPOSSIBLE"

file = open("s4.in", 'r')
n = eval(file.readline().strip())
while n > 0:
    # create and initialize a visited array
    # of all possible moves to false
    visited = []
    size = n**n
    for i in range(size + 1):
        visited.append(False)

    move = file.readline().strip().split()
    print search(move)
    n = eval(file.readline().strip())