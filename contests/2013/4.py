def is_taller(taller_person, shorter_person, search_tree):

    que = search_tree[taller_person]
    visited = [False for _ in range(len(search_tree))]

    while que:
        if shorter_person in que:
            return 'yes'

        x = que.pop()
        if not visited[x]:
            for i in search_tree[x]:
                que.append(i)
            visited[x] = True

    que = search_tree[shorter_person]
    visited = [False for _ in range(len(search_tree))]

    while que:
        if taller_person in que:
            return 'no'

        x = que.pop()
        if not visited[x]:
            for i in search_tree[x]:
                que.append(i)
            visited[x] = True


    return 'unknown'


with open('s4.in', 'r') as infile:
    class_size, comparisons = [int(i) for i in infile.readline().split()]

    search_tree = [[] for i in range(class_size + 1)]

    for _ in range(comparisons):
        x, y = [int(i) for i in infile.readline().split()]
        search_tree[x].append(y)

    p, q = [int(i) for i in infile.readline().split()]

    print is_taller(p, q, search_tree)