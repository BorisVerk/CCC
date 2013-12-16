#started at 1715
#finished at 1745

import sys
stdin = open('s2.in', 'r')
max_weight = int(stdin.readline())
how_many_cars = int(stdin.readline())
all_cars = [int(x) for x in stdin.read().split()]

BRIDGE_SIZE = 4
bridge = list()

for car in range(len(all_cars)):
    if car < BRIDGE_SIZE:
        bridge = all_cars[0:car + 1]
    else:
        bridge.pop(0)
        bridge.append(all_cars[car])
    if sum(bridge) > max_weight:
        print car
        sys.exit()
            
print how_many_cars
stdin.close()