def is_unique(pairs):
    for first, second in pairs.iteritems():
        if first != pairs[second] or first == second:
            return 'bad'
    else:
        return 'good'

with open('s2.in', 'r') as infile:
    num_of_students = int(infile.readline()) #unnecessary
    first_pair = infile.readline().strip().split()
    second_pair = infile.readline().strip().split()

partners = zip(first_pair, second_pair)
pairs = {first: second for first, second in partners}

print is_unique(pairs)