#started at 107am-pause 155 -nothing done besides parsing

#note: when actually doing the competition, read all 5 problems first, then
#actually begin writing. This is the 4th problem, but the fifth
#is much more doable

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