import sys
# I refuse to name my variables as archaically as the spesifications suggest
infile = open("/Users/HDD/src/CCC/contests/2013/s4.in", "r")

first_line = infile.readline().split(" ")
class_size, comparisons_done = int(first_line[0]), int(first_line[1])

print class_size

data = {}
for x in xrange(comparisons_done):
    line = infile.readline().split(" ")
    (taller, shorter) = (int(line[0]), int(line[1])) # Useless line for readability
    data[(taller, shorter)] = False # Flag used for searching

last_line = infile.readline().split(" ")
personA, personB = int(last_line[0]), int(last_line[1])

infile.close()

# Everything bellow is super rough, doesn't work. it's 7am I gotta sleep
search_space = [personA]

def search():
    for element in search_space:
        if (element, personB) in data.keys():
            return "yes"
        elif (personB, element) in data.keys():
            return "no"
        else:
            for i in xrange(class_size):
                if (element, i) in data.keys() and data[(element, i)] == False:
                    search_space.append(i)
                    data[(element, i)] = False
                    something_happened = True
    if something_happened:
        return search()
    else:
        sys.exit("unknown")
    
        
print search()