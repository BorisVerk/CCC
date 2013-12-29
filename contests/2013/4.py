infile = open("/Users/HDD/src/CCC/contests/2013/s4.in", "r")

first_line = infile.readline().split(" ")
class_size, comparisons_done = int(first_line[0]), int(first_line[1])

data = []
for x in xrange(comparisons_done):
    line = infile.readline().split(" ")
    (taller, shorter) = (int(line[0]), int(line[1]))
    data.append((taller, shorter))

last_line = infile.readline().split(" ")
personA, personB = int(last_line[0]), int(last_line[1])

infile.close()

search_space = [personA]

def search(search_space):
    new_search_space = []
    something_happened = False
    for element in search_space:
        if (element, personB) in data:
            return "yes"
        elif (personB, element) in data:
            return "no"
        else:
            for i in xrange(class_size):
                if (element, i) in data:
                    new_search_space.append(i)
                    data.remove((element, i))
                    something_happened = True
    if something_happened:
        search_space = new_search_space
        return search(search_space)
    else:
        return "unknown"
                    
    
    
print search(search_space)
