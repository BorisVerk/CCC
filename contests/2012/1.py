#started this year at 2225
# note to self: Need a refresher on perms and esspecially combinations

with open('s1.in', 'r') as infile:
    jersey_num = int(infile.readline().strip()) - 1
    print (jersey_num * (jersey_num-1) * (jersey_num-2))/6