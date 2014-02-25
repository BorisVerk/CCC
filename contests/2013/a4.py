

def is_taller(taller_person, shorter_person, search_tree):
    """
    returns 'yes' if taller_person is taller than shorter_person
    returns 'no' if shorter_person turns out to be the taller person
    returns 'unknown' if it cannot be determined (as per the problem's specifications)
    uses a Breadth first Search through the "search_tree"
    """

    # visited is a list for tracking which people have already been searched
    # (so that we don't go to same guy more than once and get stuck in a loop)
    visited = [False for i in xrange(len(search_tree))]
        
    #get all the people we know to be shorter than taller_person
    queue = search_tree[taller_person]

    while len(queue) > 0:
        # take the first person of that list
        current_person = queue.pop()
        
        # if this person is the "shorter_person" we are looking for, we are done
        if current_person == shorter_person: return 'yes'

        # if not, then make sure we haven't already searched this person
        if not visited[current_person]:
            # add him to the list of people we need to search
            for link in search_tree[current_person]:
                queue.append(link)
            
            # mark him as visited if we ever encounter them in the future
            visited[current_person] = True

                
    # if we have looked through every possible link that the tallest person
    # connects to and still haven't found the shorter person, then there is
    # either no link between the two or the shorter person is actually taller
    
    # to make sure the person we think is taller isn't shorter than the person
    # we think was shorter, repeat the code, but flip the people we are testing
    visited = [False for i in xrange(len(search_tree))]
    queue = search_tree[shorter_person]

    while queue:
        current_person = queue.pop()
        
        if current_person == taller_person: return 'no'
        if not visited[current_person]:
            for link in search_tree[current_person]: queue.append(link) 
            visited[current_person] = True    

    # if we've gotten this far and we dont know which person is taller, there
    # must be no comparison which would link the two people together, and
    # therefore, it is impossible to know    
    return 'unknown'
         
 
with open('s4.in', 'r') as infile:
    class_size, total_comparisons = [int(i) for i in infile.readline().split()]
 
    # search_tree is the array holding all the links (comparisons between people)
    # it is a list of lists, where the INDEX of the inner list
    # is a PERSON, and the elements withing that list
    # are other people shorter than the PERSON they are in
    search_tree = [[] for i in xrange(class_size)]    
    
    for i in xrange(total_comparisons):
        # the 1 is subtracted to make a zero indexed array
        taller_person, shorter_person = [int(i)-1 for i in infile.readline().split()]
        search_tree[taller_person].append(shorter_person)
     
    taller_person, shorter_person = [int(person)-1 for person in infile.readline().split()]
   
print is_taller(taller_person, shorter_person, search_tree)
