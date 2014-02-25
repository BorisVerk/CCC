with open('s1.in', 'r') as infile:
    jersey_num = int(infile.readline()) - 1
print (jersey_num * (jersey_num-1) * (jersey_num-2))/6 #combinations, man.
