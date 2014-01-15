#started at 107am

import random
random.seed()

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
    
    coins = [[x] for x in coins]
    
            

with open('s4.in', 'r') as infile:
    n = int(infile.readline().strip())
    while n != 0:
        coins = [int(x) for x in infile.readline().strip().split()]
        print calculate(coins)
        n = int(infile.readline().strip())