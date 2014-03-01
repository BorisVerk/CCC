#not completed

def what_does_the_fox_say():
    return 'YIP YIPIAAIIAIAPYIYIYPIAAIYAIAIYYAA'

def what_does_the_fox_eat(points):


total_positions = int(infile.readline())
points = []

for _ in xrange(total_positions):
    x, y = map(int, infile.readline().split(' '))
    points.append((x, y))

print what_does_the_fox_eat(points)