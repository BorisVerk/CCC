rounds = int(raw_input())
score_a = 100
score_b = 100

for round in range(rounds):
    a_roll, b_roll = [int(x) for x in raw_input().strip().split()]
    if a_roll == b_roll:
        continue
    if a_roll > b_roll:
        score_b -= a_roll
    else:
        score_a -= b_roll

print score_a
print score_b
