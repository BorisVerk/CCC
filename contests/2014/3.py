#not completed

def throw_in_lake(mountain):
    branch = []

    current_car = 1
    while mountain:
        car = mountain.pop()
        if car == current_car:
            continue #Throw it in the lake
        elif car == (current_car + 1) and current_car not in mountain:
            current_car += 1
        else:
            branch.append(car)

tests = int(infile.readline())

for test in range(tests):
    len_cars = int(infile.readline())
    mountain = []
    for _ in range(len_cars):
        car = int(infile.readline())
        mountain.append(car)
    print throw_in_lake(mountain)