# again, not my solution
# note to self, rewrite this to learn to use nested lists

# returns true if person_one is taller than person_two
# uses a Breadth first Search thru the "search_tree" tree of size class_size
def taller(search_tree, class_size, person_one, person_two):
    # visited is a "visited" list for tracking (don't go to same guy twice)
    visited = []
    for r in range(class_size):
        visited.append(False)    
    
    queue = []
    for link in search_tree[person_one]:
        queue.append(link)
    while len(queue) > 0:
        current_person = queue.pop(0)
        if current_person == person_two:
            return True
        if not visited[current_person]:
            visited[current_person] = True
            for link in search_tree[current_person]:
                queue.append(link)
    return False
         
 
with open("s4.in", 'r') as infile:
    line = infile.readline().strip().split(" ")
    class_size = int(line[0])
    total_comparisons = int(line[1])
 
    # search_tree is the main array holding all the links
    # it is a list of lists, where the index of the inner list
    # is the person, and the elements withing that list
    # are other people shorter than the index they are in
    search_tree = []
    for i in range(class_size):
        row = []
        search_tree.append(row)
    
    
    for i in range(total_comparisons):
        line = infile.readline().strip().split()
        #the 1 is substracted to make a zero indexed array
        person_one = int(line[0]) - 1 
        person_two = int(line[1]) - 1
        search_tree[person_one].append(person_two)
     
    line = infile.readline().strip().split()
    person_one = int(line[0]) - 1
    person_two = int(line[1]) - 1
   
if taller(search_tree, class_size, person_one, person_two): print "yes"
elif taller(search_tree, class_size, person_two, person_one): print "no"
else: print "unknown"
    