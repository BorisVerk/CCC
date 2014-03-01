def is_unique(pairs):
    for first, second in pairs.iteritems():
        if first != pairs[second] or first == second:
            return 'bad'
    return 'good'

num_of_students = int(raw_input()) #unnecessary
first_pair = raw_input().strip().split()
second_pair = raw_input().strip().split()

partners = zip(first_pair, second_pair)
pairs = {first: second for first, second in partners}

print is_unique(pairs)