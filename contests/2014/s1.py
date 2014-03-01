with open('s1.in', 'r') as infile:
    how_many_people = int(raw_input())
    people = range(1, how_many_people+1) #you're a computer scientist, you should number your friends starting at 0

    how_many_rounds = int(raw_input())
    rounds = [int(raw_input()) for _ in range(how_many_rounds)]

for round in rounds:
    new_people = []
    for i, person in enumerate(people, start=1):
        if (i) % round is not 0:
            new_people.append(person)
    people = new_people

for person in people:
    print person