# array starts at 1,1. what is this, amateur hour?

with open('s5.in', 'r') as infile:
    row, col = [int(x)-1 for x in infile.readline().split(' ')] #the minus 1 is to force a 0 indexed array
    infile.readline() # dont need to know how many lines remain in the file

    cat_cages = []
    for line in infile:
        x, y = [int(x)-1 for x in line.split(' ')] #subtract 1 just like for row, col
        cat_cages.append((x, y))

all_cages = {(x, y): 0 for x in range(row+1) for y in range(col+1)}
all_cages[(0, 0)] = 1

def get_neighbors(x, y):
    return [all_cages.get((x-1, y), 0), all_cages.get((x, y-1), 0)]

for x in range(row+1):
    for y in range(col+1):
        #skip the first spot, it was initialized to 1 earlier
        if (x, y) == (0, 0): continue

        total_paths_to_point = sum(get_neighbors(x, y))

        #if it's a cat cage then there are 0 paths to it because we will never visit it.
        #otherwise, it is a mathematical fact that the total number of paths to a node
        #on a grid is equal to the sum of paths to the nodes that lead to it.
        #in simpler terms, if there are 4 ways to get to a cage from the top
        #and 5 ways to get to it from the left, there are 9 total ways to get to it.
        all_cages[(x, y)] = 0 if (x, y) in cat_cages else total_paths_to_point

print all_cages[(row, col)]