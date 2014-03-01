raw_input() #don't need the first line
votes = raw_input().strip()

a_count = votes.count('A')
b_count = votes.count('B')

if a_count > b_count:
    print 'A'
elif b_count > a_count:
    print 'B'
else:
    print 'Tie'
