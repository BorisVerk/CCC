with open('s2.in', 'r') as infile:
    max_weight = int(infile.readline())
    how_many_cars = int(infile.readline())
    all_cars = [int(line) for line in infile]

BRIDGE_SIZE = 4
bridge = list()

for i, car in enumerate(all_cars):
    if len(bridge) == BRIDGE_SIZE:
        bridge.pop(0)

    bridge.append(car)

    if sum(bridge) > max_weight:
        print i
        break #is this a pun?
else:
    print how_many_cars
