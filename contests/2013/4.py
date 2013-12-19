# I refuse to name my variables as archaically as the spesifications suggest
infile = open("/Users/HDD/src/CCC/contests/2013/s4.in", "r")

first_line = infile.readline().split(" ")
class_size, comparisons_done = int(first_line[0]), int(first_line[1])

data = []
for x in xrange(comparisons_done):
    line = infile.readline().split(" ")
    (taller, shorter) = (int(line[0]), int(line[1])) #useless line for readability
    data.append((taller, shorter))

last_line = infile.readline().split(" ")
personA, personB = int(last_line[0]), int(last_line[1])

infile.close()


#now what?