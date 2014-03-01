with open('s2.in', 'r') as infile:
    n_questions = int(infile.readline().strip())
    answers = [infile.readline().strip() for _ in xrange(n_questions)]
    key = [infile.readline().strip() for _ in xrange(n_questions)]

test_score = 0
for answer, key in zip(answers, keys):
    if answer == key:
        test_score = test_score + 1
print test_score
