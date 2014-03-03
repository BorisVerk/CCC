def throw_in_lake(mountain):
    branch = []
    current_car = min(mountain)

    while len(mountain) + len(branch) > 0:
        if current_car

    return 'Y'


with open('s3.in', 'r') as infile:
    tests = int(infile.readline())

    for test in range(tests):
        len_cars = int(infile.readline())
        mountain = []
        for _ in range(len_cars):
            car = int(infile.readline())
            mountain.append(car)
        print throw_in_lake(mountain)